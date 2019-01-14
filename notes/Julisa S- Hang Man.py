import random
word_bank = ["tissue box","computer","cellphone","table","chair","books","doors","keyboard","backpacks","watch",
             "chargers","pencil","paper","clocks"]
valid_characters = ["a,""b,""c,""d,""e,""f,""g,""h,""i,""j,""k,""l,""m,""n,""o,""p,""q,""r,""s,""t,""u,""v,""w,""x,""y,"
                    "z"]
print("You have 26 %s characters to choose from." % valid_characters)
guess_word = random.choice(word_bank)
print(guess_word)
total_turn = 8
print("You have %s total turn to start with." % total_turn)

