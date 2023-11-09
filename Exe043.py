peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))

imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('Você está ABAIXO do Peso Ideal!')
elif imc <= 24.9:
    print('PARABÉNS, você está no peso IDEAL!')
elif imc <= 29.9:
    print('Você está LEVEMENTE acima do peso!')
elif imc <= 34.9:
    print('Você está em OBESIDADE MODERADA! Intensifique os exercícios físicos e equilibre a sua dieta!')
elif imc <= 39.9:
    print('Você está em OBESIDADE SEVERA! Intensifique os exercícios físicos e equilibre a sua dieta e faça exames de saúde!')
else:
    print('Você está em OBESIDADE MÓRBIDA! Consulte um médico!')


