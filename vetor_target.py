import json
with open('dados.json','r') as f:
    dados = json.load(f)

maior_faturamento = max(dia['valor'] for dia in dados)

dias_com_faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

menor_faturamento = min(dias_com_faturamento)

dias_acima_media = len([dia for dia in dados if dia['valor'] > media_mensal])


print(f'O dia com menor faturamento no mes foi:{menor_faturamento}')
print(f'O dia com maior faturamento no mes foi:{maior_faturamento}')
print(f'O numero de dias em que o faturamento foi acima da media é:{dias_acima_media}')