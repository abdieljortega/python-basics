# def printMessage():
#   print('Mensaje especial: ')
#   print('¡Estoy aprendiendo a usar funciones')

# printMessage()
# printMessage()
# printMessage()

def conversacion(mensaje):
  print('Hola')
  print('Cómo estás?')
  print(mensaje)
  print('Adios')

opcion = input('Elige una opción (1, 2, 3): ')
if opcion == '1':
  conversacion('Elegiste la opcion ' + opcion)
elif opcion == '2':
  conversacion('Elegiste la opcion ' + opcion)
elif opcion == '3':
  conversacion('Elegiste la opcion ' + opcion)
else:
  print('Escribe la opción correcta')