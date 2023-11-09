num1 = int(input('\033[4;31mPrimeiro valor:\033[m'))
num2 = int(input('\033[4;32mSegundo valor:\033[m'))
num3 = int(input('\033[4;33mTerceiro valor:\033[m'))
print('Utilizando lista: ')
lista = [num1, num2, num3]
print('O menor valor digitado foi {}'.format(min(lista)))
print('O maior valor digitado foi {}'.format(max(lista)))
print('Utilizando if/else:')
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('Neste caso o menor valor digitado é {}'.format(menor))
print('Neste caso o maior valor digitado é {}'.format(maior))
