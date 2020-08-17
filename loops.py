# def loop(times = 100, count = 0):
#   if count > times:
#     return
#   else:
#     print(2 ** count)
#     count = count + 1
#     loop(times, count)

# def run():
#   loop()

# if __name__ == '__main__':
#   run()

def run():
  LIMIT = 1000

  count = 0
  powOf2 = 2 ** count
  while powOf2 < LIMIT:
    print('2 elevado a ' + str(count) + ' es igual a: ' + str(powOf2))
    count = count + 1
    powOf2 = 2 ** count

if __name__ == '__main__':
  run()