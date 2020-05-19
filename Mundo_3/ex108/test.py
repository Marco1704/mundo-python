import coin



price = float(input('Enter the price: £ '))
rate = 10
print(f'The double of {coin.coin(price)} is {coin.coin(coin.double(price))}')
print(f'Half of {coin.coin(price)} is {coin.coin(coin.half(price))}')
print(f'the price increased by {rate}% is {coin.coin(coin.increase(price,rate))}')
print(f'The price with a discount of {rate}% is {coin.coin(coin.decrease(price,rate))}')