total = list()
for c in range(1, 7):
    number = int(input(f'Digite o {c}º número: '))
    if number % 2 == 0:
        total.append(number)
print(f'Lista de números informados: {total} \nA soma dos números pares inseridos na lista é {sum(total)}')
