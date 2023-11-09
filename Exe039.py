from datetime import date 
ano = int(input('\033[4;31mAno de Nascimento:\033[m '))
idade = date.today().year - ano
idadealista = ano + 18
print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}...')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento militar.')
    print(f'Seu alistamento será em {idadealista}')
elif idade == 18:
    print('Você deverá se alistar IMEDIATAMENTE!')
else:
    print(f'Você deveria ter se alistado há {date.today().year - idadealista} anos... \nSeu alistamento foi em {idadealista}')