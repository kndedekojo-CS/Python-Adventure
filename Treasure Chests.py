#This function opens chests using a for loop. Each chest gives 10 gold.
def collect_gold(number_of_chests):
    for chest in range(number_of_chests):
        print("You found 10 gold!")

# This asks how many chests to open.
chests = int(input("How many chests do you want to open? "))

# This calls the function.
collect_gold(chests)