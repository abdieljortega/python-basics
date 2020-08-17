def run():
  # for count in range(1000):
  #   if count % 2 != 0:
  #     continue
  #   print(count)

  # for i in range(0, 10000):
  #   print(i)
  #   if i == 5678:
  #     break

  # text = input('Excribe un texto: ')
  # for letter in text:
  #   if letter == 'o':
  #     break
  #   print(letter)

  du = 'Du'
  batman = 'Batman!'
  count = 0
  while True:
    if count == 15:
      print(batman)
      break
    print(du)
    count += 1


if __name__ == "__main__":
    run()