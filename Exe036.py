valor_imovel = float(input('Informe o valor do imóvel: R$ '))
salario = float(input('Informe o rendimento: R$ ')) * 30/100
anos = int(input('Informe em quantos anos quer pagar: ')) * 12
parcela = valor_imovel / anos
print('Valor do Imóvel: R${:.2f} \nParcela a ser paga (30% da renda): R${:.2f} \nQuandidade de prestações: {}'.format(valor_imovel, salario, anos))
if salario >= parcela:
    print('Empréstimo de {:.2f} APROVADO! O valor da parcela será de R${:.2f} a serem pagos em {} meses!'.format(valor_imovel, parcela, anos))
else:
    print('Empréstimo de {:.2f} REPROVADO! O valor da parcela excede os 30% da renda informada!'.format(valor_imovel))