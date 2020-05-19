from time import sleep
c = ('\033[m',          # 0 no colors
     '\033[0;30;41m',   # 1 - red
     '\033[0;30;42m',   # 2 - green
     '\033[0;30;43m',   # 3 - yellow
     '\033[0;30;44m',   # 4 - blue
     '\033[0;30;45m',   # 5 - purple
     '\033[7;30m'       # 6 - white
     );


def wizard(comm):
    title(f'Accessing the information about \' {command} \'', 4)
    print(c[6], end='')
    help(command)
    print(c[0], end='')
    sleep(2)


def title(msg,col=0):
    tam = len(msg) + 4
    print(c[col], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


command = ''
while True:
    title('Help System Pyhelp', 2)
    command = str(input('Function or Library >'))
    if command.upper() == 'END':
        break
    else:
        wizard(command)
title('See you soon!', 4)