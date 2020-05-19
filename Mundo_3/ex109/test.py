import coin



price = float(input('Enter the price: £ '))
rate = 10
print(f'The double of {coin.coin(price)} is {coin.double(price,True)}')
print(f'Half of {coin.coin(price)} is {coin.half(price, True)}')
print(f'the price increased by 10% is {coin.increase(price,10, True)}')
print(f'The price with a discount of 13% is {coin.decrease(price, 13, True)}')