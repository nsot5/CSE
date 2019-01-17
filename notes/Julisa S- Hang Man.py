import random
import string
print(list(string.ascii_letters))
print(list(string.digits))
print(list(string.punctuation))
word_bank = ["tissue box","computer","cellphone","table","chair","books","doors","keyboard","backpacks","watch",
             "chargers","pencil","paper","clocks"]

guess_word = random.choice(word_bank)
print(guess_word)
total_turn = 8
print("You have %s total turn to start with." % total_turn)

while total_turn > 0:
    if word_bank < guess_word:
