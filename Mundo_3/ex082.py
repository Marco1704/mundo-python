general = []
even = []
odd = []
while True:
    general.append(int(input('Enter a number: ')))
    res = str(input('Another number? [Y/N] ')).upper().strip()
    if res in 'N':
        break
print('-=-' * 30)
print(f'The complete list of numbers is: {general}')
for n in general:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
#for i, v in enumerate:
#    if v % 2 == 0:
#       even.append(v)
#    else:
#       odd.append(v)
print(f'the list of odd numbers entered is: {odd}')
print(f'The lis of even numbers entered is: {even}')