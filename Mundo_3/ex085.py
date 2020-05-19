'''numbers = []
odd = []
even = []
while True:
    for n in range(0, 7):
        n = int(input(f'Enter the {n + 1} value:  '))
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    break
numbers.append(even[:])
numbers.append(odd[:])
print(f'The numbers entered are: {numbers}')
print(f'The even numbers are: {even}')
print(f'The odd numbers are: {odd}')'''

numbers = [[] , []]
value = 0
for c in range(1,8):
    value = int(input('Enter a number: '))
    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)
numbers[0].sort()
numbers[1].sort()
print('-=-' * 30)
print(f'The values entered are: {numbers}')
print(f'The even numbers are: {numbers[0]}')
print(f'The odd numbers are: {numbers[1]}')
