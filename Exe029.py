from colorama import Fore, Back, Style
v = float(input('Qual a velocidade do veículo? '))
exced = v - 80
if v <= 80:
    print(Back.GREEN + Fore.BLACK + 'Tenha um bom dia, Dirija com segurança! ')
else:
    print(Fore.RED + 'MULTADO! Você excedeu o limite pemitido que é de 80Km/h')
    print(Style.BRIGHT + Fore.CYAN + 'Você deve pagar uma multa de R${:.2f}'.format(exced * 7,00))
print(Style.RESET_ALL)
print('Não corra, não mate, não morra! ')