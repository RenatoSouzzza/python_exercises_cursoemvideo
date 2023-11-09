import math
ang = float(input('Digite o ângulo que deseja: '))
sen = math.sin(math.radians(ang))
print('O ângulo de {:.0f} tem o SENO de {:.2f}'.format(ang, sen))
coss = math.cos(math.radians(ang))
print('O ângulo de {:.0f} tem o COSSENO de {:.2f}'.format(ang, coss))
tang = math.tan(math.radians(ang))
print('O ângulo de {:.0f} tem a TANGENTE de {:.2f}'.format(ang, tang))