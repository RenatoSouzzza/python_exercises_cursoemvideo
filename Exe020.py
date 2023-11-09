from random import shuffle
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)
print('A ordem da apresentação será: {}'.format(ordem))