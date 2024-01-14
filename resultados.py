import requests
import csv

# Defina os valores de concursoInicio e concursoFim
concursoInicio = 1  # Substitua pelo número do concurso inicial desejado
concursoFim =  1 # Substitua pelo número do concurso final desejado
loteria = "LOTERIA"  # Especifique a loteria desejada EXEMPLO: megasena
token = "TOKEN"  # Substitua pelo seu token de acesso - Cadastre e consiga seu token em - https://apiloterias.com.br/

# Crie um arquivo CSV para salvar os resultados
with open('resultados.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Concurso', 'Data', 'Local Realizacao', 'Rateio Processamento', 'Acumulou', 'Valor Acumulado', 'Dezenas', 'Premiacao'])

    # Loop através dos concursos de concursoInicio até concursoFim
    for concurso in range(concursoInicio, concursoFim + 1):
        # URL da API de resultados das loterias
        url = f"https://apiloterias.com.br/app/resultado?loteria={loteria}&token={token}&concurso={concurso}"

        # Enviar uma solicitação HTTP para obter os resultados
        response = requests.get(url)

        # Verificar se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Parsear a resposta JSON
            resultado = response.json()

            print(f"Resultado para o concurso {concurso}: {resultado}")
            
            # Extrair informações relevantes do resultado
            numero_concurso = resultado.get('numero_concurso', '-')
            data_concurso = resultado.get('data_concurso', '-')
            local_realizacao = resultado.get('local_realizacao', '-')
            rateio_processamento = resultado.get('rateio_processamento', '-')
            acumulou = resultado.get('acumulou', '-')
            valor_acumulado = resultado.get('valor_acumulado', '-')
            dezenas = ', '.join(resultado.get('dezenas', []))
            premiacao = ', '.join([f"{item['nome']} ({item['quantidade_ganhadores']} ganhadores)" for item in resultado.get('premiacao', [])])

            # Escrever as informações no arquivo CSV
            csv_writer.writerow([numero_concurso, data_concurso, local_realizacao, rateio_processamento, acumulou, valor_acumulado, dezenas, premiacao])

        else:
            print(f"Não foi possível obter os resultados para o concurso {concurso} (Código de status: {response.status_code})")

print("Resultados salvos em 'resultados.csv'")
