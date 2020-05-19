student = {}
student['name'] = str(input('Student Name:'))
student['average'] = float(input(f'Average Grade of {student["name"]}: '))
if student['average']  >= 7:
    student['Situation'] = 'Pass'
elif 5 <= student['average']< 7:
    student['Situation'] = 'Summer Class'
else:
    student['Situation'] = 'Not Pass'
print('-=-' * 10)
print('    Final Summary    ')
print('-=-' * 10)
for k, v in student.items():
    print(f'{k.capitalize()} = {v}')