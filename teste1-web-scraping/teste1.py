from download import baixar_pdf, obter_links_pdf
from arquivos import criar_pasta, criar_arquivo_zip
import os

def main():
    url_pagina = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    pasta_pdfs = "pdfs_baixados"
    nome_zip = "anexos_zipados.zip"
    
    criar_pasta(pasta_pdfs)

    pdfs_encontrados = obter_links_pdf(url_pagina)

    for pdf in pdfs_encontrados:
        baixar_pdf(pdf['url'], pdf['nome'], pasta_pdfs)

    criar_arquivo_zip(pasta_pdfs, nome_zip)

if __name__ == "__main__":
    main()