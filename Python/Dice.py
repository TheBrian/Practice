import random as rand


def dice(sides):
    return rand.randint(1, sides)


roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    sides = int(input("What number sided die would you like to throw?: "))
    print("You rolled a: ", dice(sides))
    roll_again = input("Roll the dices again? yes/no: ")
