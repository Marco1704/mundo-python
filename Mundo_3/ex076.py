prod_list = ('pencil', 1.75,
             'eraser', 0.99,
             'notebook', 2.00,
             'pencase', 1.50,
             'transferor', 1.20,
             'compass', 2.50,
             'rucksack', 150.50,
             'pen', 1.00,
             'book', 45.00)
print('-' * 40)
print(f'{"PRODUCT LIST":^40}')
print('-' * 40)
for pos in range(0, len(prod_list)):
    if pos % 2 == 0:
        print(f'{prod_list[pos]:.<30}', end='')
    else:
        print(f'£{prod_list[pos]:>7.2f}')
print('-' * 40)