elements = []
while True:
    elements.append(int(input('Enter a number: ')))
    res = str(input('Add another number? [Y/N]')).upper().strip()
    if res in 'N':
        break
print('-=-' * 15)
print(f'You entered {len(elements)} elements in the list')
elements.sort(reverse=True)
print(f'The list of elements in reverse order is {elements}')
if 5 in elements:
    print('5 is in the list')
else:
    print('5 is not in the list')
