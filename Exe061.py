print('='*40)
print('Gerador de PA com estrutura While')
print('='*40)


termo, razao = int(input('Primeiro Termo: ')), int(input('Razão: '))
decimo = termo + (10-1) * razao

while termo <= decimo:
    print(f' {termo}', end=' ➝ ') 
    termo += razao
print(' Acabou')
