import os
import requests
from datetime import datetime

# Diretórios dos dados
DATA_DIR = "../data"
RAW_DIR = os.path.join(DATA_DIR, "raw")
LAST_UPDATE_FILE = os.path.join(DATA_DIR, "last_update.txt")

# URLs das fontes de dados
DATA_SOURCES = {
    "tesouro_direto": "https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv",
    "selic": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=csv",
    "ipca": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv"
}


# Criar diretórios se não existirem
os.makedirs(RAW_DIR, exist_ok=True)

def get_last_update_date():
    """Lê a data da última atualização salva no arquivo last_update.txt"""
    if os.path.exists(LAST_UPDATE_FILE):
        with open(LAST_UPDATE_FILE, "r") as f:
            return f.read().strip()
    return None

def update_last_update_date():
    """Atualiza o arquivo last_update.txt com a data de hoje"""
    today = datetime.today().strftime("%Y-%m-%d")
    with open(LAST_UPDATE_FILE, "w") as f:
        f.write(today)

def download_file(url, filename):
    """Baixa um arquivo e salva no diretório raw/"""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(RAW_DIR, filename), "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"✅ Download concluído: {filename}")
    else:
        print(f"❌ Erro ao baixar {filename}: {response.status_code}")

def download_data():
    """Verifica se os dados já foram baixados hoje, senão, baixa novamente"""
    last_update = get_last_update_date()
    today = datetime.today().strftime("%Y-%m-%d")

    if last_update == today:
        print("📌 Dados já atualizados hoje. Nenhum download necessário.")
        return

    print("🔄 Baixando novos dados...")

    for key, url in DATA_SOURCES.items():
        filename = f"{key}.csv"
        download_file(url, filename)

    # Atualizar a data da última atualização
    update_last_update_date()
    print("✅ Atualização concluída.")

if __name__ == "__main__":
    download_data()
