import random

roll_again = True

while roll_again:
    print("Rolling the dice...")
    dice_roll = random.randint(1,6)
    print("You rolled a", dice_roll)

    roll_again_input = input("Would you like to roll again? (yes/no): ")
    if roll_again_input.lower() == "no":
        roll_again = False

print("Thanks for playing!")
