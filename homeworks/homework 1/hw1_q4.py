"""
Author: [Cheng Li]
Assignment / Part: HW1 - Q4 
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Q4
print("Please enter your amount of dollars and cents, in two seprate lines.")

dollars = int(input( ))
cents = int(input( ))

dollars_cents = dollars*100
total_cents = dollars_cents + cents

quarters = total_cents // 25
dimes = (total_cents % 25) // 10
nickels = (total_cents % 25 % 10) //5
pennies = total_cents % 25 % 10 % 5

print(str(dollars) + " dollars and " + str(cents) + " cents are: " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(nickels) + " nickels and " + str(pennies) + " pennies")
