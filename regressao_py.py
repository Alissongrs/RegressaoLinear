import pandas as pd
import numpy as np
url = 'vendas_linha_petshop_2020_2024.csv'
dados = pd.read_csv(url, sep=';', encoding='latin1')

# Limpeza e preparação da coluna 'valor'
dados['valor'] = (
    dados['valor']
    .str.replace('[^0-9,]', '', regex=True)  # Remove caracteres não numéricos e não vírgulas
    .str.replace(',', '.')  # Substitui vírgulas por pontos
)

# Converter a coluna 'valor' para float
dados['valor'] = pd.to_numeric(dados['valor'], errors='coerce')  # Converte para numérico e trata valores inválidos como NaN
dados['valor'] = dados['valor'].fillna(0)  # Preenche NaNs com 0

# Repetir o mesmo processo para outras colunas monetárias
dados['valor_total_bruto'] = (
    dados['valor_total_bruto']
    .str.replace('[^0-9,]', '', regex=True)
    .str.replace(',', '.')
)
dados['valor_total_bruto'] = pd.to_numeric(dados['valor_total_bruto'], errors='coerce')
dados['valor_total_bruto'] = dados['valor_total_bruto'].fillna(0)

dados['valor_comissao'] = (
    dados['valor_comissao']
    .str.replace('[^0-9,]', '', regex=True)
    .str.replace(',', '.')
)
dados['valor_comissao'] = pd.to_numeric(dados['valor_comissao'], errors='coerce')
dados['valor_comissao'] = dados['valor_comissao'].fillna(0)

dados['lucro_liquido'] = (
    dados['lucro_liquido']
    .str.replace('[^0-9,]', '', regex=True)
    .str.replace(',', '.')
)
dados['lucro_liquido'] = pd.to_numeric(dados['lucro_liquido'], errors='coerce')
dados['lucro_liquido'] = dados['lucro_liquido'].fillna(0)

# Para a coluna 'quantidade', garantir que seja numérico e inteiro
dados['quantidade'] = pd.to_numeric(dados['quantidade'], errors='coerce')  # Converte para numérico, tratando valores inválidos como NaN
dados['quantidade'] = dados['quantidade'].fillna(0).astype(int)  # Preenche NaNs com 0 e converte para inteiro

# Verificar se ainda há NaNs
print(dados.isnull().sum())

# Mostrar as primeiras linhas para verificação
print(dados.tail())

print(dados)
dados.to_csv('DadosTratados.csv', index=False)