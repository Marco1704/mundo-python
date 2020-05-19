'''phrase = str(input('Enter the phrase to be analysed: ').upper()).strip()
words = phrase.split()
new_phrase = ''.join(words)
backwards = ''
for word in range(len(new_phrase) -1, -1, -1):
    backwards += new_phrase[word]
if backwards == new_phrase:
    print('The phrase is a Palindrome')
else:
    print('The phrase is not a Palindrome')'''

#second solution
phrase = str(input('Enter the phrase to be analysed: ').upper()).strip()
words = phrase.split()
new_phrase = ''.join(words)
backwards = new_phrase[::-1]
print(f'The inverse of {new_phrase} is {backwards}')
if backwards == new_phrase:
    print('The phrase is a Palindrome')
else:
    print('The phrase is not a Palindrome')