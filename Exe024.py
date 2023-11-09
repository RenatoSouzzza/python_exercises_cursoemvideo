# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

cidade = str(input('Em qual cidade você nasceu? ')).strip()
print('santo' in cidade.casefold())

# Ou 

print(cidade[:5].upper() == 'SANTO')