s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print(f'The sum of all odd numbers that are multiples of 3 between 1 and 500 is {s}')