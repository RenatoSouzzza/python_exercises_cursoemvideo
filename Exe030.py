num = int(input('\033[4;35mMe diga um número qualquer: \033[m'))
if num % 2 == 0:
    print('O número é \033[1;32;40mPAR!\033[m')
else:
    print('O número é \033[1;31;40mÍMPAR!\033[m')

# ou
num = int(input('\033[7;35;44mMe diga um número qualquer: \033[m'))
resultado = num % 2
if resultado == 0:
    print('O número {} é \033[1;32;40mPAR!\033[m'.format(num))
else:
    print('O número {} é \033[1;31;40mIMPAR!\033[m'.format(num))