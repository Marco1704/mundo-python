import coin



price = float(input('Enter the price: £ '))
rate = 10
print(f'The double of {price} is £{coin.double(price)}')
print(f'Half ot the price is £{coin.half(price)}')
print(f'the price increased by {rate}% is £{coin.increase(price,rate)}')
print(f'The price with a discount of {rate}% is £{coin.decrease(price,rate)}')