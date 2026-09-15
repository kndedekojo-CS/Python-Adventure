# This function lets the player drink potions.
# Each potion gives 10 health.
def drink_potions(number_of_potions, health):
    for potion in range(number_of_potions):
        health = health + 10

        # This checks that health does not go above 100.
        if health > 100:
            health = 100

        print("You drank a potion!")
        print("Your health is", health)


# This asks for the player's current health.
health = int(input("Enter your health: "))

# This asks how many potions the player wants to drink.
potions = int(input("How many potions do you want to drink? "))

# This calls the function.
drink_potions(potions, health)