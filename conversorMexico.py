pesos = input('¿Cuántos pesos mexicanos tienes?: ')
pesos = float(pesos)
valorDolar = 21.98
dolares = pesos / valorDolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('El resultado es $' + dolares + ' ' + ' dolares')