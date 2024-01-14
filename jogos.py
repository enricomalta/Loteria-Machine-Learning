import chardet

def detectar_codificacao_arquivo(arquivo):
    detector = chardet.universaldetector.UniversalDetector()
    for linha in arquivo:
        detector.feed(linha)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']

def extrair_numeros_de_string(texto):
    numeros = []
    numero_atual = ""
    for caractere in texto:
        if caractere.isdigit() or caractere == '-':
            numero_atual += caractere
        elif numero_atual:
            numeros.append(int(numero_atual))
            numero_atual = ""
    if numero_atual:
        numeros.append(int(numero_atual))
    return numeros

def ajustar_tamanho_sequencia(seq_numeros, tamanho_jogo):
    resto = len(seq_numeros) % tamanho_jogo
    if resto != 0:
        # Preencher com zeros à direita para ajustar o tamanho
        seq_numeros += [0] * (tamanho_jogo - resto)
    return seq_numeros

def dividir_em_jogos(seq_numeros, tamanho_jogo):
    jogos = [seq_numeros[i:i + tamanho_jogo] for i in range(0, len(seq_numeros), tamanho_jogo)]  # noqa: E501

    jogos_nomeados = {"jogo" + str(i + 1): jogo for i, jogo in enumerate(jogos)}

    return jogos_nomeados

# Abra o arquivo sequencianumeros.txt e leia os números com a codificação detectada
with open("sequencianumeros.txt", "rb") as arquivo:
    codificacao = detectar_codificacao_arquivo(arquivo)

with open("sequencianumeros.txt", "r", encoding=codificacao) as arquivo:
    conteudo = arquivo.read()
    sequencia_numeros = extrair_numeros_de_string(conteudo)

# Tamanho de cada jogo
tamanho_jogo = 6

# Ajustar o tamanho da sequência para ser múltiplo do tamanho do jogo
sequencia_numeros = ajustar_tamanho_sequencia(sequencia_numeros, tamanho_jogo)

# Dividir a sequência em jogos e nomear
jogos_divididos = dividir_em_jogos(sequencia_numeros, tamanho_jogo)

# Imprimir os jogos
for nome, jogo in jogos_divididos.items():
    print(f"{nome}: {', '.join(map(str, jogo))}")
