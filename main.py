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

if minimum_driving_age >= drivers_age:
    print("You are legally able to drive!")
else:
    print("You are not old enough to drive yet.")