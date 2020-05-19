#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa # tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.


def vote(year):
    from datetime import date
    current = date.today().year
    age = current - year
    if age < 16:
        return f'Below {age} years old are not allowed to vote'
    if age >= 18:
        return f'You are oblige to vote with {age} years old'
    if age <= 65:
        return f'{age} years old can opt out of voting in elections'


birth = int(input('Enter your birth year: '))
print(vote(birth))
