s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i # acumulador
        c += 1 # contador
print(f'A soma de todos os {c} valores foi {s}')