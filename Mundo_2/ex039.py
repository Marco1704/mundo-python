from datetime import date
birth = int(input('Enter your year of birth: '))
curyear = date.today().year
age = curyear - birth
if age < 18:
    futdate = 18 - age
    yearenlist = curyear + futdate
    print(f'You are {age}. \nYou will be apt for national service in {yearenlist}')
elif age == 18:
    print('Enlist now for your National Service')
elif age > 18:
    pasdate = age - 18
    yearenlist = curyear - pasdate
    print(f'You should have enlist for your national Service {age-18} years ago in {yearenlist}')