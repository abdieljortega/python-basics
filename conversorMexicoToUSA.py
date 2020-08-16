dolares = input('¿Cuántos dolares tienes?: ')
dolares = float(dolares)
valorPesoMexicano = 21.98
pesos = dolares * valorPesoMexicano
pesos = round(pesos, 2)
pesos = str(pesos)
print('El resultado es $' + pesos + ' ' + ' pesos')