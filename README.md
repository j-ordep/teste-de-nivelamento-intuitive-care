# README - Teste de Nivelamento IntuitiveCare

Este repositório contém a implementação dos testes de nivelamento solicitados pela IntuitiveCare. Cada teste aborda diferentes habilidades técnicas, como web scraping, transformação de dados, manipulação de banco de dados e desenvolvimento de APIs. Abaixo, você encontrará uma descrição detalhada de cada teste e como executá-los.

---

## **1. Teste de Web Scraping**

### **Descrição**
Este teste consiste em realizar o download de arquivos PDF de um site, compactá-los e salvá-los em um único arquivo.

### **Tarefas**
1. Acessar o site: [Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos).
2. Fazer o download dos Anexos I e II em formato PDF.
3. Compactar os arquivos baixados em um único arquivo ZIP ou RAR.

### **Execução**
- Linguagens suportadas: **Python** ou **Java**.
- Certifique-se de ter as bibliotecas necessárias instaladas:
  - Python: `requests`, `beautifulsoup4`, `zipfile`.
  - Java: `Jsoup` ou bibliotecas equivalentes.

---

## **2. Teste de Transformação de Dados**

### **Descrição**
Este teste envolve a extração de dados de um PDF, transformação em formato estruturado e compactação.

### **Tarefas**
1. Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do **Anexo I** (todas as páginas).
2. Salvar os dados extraídos em um arquivo CSV.
3. Compactar o arquivo CSV em um arquivo denominado `Teste_{seu_nome}.zip`.
4. Substituir as abreviações das colunas **OD** e **AMB** pelas descrições completas, conforme a legenda no rodapé do PDF.

### **Execução**
- Linguagens suportadas: **Python** ou **Java**.
- Bibliotecas recomendadas:
  - Python: `PyPDF2`, `pandas`, `zipfile`.
  - Java: `Apache PDFBox`, `OpenCSV`.

---

## **3. Teste de Banco de Dados**

### **Descrição**
Este teste avalia a capacidade de manipulação de dados em banco de dados relacional.

### **Tarefas de Preparação**
1. Baixar os arquivos dos últimos 2 anos do repositório público:  
   [Demonstrativos Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/).
2. Baixar os dados cadastrais das operadoras ativas no formato CSV:  
   [Operadoras Ativas](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/).

### **Tarefas de Código**
1. Criar queries para estruturar tabelas necessárias para o arquivo CSV.
2. Elaborar queries para importar o conteúdo dos arquivos, garantindo o encoding correto.
3. Desenvolver uma query analítica para responder:
   - Quais as 10 operadoras com maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO-HOSPITALAR" no último trimestre?
   - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

### **Execução**
- Banco de dados suportados: **MySQL 8+** ou **PostgreSQL 10+**.
- Ferramentas recomendadas: MySQL Workbench, pgAdmin.

---

## **4. Teste de API**

### **Descrição**
Este teste consiste em desenvolver uma interface web que interaja com um servidor em Python para realizar buscas em dados previamente preparados.

### **Tarefas de Preparação**
1. Utilizar o CSV gerado no item **3.2** do Teste de Banco de Dados.

### **Tarefas de Código**
1. Criar um servidor em Python com uma rota que permita realizar buscas textuais na lista de cadastros de operadoras e retornar os registros mais relevantes.
2. Desenvolver uma interface web utilizando **Vue.js** para consumir a API.
3. Criar uma coleção no **Postman** para demonstrar os resultados.

### **Execução**
- Tecnologias suportadas:
  - Backend: **Python** (bibliotecas recomendadas: `Flask` ou `FastAPI`).
  - Frontend: **Vue.js**.
  - Ferramenta de teste: **Postman**.

---

## **Requisitos Gerais**

- **Confidencialidade**: Este documento e o código desenvolvido são confidenciais e não devem ser divulgados sem autorização expressa.
- **Organização do Repositório**:
  - `web_scraping/`: Código do Teste 1.
  - `transformacao_dados/`: Código do Teste 2.
  - `banco_dados/`: Scripts SQL do Teste 3.
  - `api/`: Código do Teste 4.

---

## **Como Executar**

### **Pré-requisitos**
- Python 3.8+ ou Java 11+.
- Banco de dados MySQL 8+ ou PostgreSQL 10+.
- Node.js 16+ para o frontend em Vue.js.

### **Passos**
1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```
2. Siga as instruções específicas de cada teste na respectiva pasta.

---

## **Contato**
Em caso de dúvidas, entre em contato com o responsável pelo teste.
