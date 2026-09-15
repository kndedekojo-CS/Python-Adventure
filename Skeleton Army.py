
# This function fights skeletons using a for loop.
def fight_skeletons(number_of_skeletons):
    for skeleton in range(number_of_skeletons):
        print("You defeated a skeleton!")

# This asks how many skeletons to fight.
skeletons = int(input("How many skeletons are attacking? "))

# This calls the function.
fight_skeletons(skeletons)