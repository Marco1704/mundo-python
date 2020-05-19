from datetime import date
employee = {}
employee['Name'] = str(input('Name: ')).capitalize().strip()
employee['Year'] = int(input('Year of Birht: '))
employee['NIN'] = int(input('National Insurance number [enter 0 if not applicable]: '))
employee['age'] = date.today().year - employee['Year']
if employee['NIN'] == 0:
    print('-=' *35)
    print(f' - Employee name: {employee["Name"]}')
    print(f' - {employee["Name"]} is {employee["age"]} years old')
    print(f' - {employee["Name"]} do not have a National Insurance number')
if employee['NIN'] != 0:
    employee['salary'] = float(input('Monthly Salary: £ '))
    employee['startingyear'] = int(input(f'Year when {employee["Name"]} start to work: '))
    employee['retirement'] = (employee['startingyear'] - employee['Year']) + 35
    print('-=' * 35)
    print(f' - Employee name: {employee["Name"]}')
    print(f' - {employee["Name"]} is {employee["age"]} years old')
    print(f' - {employee["Name"]} National Insurance number is: {employee["NIN"]}')
    print(f' - {employee["Name"]} start work in {employee["startingyear"]}')
    print(f' - Salary is £{employee["salary"]}')
    print(f' - {employee["Name"]} will retire at the age of {employee["retirement"]} year old')