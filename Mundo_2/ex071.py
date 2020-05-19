print('-=-' * 15)
print(f'\t\t\tPython Bank')
print('-=-' * 15)
withdrawn = int(input('Please enter the value to be withdrawn? £'))
total = withdrawn
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total of {totalced} paper notes of £{ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
                break
print('-=-' * 15)
print('Have a nice day')
