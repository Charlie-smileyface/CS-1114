"""
Author: [Cheng Li]
Assignment / Part: HW3 - Q2
Date due: 2023-02-23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q2
positive_integer = int(input("Please enter a positive integer: "))

print("Executing while-loop...")
number = 0
while number <= 2*positive_integer:
    if number % 2 == 1:
        print(number)
    number += 1



print("Executing for-loop...")
for element in range(2*positive_integer):
    if element % 2 == 1:
        print(element)
