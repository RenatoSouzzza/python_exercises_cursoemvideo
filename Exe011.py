h = float(input('Altura da parede:'))
b = float(input('Largura da parede: '))
area = h * b
print('Sua parede com {:.2f}m de Altura e {:.2f}m de largura tem uma área de {:.3f}m²'.format(h, b, area))
print('Para pintá-la você precisará de {:.4f}l de tinta, caso faça somente uma demão'.format(area / 2))