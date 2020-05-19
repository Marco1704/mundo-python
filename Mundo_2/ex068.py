'''from random import randint
print('-><-' * 10)
print("Let's Play Odds or Even")
print('-><-' * 10)
while True:
    p1 = int(input('Enter a number: '))
    com = randint(0, 10)
    play = ' '
    count = 0
    total = p1 + com
    while play not in 'OE':
        play = str(input('Odds or Even? [O/E] ')).upper().strip()
    print(f'You play {p1} and the computer play {com}, total of {total} ', end='')
    print('EVEN' if total % 2 == 0 else 'ODDS')
    if type == 'E':
        if total % 2 == 0:
            print('You Won!!!')
            count += 1
        else:
            print('You Lost!!!')
            break
    elif type == 'O':
        if total % 3 == 0:
            print('You Won!!!')
            count += 1
        else:
            print('You lost!!!')
            break
    print("Let's play again")
print(f'Game Over, you won {count} times')'''

from random import randint
count = 0
while True:
    p1 = int(input('Enter your number: '))
    com = randint(0, 10)
    play = ' '
    total = p1 + com
    while play not in 'OE':
        play = str(input("Odd or Even? [O/E]")).upper().strip()
    print(f'Your number is {p1} and the computer number is {com}, total of {total} ', end='')
    print('it is a EVEN number' if total % 2 == 0 else 'it is a ODD number')
    if play == 'E':
        if total % 2 == 0:
            print('You Won!!!')
            count += 1
        else:
            print('You Lost!!!')
            break
    elif play =='O':
        if total % 2 == 1:
            print('You Won!!!')
            count += 1
        else:
            print('You Lost!!!')
            break
    print("Let's Play Again")
print(f'Game Over, you won {count} times')