from datetime import date
ano = int(input('\033[1;32mQual ano quer analisar? Coloque 0 para analisar o ano atual: \033[m '))
print('\033[4;31;47mAnalisando...\033[m')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))
