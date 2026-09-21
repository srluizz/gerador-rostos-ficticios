import os
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="Gerador de Rostos Fictícios", page_icon="👤", layout="centered"
)

# --- SEÇÕES EXPLICATIVAS NA BARRA LATERAL ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400", caption="Ilustração de IA")
    
    st.markdown("### 🎯 Para que serve?")
    st.write(
        "Este aplicativo é útil para desenvolvedores, designers e criadores de conteúdo "
        "que precisam de **imagens de rostos humanos para testes**, protótipos de sistemas, "
        "bancos de dados de teste ou mockups de interface, **sem violar a privacidade** de pessoas reais."
    )
    
    st.markdown("---")
    
    st.markdown("### ⚙️ Como funciona?")
    st.markdown(
        "1. **IA Generativa:** O app se conecta ao site *This Person Does Not Exist*, que utiliza Redes Geradoras Adversariais (GANs) para criar rostos inéditos.\n"
        "2. **Automação:** Você escolhe quantas fotos quer baixar usando o controle deslizante.\n"
        "3. **Download Seguro:** O script faz requisições HTTP simulando um navegador real, adicionando um carimbo de tempo para garantir imagens sempre novas.\n"
        "4. **Armazenamento:** As imagens são salvas automaticamente em uma pasta local chamada `fotos_ficticias`."
    )

# --- INTERFACE PRINCIPAL ---
url = "https://thispersondoesnotexist.com/"
st.title("👤 Gerador de Rostos Fictícios")
st.write(
    f"Este aplicativo baixa rostos gerados por Inteligência Artificial do site [This Person Does Not Exist]({url})"
)

# Controles na interface
quantidade = st.slider("Quantas fotos você deseja baixar?", 1, 20, 5)
pasta_destino = "fotos_ficticias"

if st.button("Iniciar Download", type="primary"):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    base_url = "https://thispersondoesnotexist.com/random-person.jpeg"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": (
            "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
        ),
        "Referer": "https://thispersondoesnotexist.com/",
    }

    barra_progresso = st.progress(0)
    status_texto = st.empty()

    for i in range(1, quantidade + 1):
        status_texto.text(f"Baixando foto {i} de {quantidade}...")
        try:
            url_dinamica = f"{base_url}?t={int(time.time() * 1000)}"
            response = requests.get(url_dinamica, headers=headers, timeout=10)

            if response.status_code == 200:
                caminho_arquivo = os.path.join(pasta_destino, f"foto_{i:03d}.jpg")
                with open(caminho_arquivo, "wb") as f:
                    f.write(response.content)

                # Atualiza a barra de progresso
                barra_progresso.progress(i / quantidade)

            time.sleep(1)  # Intervalo para o servidor gerar outra face
        except Exception as e:
            st.error(f"Erro ao baixar a foto {i}: {e}")

    status_texto.success(
        f"Pronto! {quantidade} fotos salvas na pasta '{pasta_destino}'."
    )