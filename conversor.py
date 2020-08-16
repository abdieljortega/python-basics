pesos = input('¿Cuántos pesos colombianos tienes?: ')
pesos = float(pesos)
valorDolar = 3875
dolares = pesos / valorDolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('El resultado es $' + dolares + ' ' + ' dolares')