celsius = float(input('Informe a temperatura em ºC: '))
farenheit = (celsius * 9/5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f} °F!'.format(celsius, farenheit))
if celsius <= 16:
    print('Tá uma friaquinha. Não esquece o casaquinho!')
elif celsius >= 31:
    print('Tá calor hein bicho, até cavalo na bunda sua!')
else:
    print('Tempinho bão, hein!')
