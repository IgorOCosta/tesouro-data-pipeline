# 📊 Tesouro Data Pipeline

**Tesouro Data Pipeline** é um projeto de **engenharia de dados** que coleta, transforma e analisa dados históricos do **Tesouro Direto**, **IPCA** e **Selic** para gerar insights sobre os rendimentos reais das aplicações financeiras.

O pipeline ETL utiliza **Python, Pandas, Docker e MongoDB** para extrair dados, armazená-los como documentos NoSQL e gerar análises visuais interativas.

## 📌 Índice
- [📊 Tesouro Data Pipeline](#-tesouro-data-pipeline)
- [📂 Estrutura do Banco de Dados](#-estrutura-do-banco-de-dados)
- [🚀 Objetivos](#-objetivos)
- [🛠 Tech Stack](#-tech-stack)
- [🔥 Habilidades Trabalhadas](#-habilidades-trabalhadas)
- [🖥 Como Rodar](#-como-rodar)

## 📂 Estrutura do Banco de Dados

No MongoDB, cada **tipo de título** será salvo como um documento separado na coleção **tesouro_direto**:

```json
{
  "titulo": "Tesouro IPCA+ 2029",
  "historico": [
    {"data": "2024-01-01", "preco": 1000, "taxa": 6.0},
    {"data": "2024-02-01", "preco": 1015, "taxa": 5.8}
  ]
}
```
Cada título conterá um histórico detalhado, permitindo análises sobre diferentes indexadores.

## 🚀 Objetivos
✔ Coletar e armazenar dados do **Tesouro Direto**, **IPCA** e **Selic**  
✔ Criar colunas derivadas para calcular o **crescimento real da aplicação**  
✔ Comparar diferentes indexadores e simular o rendimento real dos investimentos  
✔ Usar **MongoDB** para armazenar os títulos em documentos separados  
✔ Orquestrar tudo com **Docker**  
✔ Gerar gráficos e relatórios automatizados para análise  

## 🛠 Tech Stack
- **Linguagem:** Python  
- **Bibliotecas:** Pandas, Requests, Matplotlib, Seaborn  
- **Banco de Dados:** MongoDB (NoSQL)  
- **Orquestração:** Docker  
- **Ferramentas:** Jupyter Notebook, GitHub  

## 🔥 Habilidades Trabalhadas
✅ **Data Engineering:** ETL, armazenamento em banco NoSQL  
✅ **Data Analysis:** Exploração e transformação de dados  
✅ **Docker & Containers:** Isolamento e escalabilidade  
✅ **MongoDB:** Modelagem de documentos para análise financeira  
✅ **Python & Pandas:** Manipulação e processamento eficiente  

## 🖥 Como Rodar
### 🔹 Pré-requisitos
Certifique-se de ter instalados:
- **Docker** e **Docker Compose**
- **Python 3.8+**
- **MongoDB**

### 🔹 Passo a Passo
1. Clone o repositório:
   ```bash
   git clone https://github.com/IgorOCosta/tesouro-data-pipeline.git
   cd tesouro-data-pipeline
   ```

2. Inicie os containers Docker:
   ```bash
   docker-compose up -d
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o pipeline ETL:
   ```bash
   python src/main.py
   ```

5. Acesse o MongoDB para verificar os dados inseridos:
   ```bash
   docker exec -it mongodb-container mongo
   ```

6. Para visualizar os gráficos, abra o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

Agora é só explorar os insights gerados pelo projeto! 🚀

