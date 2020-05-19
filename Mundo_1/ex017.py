#'''a = float(input('Enter the lenth of side A: '))
#b = float(input('Enter the lenth of side B: '))
#c = math.sqrt(a**2 + b**2)
#print(f'The triangle hypotenuse lenth is {c:.2f}')'''


import math
a = float(input('Enter the lenth of side A: '))
b = float(input('Enter the lenth of side B: '))
c = math.hypot(a,b)
print(f'The triangle hypotenuse lenth is {c:.2f}')