"""
Author: [Cheng Li]
Assignment / Part: HW5 - Q3 (etc.)
Date due: 2023-03-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


user_input = input("Please enter a string of lowercase letters: ")

index = 1

while index < len(user_input) and ord(user_input[index]) < ord(user_input[index-1]):
    index += 1
    
if index == len(user_input):
    print(f"{user_input} is decreasing")

else:
    print(f"{user_input} is not decreasing")
    print(f"It stopped being lexicographically decreasing at location {index}")
