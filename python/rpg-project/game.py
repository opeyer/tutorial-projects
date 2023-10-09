# RPG Project
# Pre-alpha version
# by Otto William Peyer IV

# Imports
import random

# Header
print("RPG Project by opeyer")

# Need to make start menu function here

# Scenes
def scene1():
    print("Chapter One")
    print("BREAKFAST")
    print("You stroll into the convenience store.")
    print("Amidst the hustle and bustle of various non-descript persons, you pace down the aisles, looking for a fix of something.")
    print("After all, the first meal of the day can really change things...")
    print("What? It's an important decision!")
    print("Don't look at me like that...")

    print("Anyway, what'll it be?")
    print("(Type the corresponding number and press ENTER to make a decision.)")

    print("1: Do you even have to ask? Flae's Brown Sugar Sweet Potato Chips, all the way baby.")
    print("2: Have yourself a nice, chocolatey Twigs bar.")
    print("3: I'll just have a Coke.")

    foodChoice = input("What would you like to eat? ")

    foodChoice = int(foodChoice)

    if foodChoice == 1:
        print("You walk up to the counter and smile at the attendent, a somewhat sour looking girl with freckles and dyed blue hair.")
        print("With a bit of resigned annoyance in her voice, she sighs out, 'Flae's? Will that be all, sir?'")
        print("You pay the girl and walk out, back onto the street.")
    elif foodChoice == 2:
        print("You walk up to the counter and smile at the attendent, a somewhat sour looking girl with freckles and dyed blue hair.")
        print("With a bit of resigned annoyance in her voice, she sighs out, 'Twigs? That all?'")
        print("You pay the girl and walk out, back onto the street.")
        print("As you step out, you hear her mutter under her breath, 'Gross!'")
        print("Ouch...")
    elif foodChoice == 3:
        print("You walk up to the counter and smile at the attendent, a somewhat sour looking girl with freckles and dyed blue hair.")
        print("'Coke. Didn't take you for the type.'")
        print("A bit offended, you stammer back, 'And what type would that be?'")
        print("But she just smirks...")
        print("You pay the girl and walk out, back onto the street.")

    if foodChoice == 1:
        print("Under construction...")
    elif foodChoice == 2:
        print("Under construction...")
    elif foodChoice == 3:
        appetite = [1, 2]
        print("After that little burst of rudeness, you walk for a time collecting your thoughts.")
        print("[RANDOM ROLL INITIATED]")
        print("(In the world of RPG PROJECT, you will occasionally come up against random rolls which will determine various things that happen. In this case, it will decide whether or not you still have an appetite for that thar sody pop you got...)")
        appetiteChoice = random.choice(appetite)
        print("You rolled a", appetiteChoice, "!")
        appetiteChoice = int(appetiteChoice)
        if appetiteChoice == 1:
            print("Thankfully, nothing seems to be keeping you down. You unscrew the Coke and take a sip. Ahh!!! Refreshing!")
        elif appetiteChoice == 2:
            print("You don't really have much of an appetite anymore. You drop the Coke off into a bin. RIP.")

# Call
scene1()