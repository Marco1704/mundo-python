matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sev = hi = scol = sumto =  0
for l in range(0, 3):
    for c in range(0,3):
        matrix[l][c] = int(input(f'Enter the number for [{l},{c}]: '))
print('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            sev += matrix[l][c]
        sumto += matrix[l][c]
    print()
print('-=-' * 30)
print(f'The sum of the even numbers is {sev}')
for l in range(0, 3):
    scol += matrix[l][2]
print(f'The sum of the values on the third column is {scol}')
for c in range(0, 3):
    if c == 0:
        hi = matrix[1][c]
    elif matrix[1][c] > hi:
        hi = matrix[1][c]
print(f'The higher value on the second line is {hi}')
print(sumto)