from time import sleep


def count(i, f, p):
    print('-=' * 15)
    print(f'The count between {i} to {f} with pace {p} is ')
    sleep(2.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('End')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('End')



count(1, 10, 1)
count(10, 0, 2)
print('-=' * 15)
print('Try your own count')
intial = int(input('Enter the first element: '))
final = int(input('Enter the last element: '))
pas = int(input('Enter the pace: '))
count(intial, final, pas)
print('...Exiting...')
