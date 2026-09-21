# 👤 Gerador de Rostos Fictícios

Um aplicativo web interativo desenvolvido em **Python** e **Streamlit** que automatiza o download de rostos humanos gerados por Inteligência Artificial em tempo real a partir do site *This Person Does Not Exist*.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Requests-005571?style=for-the-badge&logo=requests&logoColor=white" />
</div>

---

## Funcionalidades
* **Interface Web Amigável:** Painel interativo construído com Streamlit.
* **Controle Dinâmico:** Escolha a quantidade exata de imagens que deseja capturar através de um slider.
* **Barra de Progresso:** Acompanhamento visual em tempo real do status dos downloads.
* **Bypass de Cache:** Utiliza manipulação de parâmetros de tempo (`timestamp`) para garantir que o servidor gere novas faces a cada requisição.
* **Resiliência:** Tratamento de exceções para evitar interrupções caso ocorram falhas de conexão pontuais.

---

## Tecnologias Utilizadas
* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Requests](https://requests.readthedocs.io/)

---

## Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/srluizz/gerador-rostos-ficticios.git
   cd gerador-rostos-ficticios
   ```

2. **Instale as dependências:**
   ```bash
   pip install streamlit requests
   ```

3. **Execute o aplicativo:**
   ```bash
   streamlit run app.py
   ```

4. O aplicativo abrirá automaticamente no seu navegador padrão!

---

## Estrutura do Projeto
```text
ai-face-scraper/
│
├── app.py            # Código principal da aplicação Streamlit
├── fotos_ficticias/  # Pasta gerada automaticamente com as imagens baixadas
└── README.md         # Documentação do projeto
```

---

## Licença
Este projeto está sob a licença [MIT](LICENSE).