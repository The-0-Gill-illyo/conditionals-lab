import random

# Conditional Tasks

# Task 1: Driving Age

# Declare a variable and assign it the value of the legal driving age in the United States.
# Declare a variable to store a user's age. Use the built-in Python input() function to retrieve
# the user’s age via user input.
# If the user’s age is greater than or equal to the legal driving age in the United States, then
# print to the console “You are legally able to drive.”
# If the user’s age is less than the legal driving age in the United States, print to the console
# “You are not old enough to drive yet.”

minimum_driving_age = "16"

drivers_age = input("Please enter your age. ")

if drivers_age >= minimum_driving_age:
    print("You are legally able to drive!")
else:
    print("You are not old enough to drive yet.")
    
# Task 2: Random Number

# Declare a variable to store a random number between 0 and 10. 
# You will need to do some research to determine how to generate a random number in Python.
# A good search term to use: “random number Python”
# If the number is between 0 and 2, print to the console “0 or 1 or 2”
# If the number is between 3 and 5, print to the console “3 or 4 or 5”
# If the number is between 6 and 8, print to the console “6 or 7 or 8”
# If the number is equal to 9 or 10, print to the console “9 or 10”

random_number = random.randint(0, 10)

if random_number == random.randint(0, 2):
    print("0 or 1 or 2")
elif random_number == random.randint(3, 5):
    print("3 or 4 or 5")
elif random_number == random.randint(6, 8):
    print("6 or 7 or 8")
else:
    print("9 or 10")