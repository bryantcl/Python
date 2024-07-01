print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at a crossroad, where to you want to go? Type "left" or "right".')
if direction == "left":
    swimOrWait = input("Swim or Wait? ")
    if swimOrWait == "Wait":
        whichDoor = input("Which door? Red, Blue, Yellow, or Any other door? ")
        if whichDoor == "Yellow":
            print("You Win!")
        elif whichDoor == "Red":
            print("Burned by fire.")
            print("Game Over.")
        elif whichDoor == "Blue":
            print("Eaten by beasts.")
            print("Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by troute.")
        print("Game Over.")
else:
    print("Fall into a hole.")
    print("Game Over.")