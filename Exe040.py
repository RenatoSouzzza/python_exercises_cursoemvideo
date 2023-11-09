from time import sleep
nota1 = float(input('\033[1;33mPrimeira nota:\033[m'))
nota2 = float(input('\033[1;33mSegunda nota:\033[m'))
nota3 = float(input('\033[1;33mTerceira nota:\033[m'))
media = (nota1 + nota2 + nota3) / 3
print('Processando...')
sleep(1)
print('SUA MÉDIA: {:.1f}'.format(media))
if media >= 7.0:
    print('\033[1;32mPARABÉNS!!! Você foi APROVADO!\033[m')
elif media < 5.0:
    print('\033[1;31mREPROVADO! Te vejo no ano que vem!\033[m')
else:
    print('\033[1;33mRECUPERAÇÃO! Faça a prova substitutiva!\033[m')
