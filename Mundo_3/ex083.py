#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Enter the formula: '))
fm = []
for simb in expr:
    if simb == '(':
        fm.append('(')
    elif simb == ')':
        if len(fm) > 0:
            fm.pop()
        else:
            fm.append(')')
if len(fm) == 0:
    print('The expression is right')
else:
    print('The expression is wrong')


