# write a program that will calculate salary increases
#condition 1 salary higher than £2500 receives 10% increase
#condition 2 salary lower or equal to £2500 receives 15% increase

salary = float(input('Enter the current salary: £'))
if salary > 2500:
    new_salary = salary * 0.10 + salary
else:
    new_salary = salary * 0.15 + salary
print(f'The New Salary will be {new_salary}')
