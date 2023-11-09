import random
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
sorteio = [ aluno1, aluno2, aluno3, aluno4 ]

print('O Aluno escolhido foi {}! '.format(random.choice(sorteio)))