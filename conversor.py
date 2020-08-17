menu = """
Bienvenido al conversor de monedas 💰💰💰

1 - Pesos Mexicanos
2 - Pesos Colombianos
3 - Pesos Argentinos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
  pesos = input('¿Cuántos pesos mexicanos tienes?: ')
  pesos = float(pesos)
  valorDolar = 21.98
  dolares = pesos / valorDolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('El resultado es $' + dolares + ' ' + ' dolares')
elif opcion == '2':
  pesos = input('¿Cuántos pesos colombianos tienes?: ')
  pesos = float(pesos)
  valorDolar = 3875
  dolares = pesos / valorDolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('El resultado es $' + dolares + ' ' + ' dolares')
elif opcion == '3':
  pesos = input('¿Cuántos pesos argentinos tienes?: ')
  pesos = float(pesos)
  valorDolar = 65
  dolares = pesos / valorDolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('El resultado es $' + dolares + ' ' + ' dolares')
else:
  print('Ingresa una opción correcta por favor')
