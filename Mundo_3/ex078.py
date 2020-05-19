#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
values = []
hig = 0
low = 0
for c in range(0, 5):
    values.append(int(input(f'Enter a value to the position {c}: ')))
    if c == 0:
        hig = low = values[c]
    else:
        if values[c] > hig:
            hig = values[c]
        if values[c] < low:
            low = values[c]
print(f'You entered the following numbers: {values}')
print(f'The higher value is {hig} in the position(s): ', end='')
for i, v in enumerate(values):
    if v == hig:
        print(f'{i}...', end='')
print(f'\nThe lowest value is {low} in the position(s): ', end='')
for i, v in enumerate(values):
    if v == low:
        print(f'{i}...', end='')




