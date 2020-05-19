num = int(input('Enter a value to calculate its factorial: '))
fac = 1
numfac = num
while numfac > 0:
    fac = fac * numfac
    numfac = numfac - 1
print(f'The factorial of {num} is {fac}')
