import random

money = 15
most_money = money
while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        money += 4
        if money > most_money:
            most_money = money
    elif dice1 + dice2 > 7:
        money -= 1
    else:  # Lower than 7
        money -= 1
    print("Next Round:")
    print("The first dice is a %d" % dice1)
    print("The second dice is a %d" % dice2)
    print()
    print("You played 40 rounds")
    print()