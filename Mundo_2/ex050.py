su = 0
co = 0
for c in range(1, 7):
    n = int(input('Enter the number: '))
    if n % 2 == 0:
        su += n
        co += 1
print(f'the Sum of all {co} even numbers is {su}')
