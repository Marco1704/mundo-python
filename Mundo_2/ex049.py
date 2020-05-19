n = int(input('Enter the number to calcule its multiplication table: '))
for c in range(1,11):
    print('-' * 10)
    print(f'{n} x {c:2} = {n * c}')