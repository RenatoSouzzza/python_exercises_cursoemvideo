print('='*40)
print('10 TERMOS DE UMA PA(Progressão Aritmética)')
print('='*40)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao
print(decimo)
for c in range(termo, decimo + razao, razao):
    print(f' {c} ', end='➝ ')
print(' Acabou')