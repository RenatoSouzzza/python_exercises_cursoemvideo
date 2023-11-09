from time import sleep
first = int(input('Primeiro Valor: '))
second = int(input('Segundo Valor: '))
option = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa 
>>> Qual sua Opção? '''))
sleep(1)
while option != 5:
    if option == 1:
        print('Processando...')
        sleep(2)
        print(f'A soma entre {first} e {second} é {(first + second)}')
        print('-==' * 15)
    elif option == 2:
        print('Processando...')
        sleep(2)
        print(f'A multiplicação entre {first} e {second} é {(first * second)}')
        print('-==' * 15)
    elif option == 3:
        print('Processando...')
        sleep(2)
        print(f'Entre os números {first} e {second} o maior dígito é {max(first, second)}')
        print('-==' * 15)
    elif option == 4:
        print('Processando...')
        sleep(2)
        print('Informe novamente os valores! ')
        print('-==' * 15)
        sleep(2)
        first = int(input('Primeiro Valor: '))
        second = int(input('Segundo Valor: '))
    else:
        print('Opção inválida. Tente novamente de 1 a 5: ')
        print('-==' * 15)
    print('Reiniciando...')
    print('-==' * 15)
    sleep(1) 
    option = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa 
>>> Qual sua Opção? '''))
print('Finalizando...')
print('-==' * 15)
sleep(1)
print('Fim do Programa!')