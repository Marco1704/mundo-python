print('-=-' * 10)
print('Triangle Analyser')
print('-=-' * 10)
a = float(input('Enter the value of segment a: '))
b = float(input('Enter the value of segment b: '))
c = float(input('Enter the value of segment c: '))
if a>b+c or b>a+c or c>a+b:
    print('The above line segments CANNOT form a triangule')
else:
    print('The above line segments CAN form a triangule')
