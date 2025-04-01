import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def baixar_pdf(url, nome_arquivo, pasta_destino):
    nome_arquivo = nome_arquivo.rstrip(".")

    download_pdf = requests.get(url)

    if download_pdf.status_code == 200:
        with open(f"{pasta_destino}/{nome_arquivo}.pdf", "wb") as arquivo_pdf:
            arquivo_pdf.write(download_pdf.content)
        print(f"Download concluído: {nome_arquivo}")
        return True
    else:
        print(f"Erro ao baixar: {url}")
        print(f"Código de status: {download_pdf.status_code}")
        return False

def obter_links_pdf(url_pagina):
    pagina_response = requests.get(url_pagina)
    pagina_html = BeautifulSoup(pagina_response.text, "html.parser")
    lista_de_links = pagina_html.find_all('a')
    
    urls_processadas = set()
    pdfs_encontrados = []
    
    for link in lista_de_links:
        texto_link = link.get_text()
        url_arquivo = link.get('href')
        
        if url_arquivo:
            url_arquivo = urljoin(url_pagina, url_arquivo)
            
            if ('Anexo I' in texto_link or 'Anexo II' in texto_link) and url_arquivo.endswith('.pdf') and url_arquivo not in urls_processadas:
                print(f"Encontrado: {texto_link}")
                print(f"Link: {url_arquivo}")
                
                nome_arquivo = texto_link.strip().replace(" ", "_")
                pdfs_encontrados.append({
                    'url': url_arquivo,
                    'nome': nome_arquivo
                })
                urls_processadas.add(url_arquivo)
                print("---")
    
    return pdfs_encontrados