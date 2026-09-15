#This function picks a weapon.
def choose_weapon(weapon):
    if weapon == "sword":
        print("You have equiped a sword!")
    elif weapon == "bow":
        print("You have equiped a bow!")
    elif weapon == "staff":
        print("You have equiped a staff!")
    else:
        print("That is not a valid weapon!")

# This asks the user to choose a weapon.
weapon = input("Choose a weapon (sword, bow, staff): ")

# This calls the function.
choose_weapon(weapon)