from _random import shuffle
name1 = str(input('First student: '))
name2 = str(input('Second student: '))
name3 = str(input('Third student: '))
name4 = str(input('Fourth student: '))
names = [name1, name2, name3, name4]
shuffle(names)
print(f'The presentation order will be as follows: \n{names}')