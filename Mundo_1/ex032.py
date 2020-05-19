from datetime import date
year = int(input('Enter the Year? or enter 0 to analyse the current one? '))
if year == 0:
    year = date.today().year #grabs the value of the current year on the machine.Breakbreak
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')