def showlinha():
    print('-' * 40)


def area(h, w):
    a = h * w
    showlinha()
    print(f'The area of a plot of {h:.2f}m widht X {w:.2f}m length is {a:.2f}m2 ')


print('Plot Management')
showlinha()
h = float(input('Enter the widht of the plot:(m) '))
w = float(input('Enter the lenght of the plot:(m) '))
area(h, w)



