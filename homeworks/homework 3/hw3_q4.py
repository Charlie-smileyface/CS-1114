"""
Author: [Cheng Li]
Assignment / Part: HW3 - Q4
Date due: 2023-02-23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

## Q4
postive_integer = int(input("Please enter a postive integer: "))

for i in range(1,postive_integer + 1):

    number = i   
    even_count = 0
    odd_count = 0

    while number > 0:   
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
        number //= 10  

    if even_count > odd_count:
        print(i,end = " ")  
