#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'one','two', 'three', 'four', 'five','six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen', 'twenty')
while True:
    number = int(input('Enter the number between 0 and 20: '))
    if 0 <= number <= 20:
        print(f'The number you entered was {cont[number]}')
    else:
        print('Invalid number, try again. ', end='')
    choice = ' '
    while choice not in 'SsNn':
        choice = str(input('\nAnother number?[S/N] ')).upper().strip()
    if choice == 'N':
        break
print('Exiting, Have a Nice Day')

