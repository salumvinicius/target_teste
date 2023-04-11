palavra = input('Insira a palavra: ')
palavra_lista = list(palavra)
palavra_reverse = []
for a in reversed(palavra_lista):
    a = palavra_reverse.append(a)

palavra_reverse = ''.join(palavra_reverse)

print(f'Palavra original: {palavra}')
print(f'Palavra ao contrario: {palavra_reverse}')