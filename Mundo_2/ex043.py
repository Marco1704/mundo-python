print('Calulate your BMI')

w = float(input('Enter your weight:(kg) '))
h = float(input('Enter your Height:(m) '))

BMI = w / (h**2)

if BMI <= 18.5:
    print(f'You are underweight, your BMI is {BMI:.2f}')
elif BMI <= 25:
    print(f'You are healthy, your BMI is {BMI:.2f}')
elif BMI <= 30:
    print(f'You are overweight, your BMI is {BMI:.2f}')
elif BMI <= 40:
    print(f'You are obese, your BMI is {BMI:.2f}')
elif BMI > 40:
    print(f'You are extremely obese, your BMI is {BMI:.2f}')