"""
Author: [Cheng Li]
Assignment / Part: HW3 - Q3
Date due: 2023-02-23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
## Q3
column = int(input("Please enter a positive integer: "))

print("+" + column * "-" + "+")

for i in range(1,column + 1):

    row = "|"

    for j in range(i,0,-1): 
        row += str(j)
        
        
    row += (column - i)*" "
    row += "|"

    print(row)
    
print("+" + column * "-" + "+")
