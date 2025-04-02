import pandas as pd
import zipfile
from pathlib import Path

descricao_abreviacoes = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial'
}

def substituir_abreviacoes(df):
    if 'OD' in df.columns:
        df['OD'] = df['OD'].replace(descricao_abreviacoes)
    if 'AMB' in df.columns:
        df['AMB'] = df['AMB'].replace(descricao_abreviacoes)
    return df

def salvar_csv(tabela_pdf, caminho_csv):
    if tabela_pdf:
        df_final = pd.concat(tabela_pdf, ignore_index=True)

        df_final = substituir_abreviacoes(df_final)

        df_final.to_csv(caminho_csv, index=False, encoding='utf-8')
    
def criar_zip(caminho_csv, caminho_zip):
    """Compacta o CSV em um arquivo ZIP."""
    with zipfile.ZipFile(caminho_zip, 'w') as zipf:
        zipf.write(caminho_csv, caminho_csv.name)