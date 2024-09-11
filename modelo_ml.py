import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('DadosTratados.csv')

df = df.drop(['cod_pedido', 'regiao_pais', 'produto', 'estado', 'formapagto', 'centro_distribuicao', 'responsavelpedido', 'categoriaprod'], axis=1)

df['data'] = pd.to_datetime(df['data'], dayfirst=True)
df['ano'] = df['data'].dt.year

X = df[['ano']]  # Usando apenas o ano para previsão
y = df['lucro_liquido']

# 4. Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Criar o modelo de regressão linear
model = LinearRegression()

# 6. Treinar o modelo
model.fit(X_train, y_train)

# 7. Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o modelo com Mean Squared Error (Erro Quadrático Médio)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# 8. Prever lucro líquido para os próximos 2 anos
anos_futuros = pd.DataFrame({'ano': np.arange(2024, 2029)})
lucro_futuro = model.predict(anos_futuros)

# Mostrar previsões para os anos futuros
previsao_futuro = pd.DataFrame({'ano': anos_futuros['ano'], 'lucro_liquido_previsto': lucro_futuro})
print(previsao_futuro)