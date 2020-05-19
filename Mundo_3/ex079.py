# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numbers = []
while True:
    n = int(input('Enter the number: '))
    if n not in numbers:
        numbers.append(n)
        print('Value has been added')
    else:
        print('duplicated value, not added')
    opt = str(input('Another entry: [Y/N] ')).upper().strip()
    if opt == 'N':
            break
numbers.sort()
print(f'You entered the following {numbers}')