distance = float(input('Enter the distance in km of your travel? '))
if distance<=200:
    print(f'The travel will cost £{distance*0.50}')
else:
    print(f'The travel will cost £{distance*0.45}')
