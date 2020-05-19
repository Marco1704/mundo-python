people = []
person = {}
agesum = ageav = 0
count = 0
while True:
    person.clear()
    person['name'] = str(input('Enter the forename: ')).capitalize().strip()
    while True:
        person['gender'] = str(input('Gender:[M/F] ')).upper().strip()
        if person['gender'] in 'MF':
            break
        print('Gender can be only M of F,please try again!')
    person['age'] = int(input('Age: '))
    agesum += person['age']
    people.append(person.copy())
    while True:
        opt = str(input('New Entry? [Y/N]' )).upper().strip()
        if opt in 'YN':
            break
        print('Invalid entry, please try again!')
    if opt == 'N':
        break
print('-=' * 30)
print(people)
print('-=' * 30)
print(f'A) {len(people)} person(s) were registered today')
print(f'B) The average age is {agesum/len(people):5.2f} years old')
print(f'C) The name of the woman registered is ', end=' ')
for p in people:
    if p['gender'] in 'Ff':
        print(f'{p["name"].capitalize()} ', end=' ')
print()
print(f'D) List of people over the average age is: ', end=' ')
for p in people:
    if p['age'] >= agesum/len(people):
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('Finished')


