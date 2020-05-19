num = int(input('Enter a number: '))
conversion = int(input('Choose the Conversion Base \n[1] for binary \n[2] for octal \n[3] for hexadecimal \nEnter your choice: '))
if conversion == 1:
    print(f'{num} in binary is {bin(num)[2:]}')
elif conversion == 2:
    print(f'{num} in hexadecimal base is {hex(num)[2:]}')
elif conversion == 3:
    print(f'{num} in Octal base is {oct(num)[2:]}')