sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Digite o sexo novamente utilizando as letras M e F: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
    
