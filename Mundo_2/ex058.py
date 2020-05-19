from random import randint
print('-=-' * 13)
print("Welcome, Let's Play the Guessing Game")
print('-=-' * 13)
print("I'm thinking in a number between 0 and 10.\nCan you guess which one?")
computer = randint(0,10)
countguess = 0
guess = 0
while guess != computer:
    guess = int(input("Enter your guess: "))
    countguess += 1
    if guess < computer:
        print('More... Try again')
    elif guess > computer:
        print('Less...Try again')
print(f"Congratulations, you guess right in {countguess} tries")
