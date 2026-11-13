# Automação de Download de Artigos (Sci-Hub)

Automação desenvolvida em Python para ler uma planilha em Excel (`.xlsx`), pesquisar e realizar o download automático de artigos científicos através do site Sci-Hub, salvando os arquivos em uma pasta específica e registrando o histórico de execução em um arquivo de log (`.txt`).

> **Nota:** Projeto desenvolvido com base nos ensinamentos de uma videoaula da **Hashtag Treinamentos**.

---

## Funcionalidades

- **Leitura de Planilha:** Percorre automaticamente uma lista de artigos (DOI, URL ou título) a partir de um arquivo `.xlsx`.
- **Busca e Download Automatizado:** Acessa a plataforma e baixa os arquivos PDF correspondentes.
- **Organização de Arquivos:** Salva todos os artigos baixados diretamente em um diretório pré-determinado.
- **Registro de Logs:** Gera um arquivo `.txt` detalhando o status de cada item processado (sucesso ou falha no download) para facilitar o acompanhamento.

---

## Tecnologias Utilizadas

* **Python 3.x**
* **Pandas / OpenPyXL** (para leitura e manipulação da planilha `.xlsx`)
* **Selenium / PyAutoGUI / Requests** *(ajuste conforme a biblioteca utilizada no seu código)*

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o **Python** instalado em sua máquina. Em seguida, instale as dependências necessárias executando:

```bash
pip install pandas openpyxl selenium
```
*(Altere ou adicione os pacotes acima de acordo com o arquivo `requirements.txt` ou imports do seu script).*

---

## Como Executar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com
   cd nome-do-repositorio
   ```

2. **Prepare a planilha de entrada:**
   - Certifique-se de que o arquivo `.xlsx` contenha a coluna esperada pelo script com os identificadores (DOI, link ou nome) dos artigos.

3. **Configure os caminhos (se necessário):**
   - Abra o arquivo principal (`main.py` ou equivalente) e verifique se os caminhos da planilha de entrada, da pasta de destino dos PDFs e do arquivo de `log.txt` estão corretos.

4. **Execute a automação:**
   ```bash
   python main.py
   ```

---

## Estrutura Sugerida do Projeto

```text
├── artigos_baixados/     # Pasta onde os PDFs serão salvos
├── lista_artigos.xlsx    # Planilha com a relação de artigos para pesquisa
├── log_execucao.txt      # Arquivo gerado com o histórico de downloads
├── main.py               # Código principal da automação
└── README.md             # Documentação do projeto
```

---

## Aviso Legal

Este projeto tem fins estritamente **educacionais** e de estudo sobre automação de processos com Python. Respeite as leis de direitos autorais e os termos de uso das plataformas acessadas.

---

## Créditos

- Desenvolvido a partir dos conteúdos práticos disponibilizados pela **[Hashtag Treinamentos](https://www.youtube.com/watch?v=EzD2AqRFe5I&t=326s)**.
