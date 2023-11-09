#jokenpo
from time import sleep
from random import random, randint
print('''Suas Ações:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
play = int(input('Qual é a sua jogada? '))
# comp = round(random.random(0,1,2))
comp = randint(0, 3)
sleep (1)
print('JO')
sleep (1)
print('KEN')
sleep (1)
print('PO!!!')
print('-=' * 20)
if comp == 0:
    print('Computador jogou PEDRA', end=' ') 
    if play == 0:
        print('\nJogador jogou PEDRA')
        print('EMPATE!')
    elif play == 1:
        print('\nJogador jogou PAPEL')  
        print('JOGADOR VENCE!')
    else:
        print('\nJogador jogou TESOURA')
        print('COMPUTADOR VENCE!')
if comp == 1:
    print('Computador jogou PAPEL', end=' ')
    if play == 0:
        print('\nJogador jogou PEDRA  \nCOMPUTADOR VENCE! ')
    elif play == 1:
        print('\nJogador jogou PAPEL \nEMPATE!')
    else:
        print('\nJogador jogou TESOURA \nJOGADOR VENCE!')
if comp == 2:
    print('Computador jogou TESOURA', end=' ')
    if play == 0:
        print('\nJogador jogou PEDRA  \nJOGADOR VENCE! ')
    elif play == 1:
        print('\nJogador jogou PAPEL \nCOMPUTADOR VENCE!')
    else:
        print('\nJogador jogou TESOURA \nEMPATE!')
print('-=' * 20)

#Solução Guanabara

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Suas Ações:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
play = int(input('Qual é a sua jogada? '))
print('-='*11)
print(f'O Computador jogou {itens[comp]}')
print(f'O Jogador jogou {itens[play]}')
print('-='*11)
if comp == 0:
    if play == 0:
        print('Empate!')
    elif play == 1:
        print('Jogador Vence!')
    elif play == 2:
        print('Computador Vence!')
    else:
        print('Jogada inválida!')
elif comp ==1:
    if play == 0:
        print('Computador Vence!')
    elif play == 1:
        print('Empate!')
    elif play == 2:
        print('Jogador Vence!')
    else:
        print('Jogada inválida!')
elif comp == 2:
    if play == 0:
        print('Jogador Vence!')
    elif play == 1:
        print('Computador Vence!')
    elif play == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
print('-='*11)


