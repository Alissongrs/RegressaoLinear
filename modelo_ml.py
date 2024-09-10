import pandas as pd
import numpy as np

df = pd.read_csv('DadosTratados.csv')

df = df.drop(['cod_pedido', 'data'], axis=1)

#df = df.drop(df[(df['lucro_liquido'] == 0.0)].index)

#df.info()

#colunas_nao_numericas = df.select_dtypes(include=['object']).columns

#df_dumies = pd.get_dummies(df, columns=colunas_nao_numericas)

#print(df_dumies.head())

#print(df['valor_total_bruto'] > 0).head()

print(df['valor_total_bruto'])adad