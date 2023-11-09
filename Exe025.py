# Crie um programa que leia o nome de uma pessoal e diga se ela tem 'Silva' no nome

nome = str(input('Diga o seu nome completo ')).strip()
listado = (nome.split())
print('Seu nome tem Silva? {}'.format('Silva' in listado)) # aqui não é possível diferenciar maiusculas e minusculas pois as funçoes 'lower'
# ou 'casefold' não se aplicam a listas
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) # aqui podemos inserir maiusculas e minusculas pois o objeto é uma string