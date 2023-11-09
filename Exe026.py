frase = str(input('Digite uma frase: ').upper().strip())
print('A letra R aparece {} vezes na frase'.format(frase.count('R')))
print('A primeira Letra R apareceu na posição {}'.format(frase.find('R')+1))
print('A útima letra R apareceu na posição {}'.format(frase.rfind('R')+1))