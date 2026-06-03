print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYou are at a cross road, where would you like to go? ")
cross_road=input("Left or Right?\n")
if cross_road=="Left":
    print("You have come to a lake.There is and island in the middle of the lake")
    left_island=input("Type 'wait' to wait for a boat.Type 'swim' to swim across.\n")
    if left_island=="wait":
        print("You arrived at the island unharmed.There is a house with 3 doors.")
        door=input("One red, one yellow and one blue.Which one do you choose?\n")
        if door=="red":
            print("Game over. You lost!")
        elif door=="yellow":
            print("Congratulations you found the Treasure!")
        else:
            print("Game over. You lost!")
    else:
        print("You were attacked by a shark.You died!")
else:
    print("You fell off from a mountain.You died!")
