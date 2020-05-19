name = str(input('Enter a sentence:').lower()).strip()
total = name.count('a')
first = name.find('a') + 1
last = name.rfind('a') + 1
print(f'How many times the word the letter "a" appears in the sentence? {total} '
      f'\nWhich position the letter "a" appeared first? {first} '
      f'\nWhich position the letter "a" appeared last? {last}')