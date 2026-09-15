# This function fights the castle guardian.
def fight_guardian(guardian_health):
    while guardian_health > 0:
        print("You attacked the guardian!")
        guardian_health = guardian_health - 10

        # This checks if the guardian is defeated.
        if guardian_health <= 0:
            print("The guardian has been defeated!")


# This asks for the guardian's health.
guardian_health = int(input("Enter the guardian's health: "))

# This calls the function.
fight_guardian(guardian_health)