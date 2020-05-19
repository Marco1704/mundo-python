a1 = int(input('Enter the first term of the AP: '))
d = int(input('Enter the common difference of the AP: '))
n = int(input('How many AP terms do you want to show: '))
an = a1
cont = 1
plus = n
total = 0
while plus != 0:
    total = total + plus
    while cont <= total:
        print(f'{an}', end='-')
        an += d
        cont += 1
    print("interval")
    plus = int(input('How many terms you want to add to this AP: '))
print('End')

