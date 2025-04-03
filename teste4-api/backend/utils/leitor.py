import csv
from pathlib import Path

def buscar_csv(arquivo_csv: Path, nome_busca: str) -> list[dict]:

    resultados = []

    with arquivo_csv.open(mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        for linha in leitor:
            nome_operadora = linha["Nome_Fantasia"].strip().lower()
            if nome_busca in nome_operadora:
                resultados.append(linha)

    return resultados

def buscar_csv_cnpj(arquivo_csv: Path, cnpj: str) -> dict | None:
    with arquivo_csv.open(mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")
        for linha in leitor:
            if linha["CNPJ"] == cnpj:
                return linha  
    return None