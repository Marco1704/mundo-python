def increase(price=0, rate=0, formt=False):
    res = (price * rate / 100) + price
    return res if formt == False else coin(res)


def decrease(price=0, rate=0, formt=False):
    res = price - (price * rate / 100)
    return res if formt == False else coin(res)


def double(price=0, formt=False):
    res = price * 2
    return res if formt == False else coin(res)


def half(price=0, formt=False):
    res = price / 2
    return res if formt == False else coin(res)


def coin(price=0, coin='£'):
    return f'{coin}{price:>.2f}'.replace('.', ',')


def summary(price=0, ratei=10,rated=5):
    print('-' * 50)
    print('Value Summary'.center(50))
    print('-' * 50)
    print(f'Price Analysis:\t{coin(price)}')
    print(f'Price Double: \t{double(price,True)}')
    print(f'Half Price: \t{half(price,True)}')
    print(f'{ratei}% Increase: \t{increase(price,ratei,True)}')
    print(f'{rated}% Discount: \t{decrease(price,rated,True)} ')
    print('-' * 50)