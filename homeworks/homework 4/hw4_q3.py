"""
Author: [Cheng Li]
Assignment / Part: HW4 - Q3
Date due: 2023-03-02, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.

"""
# Q3
num_player = int(input("How many players played this round? "))

while num_player <=0:
    num_player = int(input("Invalid input. How many players played this round? "))

max_player = 0
max_value = 0

for player in range(1,num_player+1):
    user_input = input("Enter the value of a property/asset, or DONE to finish: ")
    value = 0

    while user_input != "DONE":
        value += float(user_input)
        user_input = input("Enter the value of a property/asset, or DONE to finish: ")

    print("player",player,"has",round(value,2),"dollars.")

    if value >= max_value:
        max_value = value
        max_player = player

print("Congradulations, " + str(max_player) + "! You win with $" + str(max_value) + "!")
