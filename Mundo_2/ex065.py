res = 'S'
count = 0
nsum = 0
h = 0
lo = 0
avn = 0
while res != 'N':
    n = int(input('Enter the number: '))
    count += 1
    nsum += n
    avn = nsum / count
    res = str(input('New number S/N:')).upper().strip()
    if count == 1:
        h = lo = n
    else:
        if n > h:
            h = n
        if n < lo:
            lo = n
print(f'The average of the entered numbers is {avn} \nThe highest number is {h} and the lowest number is {lo}')
