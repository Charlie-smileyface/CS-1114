"""
Author: [Cheng Li]
Assignment / Part: HW4 - Q4
Date due: 2023-03-02, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q4
import turtle

user_input = int(input("Enter a postive integer representing the shape of the hylogon: "))

while user_input  <= 0:
    user_input = int(input("Invalid input! Enter a postive integer representing the shape of the hylogon: "))

    
for i in range(20):
    for j in range(user_input):
        turtle.forward(100)
        turtle.left(360/user_input)

    turtle.left(360/20)
