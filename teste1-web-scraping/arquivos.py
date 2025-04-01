import os
import zipfile

def criar_pasta(pasta):
    os.makedirs(pasta, exist_ok=True)

def criar_arquivo_zip(pasta_pdfs, nome_zip):
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in os.listdir(pasta_pdfs):
            if arquivo.endswith('.pdf'):
                caminho_completo = os.path.join(pasta_pdfs, arquivo)
                zipf.write(caminho_completo, arquivo)
                print(f"Adicionado ao ZIP: {arquivo}")