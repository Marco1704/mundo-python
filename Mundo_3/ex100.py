from random import randint
from time import sleep

def drawn(numbers):
    print('Drawing 5 values for the list:')
    count = 0
    while count < 5:
        numbers.append(randint(1, 10))
        count += 1
    for n in numbers:
        print(f'{n} ', end='')
        sleep(0.3)
    print('Ready')



def totalsum(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    print(f'The total Sum of the even values on the list is {total}')




values = []
drawn(values)
totalsum(values)



