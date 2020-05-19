num = int(input('Enter a number between 0 and 9999: '))
u = num//1 % 10
d = num//10%10
c = num//100%10
m = num//1000%10
print(f'The first part of the number is {u} \nThe second part of the number is {d} \nThe third part of the number is {c}'
      f'\nThe fourht part of the number is {m}')


