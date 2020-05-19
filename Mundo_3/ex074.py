from random import randint
numbers = (randint(1, 10),  randint(1, 10),  randint(1, 10),
      randint(1, 10),  randint(1, 10))
print(f'The numbers randomly created are: ', end='')
for n in numbers:
    print(f'{n} ',end='')
print(f'\nThe highest value is: {max(numbers)}')
print(f'The lowest number is: {min(numbers)}')