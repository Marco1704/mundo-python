n = 1
while n > 0:
    n = int(input('Enter the number to show its multiplication table: '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i:2} = {n * i}')
    print('--' *30)
print("Multiplication tables do not exist for negative values")