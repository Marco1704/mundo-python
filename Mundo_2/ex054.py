from datetime import date
curyear = date.today().year
totadults = 0
totunder = 0
for indv in range(1, 8):
    year = int(input(f'Enter the year of birth of the {indv}a person: '))
    if (curyear - year) > 21:
        totadults += 1
    else:
        totunder += 1
print(f'{totadults} people from the group are legally adults')
print(f'{totunder} people from the group are underage')