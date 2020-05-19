a1 = int(input('Enter the first element of the AP: '))
d = int(input('Enter the common difference of the PA: '))
ap = []
for n in range(1, 11):
    an = a1 + (n - 1) * d
    ap.append(an)
print(ap)


'''a1 = int(input('Enter the first element of the AP: '))
d = int(input('Enter the common difference of the PA: '))
a10 = a1 + (10 - 1) * d
for c in range(a1, a10 + d, d):
    print(f'{c}', end='-')
print('end')'''