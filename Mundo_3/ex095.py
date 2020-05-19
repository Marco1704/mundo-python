team = []
player = {}
matchplay = []
while True:
    player.clear()
    player['player'] = str(input('Enter the player name: '))
    total = int(input('Number of completed matches:  '))
    matchplay.clear()
    for n in range(1, total + 1):
        matchplay.append(int(input(f'Enter the number of goals per match {n}? ')))
    player['goals'] = matchplay[:]
    player['totalgoals'] = sum(matchplay)
    team.append(player.copy())
    while True:
        opt = str(input('Another Player?[Y/N]')).upper().strip()
        if opt in 'YN':
            break
        print('Invalid Entry, please try again with Y or N.')
    if opt == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in player.keys():
    print(f' {i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(team):
    print(f' {k:>3} ', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    search = int(input('Please Enter the Player code: (999 to exit) '))
    if search == 999:
        break
    if search >= len(team):
        print('Code out of range')
    else:
        print(f'    -- Stats of Player {team[search]["player"]}:')
        for i, g in enumerate(team[search]['goals']):
            print(f'    Match {i+1} score {g} goal(s)')
        print('-' * 40)
print('<<Have a Nice Day>>')