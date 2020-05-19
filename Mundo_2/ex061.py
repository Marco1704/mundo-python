a1 = int(input('Enter the first term of the AP: '))
d = int(input('Enter the common difference of the AP: '))
n = int(input('How many AP terms do you want to show: '))
an = a1
cont = 1
while cont <= n:
    print(f'{an}', end='-')
    an += d
    cont += 1
print('end')
