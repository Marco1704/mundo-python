words = ('learn', 'programming', 'language', 'python', 'course', 'free', 'study', 'practice',
         'work', 'market', 'programmer', 'future')
vowels = ('a','e','i','o','u')
for w in words:
    print(f'\nIn the word {w.upper()} we have', end=' ')
    for letter in w:
        if letter.lower() in vowels:
            print(letter, end=' ')
