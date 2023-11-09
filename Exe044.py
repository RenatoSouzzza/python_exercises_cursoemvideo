from time import sleep
print('\033[7;32;42m%\033[m' * 20)
print(f'\033[7;32;42m*LOJAS BONÉZINHO*\033[m')
print('\033[7;32;42m%\033[m' * 20)
price = float(input('Preço das Compras: R$ '))
print('Processando...')
sleep(1)
print('FORMAS DE PAGAMENTO \n[ 1 ] à vista dinheiro/PIX \n[ 2 ] à vista no cartão \n[ 3 ] 2X no cartão \n[ 4 ] 3X ou mais no cartão')
pay = int(input('Informe a opção: '))
print(f'Sua compra de R${price:.2f} vai custar', end=' ')
if pay == 1:
    print(f'R${price - (price * 10/100):.2f} com desconto de 10%')
elif pay == 2:
    print(f'R${price - (price * 5/100):.2f} com desconto de 5%')
elif pay == 3:
    print(f'R${price} em 2 parcelas de R${price / 2:.2f} SEM JUROS!')
elif pay == 4:
    total = price + (price *20/100)
    print(f'R${total} COM 20% DE JUROS! ')
    installment = int(input('Qtd de Parcelas: '))
    totalinstallment = total / installment
    print(f'Sua compra será parcelada em {installment}x de R${totalinstallment:.2f}')
print('\033[7;32;42m%\033[m' * 20)

