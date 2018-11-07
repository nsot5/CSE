# Random numbers
import random
number = random.randint(0, 10)
random_guess = int(input("guess the number between 0 and 10."))
guesses_left = 5
win = False
while guesses_left > 0 and not win:
    if random_guess < number:
        print("The number is lower.")
        random_guess = int(input("Guess again."))
        guesses_left -= 1
    elif random_guess > number:
        print("Your number was to high.")
        random_guess = int(input("Guess again."))
        guesses_left -= 1
    elif random_guess == number:
        print("You got it!")



