numbers = []
for c in range(0, 5):
    n = int(input('Enter a number: '))
    if c == 0 or n > numbers[-1]:
        numbers.append(n)
        print('Added to the end of the list...')
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
                print(f'Added to the {pos} position of the list')
                break
            pos += 1
print(f'The numbers entered on the list are: {numbers}')



