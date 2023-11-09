from time import sleep
print('-=' * 20)
wage = float(input('Qual é o salário para cálculo de aumento? R$ '))
print('-=' * 20)
print('\033[4;32mCalculando...\033[m')
sleep(1)
if wage > 1250:
    wage_increase = wage + (wage * 10/100)
else:
    wage_increase = wage + (wage * 15/100)
print('O salário que era R$ {:.2f} passará a ser R$ {:.2f}'.format(wage, wage_increase))

