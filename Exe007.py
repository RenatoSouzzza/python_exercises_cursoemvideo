nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
nota3 = float(input('Terceira nota do aluno: '))
nota4 = float(input('Quarta nota do aluno: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 6.0:
    print('A média entre as notas informadas é {}'.format(media))
    print('Parabéns, você foi aprovado (a, e)!!!')
elif media >= 5.0:
    print('A média entre as notas informadas é {}'.format(media))
    print('Você está na recuperação. Aguarde a prova substitutiva')
else:
    print('A média entre as notas informadas é {}'.format(media))
    print('Você foi reprovado (a, e)')