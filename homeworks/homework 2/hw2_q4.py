"""
Author: [Cheng Li]
Assignment / Part: HW2 - Q4
Date due: 2023-02-16, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q4
import random

# define inputs
level = int(input("What is this Pokémon's level? "))
speed = int(input("What is this Pokémon's speed? "))

random_num = random.randrange(0,256)
threshold = (speed/2)

# if statements
if random_num < threshold:
    multiplier = round((2*level+6) / (level+6),2)
else:
    multiplier = 1

# display
print("The Pokémon's move will be " + str(multiplier) + "x stronger!")
