def increase(price=0, rate=0):
    res = (price * rate/100) + price
    return res


def decrease(price=0, rate=0):
    res = price - (price * rate/100)
    return res


def double(price=0):
    res = price * 2
    return res


def half(price=0):
    res = price / 2
    return res

def coin(price=0, coin='£'):
    return f'{coin}{price:>.2f}'.replace('.',',')
