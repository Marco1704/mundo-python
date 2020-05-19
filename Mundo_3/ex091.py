from random import randint
from time import sleep
from operator import itemgetter
drawn = {}
for p in range(1, 5):
    drawn[f'player {p}'] = randint(1, 6)
ranking = []
print('-=' * 10)
print('Values drawn:')
for k, v in  drawn.items():
    print(f'{k} drawn {v}')
    sleep(1)
ranking = sorted(drawn.items(), key=itemgetter(1), reverse=True)
print('-=' * 10)
print('   ========RANKING=======')
for i,v in enumerate(ranking):
    print(f'  {i+1} place: {v[0]} draw {v[1]}')
