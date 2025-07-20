"""
Author: [Cheng Li]
Assignment / Part: HW2 - Q5
Date due: 2023-02-16, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q5
# define input
user_xp = float(input("Enter this user's current XP: "))

if user_xp <= 15.0:
    level = 1
elif user_xp <= 24.9:
    level = 2
elif user_xp <= 29.9:
    level = 3
elif user_xp <= 39.9:
    level = 4
elif user_xp <= 60:
    level = 5
else:
    level = None


if level == None:
    print("Please enter a valid XP value.")
else:
    print("Level " + str(level) + " player (XP: " + str(user_xp) + ")")
