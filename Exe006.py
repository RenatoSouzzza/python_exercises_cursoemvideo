from math import sqrt
num = int(input('Digite um número: '))
print('Analisando o número...')
print('O dobro de {} vale {}'.format(num, num * 2))
print('O triplo de {} vale {}'.format(num, num * 3))
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, num**(1/2)))
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, sqrt(num))) # com função sqrt da biblioteca math