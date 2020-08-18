import random


def passwordGenerator():
  uppercases = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  lowercases = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  symbols = ['!', '#', '$', '&', '/', '(', ')']
  numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

  characters = uppercases + lowercases + symbols + numbers

  password = []

  for i in range(15):
    randomCharacter = random.choice(characters)
    password.append(randomCharacter)

  password = ''.join(password)
  return password


def run():
  password = passwordGenerator()
  print('Tú nueva contraseña es: ' + password)


if __name__ == "__main__":
    run()