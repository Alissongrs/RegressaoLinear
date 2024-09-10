import pandas as pd
import numpy as np
url = 'vendas_linha_petshop_2020_2024.csv'
dados = pd.read_csv(url, sep=';', encoding='latin1')

dados['valor'] = dados['valor'].str.replace('R$', '', regex=False).replace(',', '.', regex=False)
dados['valor_total_bruto'] = dados['valor_total_bruto'].str.replace('R$', '', regex=False).replace(',', '.', regex=False)
dados['valor_comissao'] = dados['valor_comissao'].str.replace('R$', '', regex=False).replace(',', '.', regex=False)
dados['lucro_liquido'] = dados['lucro_liquido'].str.replace('R$', '', regex=False).replace(',', '.', regex=False)

#dados['valor'] = pd.to_numeric(dados['valor'], errors= 'coerce')
dados['valor_total_bruto'] = pd.to_numeric(dados['valor_total_bruto'], errors= 'coerce')
dados['valor_comissao'] = pd.to_numeric(dados['valor_comissao'], errors='coerce')
dados['lucro_liquido'] = pd.to_numeric(dados['lucro_liquido'], errors='coerce')
dados['quantidade'] = pd.to_numeric(dados['quantidade'], errors='coerce')

dados.info()

dados['quantidade'] = dados['quantidade'].fillna(0)
dados['quantidade'] = dados['quantidade'].dropna()
dados['quantidade'].isnull().sum()
dados['quantidade'] = dados['quantidade'].astype(int)

dados['valor_total_bruto'] = dados['valor_total_bruto'].fillna(0)
dados['valor'] = dados['valor'].fillna(0)
dados['valor_comissao'] = dados['valor_comissao'].fillna(0)
dados['lucro_liquido'] = dados['lucro_liquido'].fillna(0)

dados.to_csv('DadosTratados.csv', index=False)