sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros

print(f'O total do faturamento é:{total}')

percentual_sp = (sp/total) * 100
percentual_rj = (rj/total) * 100
percentual_mg = (mg/total) * 100
percentual_es = (es/total) * 100
percentual_outros = (outros/total) * 100
print(f'O percentual do faturamento de São Paulo é: {percentual_sp}')
print(f'O percentual do faturamento de Rio de Janeiro é: {percentual_rj}')
print(f'O percentual do faturamento de Minas Gerais é: {percentual_mg}')
print(f'O percentual do faturamento de Espirito Santo é: {percentual_es}')
print(f'O percentual do faturamento dos outros estados é: {percentual_outros}')
