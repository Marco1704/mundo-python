from time import sleep
numcount = 0
numsum = 0
num = 0
#num = numcount = numsum = 0
while num < 999:
    num = int(input('Enter a number [999 to exit]: '))
    numsum += num
    numcount += 1
    if num == 999:
        numsum -= num
        numcount -= 1
        print('Exiting...')
        sleep(1)
print(f'{numcount} values were entered and their sum is {numsum}')