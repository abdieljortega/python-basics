import random


def run():
  randomNumber = random.randint(1, 100)
  choosenNumber = int(input('Introduce un número del 1 al 100: '))
  while choosenNumber != randomNumber:
    if choosenNumber < randomNumber:
      print('Busca un número más grande')
    else:
      print('Busca un número más pequeño')
    choosenNumber = int(input('Elige otro número: '))
  print('¡Ganaste!')


if __name__ == "__main__":
    run()