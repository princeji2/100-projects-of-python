print("Welcome to Treasure Island!\nYour mission is to find the treasure in this adventure game.")
print ("You are at a cave. Where do you want to go? Type 'left' or 'right'")
if input() == "left":
    print("Oops! You fell into a hole full of spikes. Game Over.")
else:
    print("That's great, you chose to go right. \nYou continue on your journey.")
    input("You see a weak bridge ahead. How do you want to cross it? Type 'run' or 'walk'")
    if input() == "run":
        print("You ran too fast and the bridge collapsed. Game Over.")
    else:
        print("You walked carefully and crossed the bridge safely. \nYou continue on your journey.")
        input("You see a river ahead. How do you want to cross it? Type 'swim' or 'wait'")
        if input() == "swim":
            print("You tried to swim across but got caught in a strong current. Game Over.")
        else:
            print("You waited patiently and a boat arrived to take you across the river. \nYou continue on your journey.")
            input("You see a haunted castle ahead. How do you want to enter it? Type 'knock' or 'open'")
            if input() == "knock":
                print("A monster opened the door and ate you. Game Over.")
            else:
                print("You opened the door and now you are inside the haunted castle.")
                input("You see three doors ahead. Which one do you want to enter? Type 'red', 'blue', or 'yellow'")
                if input() == "red":
                    print("You entered the red door and found a room full of fire. Game Over.")
                elif input() == "blue":
                    print("You entered the blue door and found a room full of blood thrusty blue monarchs. Game Over.")
                else:
                    print("Congratulations! You entered the yellow door and found the treasure. You Win!")
