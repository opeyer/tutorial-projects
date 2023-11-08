dndPerm = 0
filmcruPerm = 1
modPerm = 1
task = "nothing"

def acceptInput():
    print("D&D Bot")
    mainCommand, subCommand = input('>').split()
    checkInput(mainCommand, subCommand)

def checkInput(mainCommand, subCommand):
    if mainCommand == "!perm":
        if subCommand == "D&D":
            print(checkPermissions(dndPerm))
        elif subCommand == "filmcru":
            print(checkPermissions(filmcruPerm))
        else:
            print("What group are you checking permissions for?")
    else:
        print("I don't know what you're trying to tell me.")

def checkPermissions(groupName):
    if groupName == 0:
        return "I'm sorry, you don't have the necessary permission for that! Message tomoko with what you're trying to do."
    else:
        return "Pass"

def setPermissions(groupName):
    if modPerm == 1:
        print("What?")
    else:
        print("You don't have permissions to do that! what are you trying to do, destroy the world? I won't let you...")

acceptInput()

