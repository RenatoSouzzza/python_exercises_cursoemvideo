lista = list()
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    lista.append(peso)
print(f'O maior peso lido foi de {max(lista)}kg')
print(f'O menor peso lido foi de {min(lista)}kg')
