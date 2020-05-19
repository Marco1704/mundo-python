def increase(price=0, rate=0, formt=False):
    res = (price * rate/100) + price
    return res if formt == False else coin(res)


def decrease(price=0, rate=0,formt=False):
    res = price - (price * rate/100)
    return res if formt == False else coin(res)


def double(price=0,formt=False):
    res = price * 2
    return res if formt == False else coin(res)


def half(price=0,formt=False):
    res = price / 2
    return res if formt == False else coin(res)

def coin(price=0, coin='£'):
    return f'{coin}{price:>.2f}'.replace('.',',')
