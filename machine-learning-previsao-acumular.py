import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Carregando o arquivo CSV
dados = pd.read_csv("resultados.csv")

# Exemplo: Suponhamos que a coluna 'Dezenas' contém os números sorteados e 'Acumulou' indica se houve um ganhador (1) ou não (0).

# Separando as características (features) dos rótulos (labels)
X = dados['Dezenas']  # Características
y = dados['Acumulou']  # Rótulos

# Dividindo os dados em conjunto de treinamento e conjunto de teste
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Convertendo a coluna 'Dezenas' em listas de números
X_treinamento = X_treinamento.str.split(',').apply(lambda x: [int(num) for num in x])
X_teste = X_teste.str.split(',').apply(lambda x: [int(num) for num in x])

# Criando e treinando o modelo de regressão logística
modelo = LogisticRegression()
modelo.fit(X_treinamento.tolist(), y_treinamento)

# Fazendo previsões no conjunto de teste
previsoes = modelo.predict(X_teste.tolist())

# Avaliando a precisão do modelo
precisao = accuracy_score(y_teste, previsoes)
print(f"Precisão do modelo: {precisao * 100:.2f}%")


#  A precisão está relacionada à tarefa de classificar se um sorteio resultará em acumulação ou não, e não à previsão
# exata dos números sorteados. A precisão é uma métrica de quão bem o modelo está fazendo em sua
# tarefa específica de classificação, não uma garantia de prever os números sorteados com precisão.
