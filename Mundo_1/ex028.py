import random
from time import sleep
print('-' *80)
print("I'm thinking on a number between 0 and 5, can you guess the right answer?")
print('-' *80)
x = random.randint(0,5)
numguess = int(input('Enter your guess: '))
print('Computing...')
sleep(3)
if numguess == x:
    print('Congratulations, you guess the right number')
else:
    print(f'You lost, the number is {x} and not {numguess}')