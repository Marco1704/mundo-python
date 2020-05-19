num = int(input('Enter a number: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0 and num %  num == 0:
        print("\33[34m", end=' ')
        tot += 1
    else:
        print('\33[33m',end=' ')
    print(f'{c}', end='')
print(f'\nThe {num} is divisible {tot} times')
if tot == 2:
    print(f'{num} is Prime')
else:
    print(f'{num} is not Prime')

