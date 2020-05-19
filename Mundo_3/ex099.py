from time import sleep
from random import randint


def higher(* num): #*num - means that you don't the exact number of parameters that you are going to receive.
    cont = higher = 0
    print('-=-' * 15)
    print('Analysing the values...')
    for values in num:
        print(f'{values} ', end='')
        sleep(0.5)
        if cont == 0:
            higher = values
        else:
            if values > higher:
                higher = values
        cont += 1
    print(f'\nThe total number of values entered is {cont}.')
    print(f'The highest value is {higher}')






#principal program
higher(2,9,4,5,7,1)
higher(4, 7, 0)
higher(1,2)
higher(6)
higher()