student = []
while True:
    name = str(input('Name: ')).capitalize().strip()
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))
    avgrade = (grade1 + grade2) / 2
    student.append([name, [grade1, grade2], avgrade])
    resp = ' '
    while resp not in 'NnYy':
        resp = str(input('Another student? [Y/N]'))
    if resp == 'N':
        break
print('-=' * 15)
print(f'{"No.":<4}{"Name:":<10}{"Average Grade:":>8}')
print('-=' * 15)
for i, a in enumerate(student):
    print(f'{i:<4}{a[0]:<8}{a[2]:>8.1f}')
while True:
    print('-=' * 20)
    opt = int(input('Enter the student ID to show the grades: (999 to exit)  '))
    if opt == 999:
        print('Exiting...')
        break
    if opt <= len(student) - 1:
        print(f'Grades of {student[opt][0]} are {student[opt][1]}')
print('Have a nice day!!!')
