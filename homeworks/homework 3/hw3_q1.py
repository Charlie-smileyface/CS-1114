"""
Author: [Cheng Li]
Assignment / Part: HW3 - Q1
Date due: 2023-02-23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

## Q1
import math

a = float(input("Please enter value of a: "))
b = float(input("Please enter value of b: "))
c = float(input("Please enter value of c: "))



if a == 0 and b == 0 and c == 0:
    print("Infinite number of solutions.")

elif a == 0 and (b != 0 or c != 0):
    print("No solution.")

elif b**2 - 4*a*c < 0:
    print("No real solution.")

elif b**2 - 4*a*c == 0:
    solution = -b/(2*a)
    print("This equation has 1 solution: x =",solution)

else:
    solution1 = (-b + math.pow(b**2 - 4*a*c,0.5))/(2*a)
    solution2 = (-b - math.pow(b**2 - 4*a*c,0.5))/(2*a)
    print("This equation have 2 solutions: x =",solution1,"and x =",solution2)
