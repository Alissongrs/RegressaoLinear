import pandas as pd
import numpy as np

df = pd.read_csv('DadosTratados.csv')

df = df.drop(['cod_pedido', 'data'], axis=1)

# Verificar se há valores nulos na coluna 'valor'
print(df['valor_comissao'].isnull().sum())
