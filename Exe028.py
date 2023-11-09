'''print('Estou pensando em um número de 0 á 5...')
n = int(input('Em qual número estou pensando? '))
if n == 4:
    print('Parabéns, você acertou! ')
else:
    print('Errroouuuuu! ')'''

import random
from time import sleep

#numero_aleatorio = round(random.random() * 10)
# ou 
# numero_aleatorio = randint(0, 10)
print('Estou pensando num número de 0 á 10... ')
number = int(input('Em qual número estou pensando? '))
print('Processando...')
sleep(2)
if number == numero_aleatorio:
    print('Parabéns, você acertou! O número escolhido foi {}'.format(numero_aleatorio))
else:
    print('Que pena, o número escolhido foi o {}'.format(numero_aleatorio))
