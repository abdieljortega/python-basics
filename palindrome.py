def palindrome(word):
  word = word.replace(' ', '').lower()
  invertedWord = word[::-1]
  if word == invertedWord:
    return True
  else:
    return False


def run():
  word = input('Write a word: ')
  isPalindrome = palindrome(word)
  if isPalindrome:
    print('Is palindrome')
  else:
    print('Is not palindrome')


if __name__ == '__main__':
  run()