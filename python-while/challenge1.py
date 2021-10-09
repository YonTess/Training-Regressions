import random

value = random.randint(1, 5)
guess = 0
count = 0

while guess != value:
    count += 1
    guess = input('Guess a number between 1 and 5:  ')
    if guess.isnumeric():
        guess = int(guess)
else:
    print(f'You guessed it in {count} times!')
