from random import randint
from time import sleep
items = ('Rock','Paper','Scissor')
computer = randint(0,2)
print('-=-' * 10)
print("Let's play Rock-paper-scissors")
print('-=-' * 10)
player = int(input('''Choose from the below!!!
[0] Rock
[1] Paper
[2] Scissor
Enter you option? '''))
print('Rock!!!')
sleep(1)
print('Paper!!!')
sleep(1)
print('Scissor!!!')
sleep(2)
print('-=-' * 5)
print(f'Player choose {items[player]}')
print(f'Computer Choose {items[computer]}')
print('-=-' * 5)
if computer == 0:
    if player == 0:
        print('DRAW!!!')
    elif player == 1:
        print('PLAYER WINS!!!')
    elif player == 2:
        print('COMPUTER WINS!!!')
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