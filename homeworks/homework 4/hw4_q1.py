"""
Author: [Cheng Li]
Assignment / Part: HW4 - Q1
Date due: 2023-03-02, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""


# Q1

base = float(input("Please enter a positive integer to serve as the base: "))
while base <= 0 or base % 1 != 0:
    base = float(input("Invalid value for the base (" + str(base) + ").Please enter a positive integer to serve as the base: "))

high_power = float(input("Please enter a positive integer to serve as the highest power: "))
while high_power <= 0 or high_power % 1 != 0:
    high_power = float(input("Invalid value for the highest power (" + str(high_power) + ").Please enter a positive integer to serve as the highest power: "))

base = int(base)
high_power = int(high_power)

for power in range(high_power,-1,-1):
    if power % 2 == 0:
        result = base**power
        print(str(base) + " ^ " + str(power) + " = " + str(result))
    
