from tabula.io import read_pdf

def ler_pdf(caminho_pdf):
    tabelas = read_pdf(caminho_pdf, pages='all', multiple_tables=True)
    return tabelas
