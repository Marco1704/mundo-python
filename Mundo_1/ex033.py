n1 = int(input('Enter the first value: '))
n2 = int(input('Enter the second Value: '))
n3 = int(input('Enter the third value: '))
if n3<n1>n2:
    highest = n1
if n1<n2>n3:
    highest = n2
if n1<n3>n2:
    highest = n3
if n2>n1<n3:
    lowest = n1
if n1>n2<n3:
    lowest = n2
if n1>n3<n2:
    lowest = n3
print(f'{highest} is the highest value entered')
print(f'{lowest} is the lowest value')

