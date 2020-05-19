import math
x = float(input('Enter the value of the angle: '))
sn = math.sin(math.radians(x))
cs = math.cos(math.radians(x))
tn = math.tan(math.radians(x))
print(f'The Sine of {x} is {sn:.2f} \nThe Cosine of {x} is {cs:.2f} \nThe Tangent of {x} is {tn:.2f}')
