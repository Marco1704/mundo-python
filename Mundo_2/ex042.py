print('-=-' * 25)
print('Analyse the line segments values and indicate if they can form a triangle ')
print('-=-' * 25)
a = float(input('Enter the value of the first segment: '))
b = float(input('Enter the value of the second segment: '))
c = float(input('Enter the value of the third segment: '))
if a < b + c and b < a + c and c < a + b:
    print('The segments can form a triangle', end='')
    if a == b == c:
        print(" equilateral")
    elif a == b and a != c:
        print(" isosceles")
    else:
        print(" scalene")
else:
    print('The segments CANNOT form a triangle')