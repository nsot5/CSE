import random
import string
print(list(string.ascii_letters))
print(list(string.digits))
print(list(string.punctuation))
word_bank = ["tissue box","computer","cellphone","table","chair","books","doors","keyboard","backpacks","watch",
             "chargers","pencil","paper","clocks"]
guess_word = random.choice(word_bank)
print(guess_word)
turns_left = 8
print("You have %s total turn to start with." % turns_left)
letters_guessed = []

while turns_left > 0:
    current_guess = input("Type in a letter: ")
    letters_guessed.append(current_guess)
    print(letters_guessed)
