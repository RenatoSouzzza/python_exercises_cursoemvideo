from datetime import date
year_birth = int(input('Ano de Nascimento do Atleta: '))
idade = date.today().year - year_birth
if idade <= 9:
    print(f'O atleta tem {idade} anos \nClassificação: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos \nClassificação: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos \nClassificação: JUNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos \nClassificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos \nClassificação: MASTER')
