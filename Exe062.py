print('='*40)
print('Gerador de PA com estrutura While')
print('='*40)


primeiro, razao = int(input('Primeiro Termo: ')), int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
add = 10
while add != 0:
    total += add
    while cont <= total:
        print(f' {termo}', end=' ➝ ') 
        termo += razao
        cont += 1
    print(' Pausa')
    add = int(input('Quantos termos a mais deseja mostrar? '))
print(f'Progressão finalizada com {total} termos exibidos!')






