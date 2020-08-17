def conversor(tipoPesos, valorDolar):
  pesos = input('¿Cuántos pesos ' + tipoPesos + ' tienes?: ')
  pesos = float(pesos)
  dolares = pesos / valorDolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('El resultado es $' + dolares + ' ' + ' dolares')

menu = """
Bienvenido al conversor de monedas 💰💰💰

1 - Pesos Mexicanos
2 - Pesos Colombianos
3 - Pesos Argentinos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
  conversor('mexicanos', 21.98)
elif opcion == '2':
  conversor('colombianos', 3875)
elif opcion == '3':
  conversor('argentinos', 65)
else:
  print('Ingresa una opción correcta por favor')
