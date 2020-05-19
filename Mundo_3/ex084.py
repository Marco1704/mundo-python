people = []
mainlist = []
hw = lw = 0
while True:
    people.append(str(input('Name: ')))
    people.append(float(input('Weihgt:[kg] ')))
    if len(mainlist) == 0:
        hw = lw = people[1]
    else:
        if people[1] > hw:
            hw = people[1]
        if people[1] < lw:
            lw = people[1]
    mainlist.append(people[:])
    people.clear()
    answer = str(input('Another Entry? [Y/N] ')).upper().strip()
    if answer not in 'Y':
        break
print('-=-' * 30)
print(f'The data entered is: {mainlist}')
print(f'{len(mainlist)} people have been registered on our database.')
print(f'The heaviest weight is {hw}kg. Weight of', end=' ')
for p in mainlist:
    if p[1] == hw:
        print(f'[{p[0]}]')
print(f'The lowest weight is {lw}kg. Weight of', end=' ')
for p in mainlist:
    if p[1] == lw:
        print(f'[{p[0]}]')