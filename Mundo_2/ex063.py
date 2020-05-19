print('---------------------')
print('Fibonacci Sequence')
print('---------------------')
n = int(input('Enter the number of terms that you want to show: '))
t1 = 0
t2 = 1
cont = 0
while cont <= n:
    tn = t1 + t2
    print(f'{tn}', end='-')
    t1 = t2
    t2 = tn
    cont += 1
print('End')

'''print('-' * 30)
print('Fibonacci Sequence')
print('-' * 30)
n = int(input('Enter the number of terms to show: '))
t1 = 0
t2 = 0
count = 0
while count<='''