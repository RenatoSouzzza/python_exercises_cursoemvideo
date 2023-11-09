import emoji
print(emoji.emojize('Olá! Bem vindo á Manjolos Car:carro:', language='pt'))
aluguel = int(input('Quantos dias alugados? '))
kilometragem = float(input('Quantos Km rodados? '))
diaria = float(input('Informe o preço acordado pela diária: R$ '))
kmrodado = float(input('Informe o preço da kilometragem acordada: R$ '))
print('Total preço aluguel: R$ {:.2f}'.format(aluguel * diaria))
print('Total preço da Kilometragem rodada: R${:.2f}'.format(kilometragem * kmrodado))
print('Total a pagar: R$ {:.2f}'.format((aluguel * diaria) + (kilometragem * kmrodado)))