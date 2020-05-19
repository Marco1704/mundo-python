num = (int(input('Enter the first number: ')), int(input('Enter the first number: ')),
       int(input('Enter the first number: ')),int(input('Enter the first number: ')))
print(f'You entered the following numbers: {num} ')
print(f'The number 9 appeared {num.count(9)} times')
if 3 in num:
    print(f'the number 3 was entered in the position number {num.index(3)+1}')
else:
    print(f'The numbers is not in this list')
print(f'The even numbers are: ', end='')
for n in num:
    if n % 2 == 0:
        print(n,end='')
