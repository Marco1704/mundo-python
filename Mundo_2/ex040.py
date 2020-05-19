print('-=-'*25)
print('Calculate the average score of a student and indicate if it is a Pass or Fail ')
print('-=-'*25)
grade1 = float(input('Enter the value for the first grade: '))
grade2 = float(input('Enter the value of the second grade: '))
ave = (grade1 + grade2)/2
print(f'The average grade is {ave:0.2f}')
if ave < 5.0:
    print('The student Fail')
elif 5.0<ave<6.9:
    print('The student needs to attend Summer School')
elif ave > 7.0:
    print('The student Pass')