lista_idade = list()
maioridade = 0
nomevelho = ''
mcont = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = input('Nome: ').upper().strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip() 
    lista_idade.append(idade)
    if c == 1 and sexo in 'M|m':
        maioridade = idade
        nomevelho = nome
    if sexo in 'M|m' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in "F|f" and idade < 20:
        mcont += 1
print(f'A média de idade do grupo é {sum(lista_idade)/4} anos')
print(f'O homem mais velho tem {maioridade} e se chama {nomevelho}')
print(f'Ao todo são {mcont} mulheres com menos de 20 anos')