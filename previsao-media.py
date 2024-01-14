import pandas as pd

# Carregar os dados históricos
dados = pd.read_csv('resultados.csv', encoding='ISO-8859-1')

# Função para converter a string de números em uma lista de inteiros
def converter_numeros(numeros_str):
    numeros = numeros_str.split(", ")  # Dividir a string em números separados por vírgula e espaço
    return [int(numero) for numero in numeros]

# Aplicar a função para converter os números sorteados em uma lista de inteiros
dados['Dezenas'] = dados['Dezenas'].apply(converter_numeros)

# Calcular a média dos números sorteados em todos os concursos
media_numeros_sorteados = dados['Dezenas'].apply(lambda x: sum(x) / len(x))

# Fazer uma previsão para os próximos números com base na média
previsao = [int(round(media)) for media in media_numeros_sorteados]

print(previsao)
