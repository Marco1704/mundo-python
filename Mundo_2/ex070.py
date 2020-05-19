total = total1000 = lower = count = 0
name = ' '
while True:
    pro = str(input('Name of the product: '))
    price = float(input('Cost of the product: £ '))
    count += 1
    total += price
    if price > 1000:
        total1000 += 1
    if count == 1:
        lower = price
        name = pro
    else:
        if price < lower:
            lower = price
            name = pro
    option = ' '
    while option not in 'YN':
        option = str(input('New product? [Y/N]')).strip().upper()
    if option == 'N':
        break
print('-=-' * 30)
print(f'The purchase total is : £ {total:.2f}')
print(f'{total1000} product is over £1000')
print(f'The product with the lowest price is the {name} and costs £{lower:.2f}')
