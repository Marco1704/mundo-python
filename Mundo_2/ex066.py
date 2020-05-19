n = count = s = 0
while n != 999:
    n = int(input('Enter a number: '))
    count += 1
    if n == 999:
        break
    s += n
print(f'{count} numbers were entered and their sum is {s}')