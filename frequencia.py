from collections import Counter
import re

# Abra o arquivo sequenciajogos.txt e leia as sequências
with open("sequenciajogos.txt", "r") as arquivo:
    linhas = arquivo.readlines()

# Função para limpar e converter uma string em números inteiros
def limpar_e_converter_numeros(texto):
    numeros = re.findall(r'\d+', texto)
    numeros = [int(num) for num in numeros]
    return numeros

# Crie um dicionário para rastrear a frequência de cada número
frequencia_numeros = Counter()

# Processar cada linha e contar a frequência dos números
for linha in linhas:
    partes = linha.strip().split(":")
    if len(partes) == 2:
        numeros = limpar_e_converter_numeros(partes[1])
        frequencia_numeros.update(numeros)

# Encontrar os números mais frequentes (por exemplo, os 6 mais frequentes)
numeros_mais_frequentes = frequencia_numeros.most_common(6)

# Imprimir os números mais frequentes
print("Números mais frequentes:")
for numero, frequencia in numeros_mais_frequentes:
    print(f"Número: {numero}, Frequência: {frequencia}")
