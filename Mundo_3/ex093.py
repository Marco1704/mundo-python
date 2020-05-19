stats = {}
score = []
stats['player'] = str(input('Enter the player name: '))
stats['match']  = int(input('Number of completed matches:  '))
for n in range(1,stats['match']+1):
   score.append(int(input(f'Enter the number of goals per match {n}? ')))
   stats['goals'] = score[:]
   stats['totalgoals'] = sum(score)
print(stats)
print('-=' * 30)
for k, v in stats.items():
    print(f'The field {k} has the value {v}')
print('-=' * 30)
print(f'{stats["player"].capitalize()} played {stats["match"]} matches '
      f'this season and score a total of {stats["totalgoals"]} goals')
for i, v in enumerate(stats['goals']):
    print(f'    => Match {i+1}, he score {v} goals')