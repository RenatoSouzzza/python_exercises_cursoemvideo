salario = float(input('Qual o salário do Funcionário? R$ '))
reajuste = float(input('Qual será o percentual de reajuste concedido? '))
novo_salario = salario + (salario * reajuste/100)
print('Salário atual do funcionário: R$ {:.2f} \nReajuste concedido: {:.2f}% \nSalário reajustado para a próxima folha: R$ {:.2f}'.format(salario, reajuste, novo_salario))