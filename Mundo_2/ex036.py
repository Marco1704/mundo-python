costhouse = float(input('Enter the value of the house: £'))
salary = float(input('Enter the monthly salary: £'))
years = int(input('Enter the number years: '))
repayments = costhouse/(years * 12)
print(f'To buy a house of £{costhouse:0.2f} in {years} years, the monthly repayments are going to be £{repayments:.2f}')
if repayments > salary * .30:
    print(f'Unfortunately the loan was rejected as the repayments are more than 30% of your salary')
else:
    print(f'Congratulations, the loan has been approved')