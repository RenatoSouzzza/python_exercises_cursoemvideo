frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
frase_contra = frase[::-1]
print(f'O inverso de {frase} é {frase_contra}')
if frase == frase_contra:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')

# Solução com FOR
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')