from time import sleep
from random import randint
items = ('Rock', 'Paper', 'Scissor')
computer = randint(0, 2)
print('''Your options are:
[0] Rock
[1] Paper
[2] Scissor''')
player = int(input('Enter your chosen option: '))
sleep(2)
print('-=-' * 15)
print(f'Player choose {items[player]}')
print(f'Computer choose {items[computer]}')
print('-=-' * 15)
if computer == 0:
    if player == 1:
        print('\33[7;35mPLAYER WINS!!!\033[m')
    elif player == 2:
        print('COMPUTER WINS!!!')
    elif player == 0:
        print('DRAW!!!')
    else:
        print('INVALID OPTION!!!')
if computer == 1:
    if player == 1:
        print('DRAW')
    elif player == 2:
        print('PLAYER WINS!!!')
    elif player == 0:
        print('COMPUTER WINS!!!')
    else:
        print('INVALID OPTION!!!')
if computer == 2:
    if player == 1:
        print('COMPUTER WINS!!!')
    elif player == 2:
        print('DRAW!!!')
    elif player == 0:
        print('PLAYER WINS!!!')
    else:
        print('INVALID OPTION!!!')