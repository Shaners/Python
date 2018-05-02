import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

for guessCount in range(1, 7):
    print("Take a guess.")
    guess = int(input('> '))

    if guess < secretNumber:
        print("Your guess was lower than my number.")
    elif guess > secretNumber:
        print("Your guess was higher than my number.")
    else:
        break # Player has won

    print(f"You have {6 - guessCount} guesses left.")

if guess == secretNumber:
    print(f"Congratulations! You won by guessing my number in {guessCount} guesses!")
else:
    print(f"You've lost by running out of guesses. My number was {secretNumber}.")