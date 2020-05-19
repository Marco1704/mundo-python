heavier = 0
lighter = 0
for p in range(1, 6):
    weight = float(input(f'Enter the weigh of the {p}a person: '))
    if p == 1:
        heavier = weight
        lighter = weight
    else:
        if weight > heavier:
            heavier = weight
        if weight < heavier:
            lighter = weight
print(f'the heavier weight is {heavier}kg')
print(f'The lighter weight is {lighter}kg')