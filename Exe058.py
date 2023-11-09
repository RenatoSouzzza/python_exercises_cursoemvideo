from random import randint
print('Sou seu Computador! \nPensei em um número de 0 a 10 \nConsegue adivinhar qual foi?')
tentativas = 1
comp = randint(0, 10)
n = int(input('Qual o seu palpite? '))
while n != comp:
    if n <= comp:
        n = int(input('Mais... Tente novamente! '))
        tentativas += 1
    elif n >= comp:
        n = int(input('Menos... Tente novamente! '))
        tentativas += 1
print(f'Você acertou com {tentativas} tentativas. O número em que pensei foi {comp}')           
