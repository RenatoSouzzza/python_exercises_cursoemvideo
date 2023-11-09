# Crie uma um programa que leia o nome completo de uma pessoa e mostre:
# 1 O nome com todas as letras maiúsculas
# 2 O nome com todas as letras minúsculas
# 3 Quantas letras ao todo (sem considerar espaços)
# 4 Quantas letras tem o primeiro nome

'''nome = str(input('Digite o seu nome: '))
print('Analisando seu nome...')
print('O seu nome com letras maiúsculas fica {}', nome.upper()) # 1
print('O seu nome com letras minúsculas fica {}', nome.lower()) # 2
print('O seu nome sem os espaços vazios tem {} caractéres '.format(len(nome.replace(' ', ''))))
print(nome.split())
nome_lista = ['Renato', 'Silva', 'de', 'Souza']
print('O seu primeiro nome tem {} letras'.format(len(nome_lista[0])))'''

# Ou

nome = str(input('Digite o seu nome: ')).strip()
separa = nome.split()
print('Analisando o seu nome...')
print('O seu nome com letras minúscula fica {}'.format(nome.upper()))
print('O seu nome com letras minúsculas fica {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem ao todo {} letras'.format(nome.find(' '))) # O Find encontra o parâmetro informado que no caso é um espaço em branco
# então ele conta as células que ficaram pra trás

print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
