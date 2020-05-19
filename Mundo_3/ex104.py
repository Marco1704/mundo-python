def leiaint(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\33[0;31mError, enter a valid absolute number.\33[m')
        if ok:
            break
    return value



n = leiaint('Enter a number: ')
print(f'The number you entered is {n}')