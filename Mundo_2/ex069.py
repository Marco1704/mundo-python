print('-=-' * 15)
print('Personnel Registration')
print('-=-' * 15)
tot18 = 0
totm = 0
totf = 0
while True:
    age = int(input('\nEnter the age: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Enter the sex: [F/M] ')).upper().strip()
        if age > 18:
            tot18 += 1
        if gender == 'M':
            totm += 1
        if gender == 'F' and age < 20:
            totf += 1
    option = ' '
    while option not in 'YN':
        option = str(input('\nNew Entry? [Y/N]')).upper().strip()
    if option == 'N':
        break
print(f'{tot18} people are over 18 years old have been registered.\n{totm} are man.\n{totf} women are under 20 years old.')
print('Exit, Have a nice day')