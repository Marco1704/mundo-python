def stats(x = '<unknown>', y = 0):
    print(f'The player {x} has scored {y} goals so far on this season')


n = str(input('Enter the player name:'))
g = str(input('Number of goals: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    stats(y=g)
else:
    stats(n, g)




