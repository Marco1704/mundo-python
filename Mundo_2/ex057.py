gender = str(input('Enter your gender M/F: ')).upper().strip()[0]
while gender not in 'MmFf':
    gender = str(input('Invalid entry,please enter your gender M/F: ')).upper().strip()[0]
print('Thanks, have a nice day!')