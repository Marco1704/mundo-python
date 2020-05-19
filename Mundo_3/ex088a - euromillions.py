from random import randint
from time import sleep
numbers = []
print('-=-' * 10)
print('         Euromillions            ')
print('-=-' * 10)
numg = int(input('How many games you want to generate? '))
games = []
tot = 1
while tot <= numg:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in numbers:
            numbers.append(num)
            cont += 1
        if cont >= 6:
            break
    numbers.sort()
    games.append(numbers[:])
    numbers.clear()
    tot +=1
print('-=-' * 3, f'SORTEANDO {numg} GAMES', '-=-' * 3)
for i, l in enumerate(games):
    print(f'Game {i+1} : {l}')
    sleep(1)
print('Good Luck!!!')