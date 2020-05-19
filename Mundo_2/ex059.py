from time import sleep
first = int(input('Enter the first value: '))
second = int(input('Enter the second value: '))
option = 0
while option != 5:
    print('''    [1] Sum the values
    [2] Multiple the values
    [3] Higher value
    [4] Enter new values
    [5] Exit
    ''')
    option = int(input('Enter your option: '))
    if option == 1:
        s = first + second
        sleep(1)
        print(f'\nThe Sum of the values is {s}')
    elif option == 2:
        m = first * second
        sleep(1)
        print(f'The product of the values is {m}')
    elif option == 3:
        if first > second:
            sleep(1)
            print(f'{first} is the higher value')
        else:
            sleep(1)
            print(f'{second} is the higher value')
    elif option == 4:
        first = int(input('Enter the first new value: '))
        second = int(input('Enter the second new value: '))
    elif option == 5:
        print('Exiting....')
        sleep(1)
    else:
        print('\nInvalid option, Try again!')
    print('-=-' *20)
print('End of the program, see you soon!')