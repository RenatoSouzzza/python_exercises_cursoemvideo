preco = float(input('Informe o preço do produto R$ '))
desc = preco * 5 / 100 
print('O preço do produto R${:.2f} com desconto de 5% será R$ {:.2f}'.format(preco, preco - desc))

# Ou

desc = preco - (preco * 5 / 100)
print('O preço do produto R${:.2f} com desconto de 5% será R$ {:.2f}'.format(preco, desc))

# Com opção de mudar o desconto:

preco = float(input('Informe o preço do produto R$ '))
percdesc = float(input('Informe o desconto concedido: '))
desc = preco - (preco * percdesc / 100)
print('O preço do produto R${:.2f} com desconto de {:.2f}% será R$ {:.2f}'.format(preco, percdesc, desc))