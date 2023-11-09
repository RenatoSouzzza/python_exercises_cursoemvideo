print('\033[4;35m=+\033[m' * 20)
print('\033[4;35mAnalisador de Triângulos\033[m')
print('\033[4;35m=+\033[m' * 20)
a1 = float(input('Primeiro Segmento: '))
a2 = float(input('Segundo Segmento: '))
a3 = float(input('Terceiro Segmento: '))
if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
    print('Os segmentos acima PODEM formar um triângulo! ')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo! ')
print('\033[4;35m=+\033[m' * 20)