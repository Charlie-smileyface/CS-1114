"""
Author: [Cheng Li]
Assignment / Part: HW2 - Q2
Date due: 2023-02-16, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q2
import math
import random

# define inputs
hp_max = int(input("Enter the max health of this Pokémon: "))

# random numbers
hp_current = random.randrange(1,hp_max+1)
ball = random.randrange(1,256)
pseudo_random_num = random.randrange(0,256)

# calculation
function = math.floor((hp_max*255*4) / (hp_current*ball))

# if statement
if function >= pseudo_random_num:
    print("You've caught the Pokémon!")

else:
    print("Oh no! The Pokémon broke free!")

