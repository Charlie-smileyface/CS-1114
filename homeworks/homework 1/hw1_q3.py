"""
Author: [Cheng Li]
Assignment / Part: HW1 - Q3 
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Q3
print("Please enter the number of coins:")
num_quarters = int(input("Number of quarters: "))
num_dimes = int(input("Number of dimes: "))
num_nickels = int(input("Number of nickels: "))
num_pennies = int(input("Number of pennies: "))

quarters_cents = num_quarters*25
dimes_cents = num_dimes*10
nickels_cents = num_nickels*5
pennies_cents = num_pennies

total_cents = quarters_cents + dimes_cents + nickels_cents + pennies_cents

dollars = total_cents // 100
cents = total_cents % 100

print("The total is " + str(dollars) + " dollar(s) and " + str(cents) + "cent(s)")
