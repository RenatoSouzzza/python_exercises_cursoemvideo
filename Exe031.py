from time import sleep
print('\033[1;32mBem vindo á Jalala Viagens e Turismo!\033[m')
distancia = float(input('Qual a distância da sua viagem? '))
print('Processando...')
sleep(1)
if distancia >= 200:
    print('Iniciando sua viagem de {:.1f}Km.'.format(distancia))
    print('O preço da sua passagem será R${:.2f}'.format(distancia * 0.45))
else:
    print('Iniciando sua viagem de {:.1f}Km.'.format(distancia))
    print('O preço da sua passagem será R${:.2f}'.format(distancia * 0.50))
print('\033[1;32mAperte os cintos, e Boa Viagem!\033[m')