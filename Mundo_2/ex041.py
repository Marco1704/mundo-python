from datetime import date
yearbirth = int(input('Enter your year of birth: '))
curyear = date.today().year
age = curyear - yearbirth
if age <= 9:
    print('You are going to compete in the grassroots category')
elif age <=14:
    print('You are going to compete in the Infant category')
elif age <=19:
    print('You are going to compete in the Junior category')
elif age <=20:
    print('You are going to compete in the Senior category')
elif age > 20:
    print('You are going to compete in the Master category')