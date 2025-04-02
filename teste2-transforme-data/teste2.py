from leitor_de_pdf import ler_pdf
from pathlib import Path 
from transformar_dados import salvar_csv, criar_zip  # Importação corrigida

def main():
    caminho_pdf = "pdfs_baixados\\Anexo_I.pdf"

    Path("csvs").mkdir(exist_ok=True)
    Path("zipFiles").mkdir(exist_ok=True)

    caminho_csv = Path("csvs") / "rol_procedimentos_em_saude.csv"
    caminho_zip = Path("zipFiles") / "teste_joao_pedro_camargo_pinheiro.zip"

    tabelas_pdf = ler_pdf(caminho_pdf)

    salvar_csv(tabelas_pdf, caminho_csv)

    criar_zip(caminho_csv, caminho_zip)

    print(f"O arquivo CSV foi salvo em {caminho_csv} e compactado em {caminho_zip}")

if __name__ == "__main__":
    main()
