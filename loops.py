def loop(times = 100, count = 0):
  if count > times:
    return
  else:
    print(2 ** count)
    count = count + 1
    loop(times, count)

def run():
  loop()

if __name__ == '__main__':
  run()