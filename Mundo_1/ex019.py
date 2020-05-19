import random
name1 = str(input('First student: '))
name2 = str(input('Second student: '))
name3 = str(input('Third student: '))
name4 = str(input('Fourth student: '))
ls = [name1, name2, name3, name4]
es = random.choice(ls)
print(f'The chosen student is {es}')