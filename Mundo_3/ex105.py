def grades( * n, sit=False):
    r = {}
    r['total'] = len(n)
    r['highest'] = max(n)
    r['lowest'] = min(n)
    r['average'] = sum(n)/len(n)
    if sit:
        if r['average'] >= 7:
            r['situation'] = 'Pass'
        elif r['average:'] >= 5:
            r['situation'] = 'Summer School'
        else:
            r['situation'] = 'Not Pass'
    return r



resp = grades(5.5,2.5,1.5, sit=True)
print(resp)