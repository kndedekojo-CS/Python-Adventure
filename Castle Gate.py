#This function checks if the level is high enough to open the gate.
def check_level(level):
    if level >= 5:
        print("The gate opens!")
    else:
        print("You are not strong enough!")

# This asks the user for their level.
level = int(input("Enter your level: "))

# This calls the function.
check_level(level)