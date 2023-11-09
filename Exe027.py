nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Muito prazer em te conhecer! ')
print('Seu primeiro nome é {} '.format(lista[0]))
print('Seu último nome é {} '.format(lista[-1]))
# Ou
print('Seu útimo nome é {}'.format(lista[len(lista)-1]))