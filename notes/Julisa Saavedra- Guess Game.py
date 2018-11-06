# Random numbers
import random
a = (random.randint(0, 10))
random_guess = int(input("guess the number between 0 and 10."))
while a !="random_guess:":
    if random_guess < a:
        print("The number is lower.")
        random_guess = int(input("Guess again."))
    elif random_guess > a:
        print("Your number was to high.")
        random_guess = int(input("Guess again."))
    else:
        print("You got it!")
        break