#from math import hypot
catopo = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
hip = (catopo ** 2 + catadj ** 2)  ** (1/2)
# print('A hipotenusa do triângulo vai medir {:.2f}'.format(hypot(catopo, catadj)))
print('A hipotenusa do triângulo vai medir {:.2f}'.format(hip))