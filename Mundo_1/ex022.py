name = str(input('Enter your full name: ')).strip()
print(f'Your name in upper case is {name.upper()}')
print(f'Your name in upper case is {name.lower()}')
print(f'Your name has the lenth of {len(name)}')
print(f'Your name has the lenth of {len(name)-len(name.split())} without white spaces')
new_name = (name.split())
print(f'Your first name has the lenth of {len(new_name[0])}')
#second solution for the lenth of the first name
#print(f'Your fist name has the lenth of {name.find(" ")}')