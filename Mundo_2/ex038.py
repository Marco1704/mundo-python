val1 = int(input('Enter the first value: '))
val2 = int(input('Enter the second value: '))
if val1 > val2:
    print(f'The first value is the highest value')
elif val1 < val2:
    print(f'The Second value is the highest value')
elif val1 == val2:
    print(f'Values are equal')