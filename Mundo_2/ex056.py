youngstwomen = 0
sumage = 0
totper = 0
oldestman = 0
oldestname = ''
for p in range(1, 5):
    print(f'-----{p}a Person-----')
    name = str(input('Name: ')).capitalize()
    age = int(input('Age: '))
    sex = str(input('Sex [M/F]: ')).upper()
    totper += 1
    sumage += age
    if p == 1 and sex == 'M':
        oldestman = age
        oldestname = name
    if sex == 'M' and age > oldestman:
        oldestman = age
        oldestname = name
    if sex == 'F' and age < 20:
        women += 1
print(f'\nThe average age of the group is {sumage/totper} years')
print(f"\nWe've a total of {youngstwomen} women in the group with less than 20 years old ")
print(f"\nThe oldest man in group is {oldestname} and he is {oldestman} years old")
