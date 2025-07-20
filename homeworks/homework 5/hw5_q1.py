"""
Author: [Cheng Li]
Assignment / Part: HW5 - Q1 (etc.)
Date due: 2023-03-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

user_input = input("Say something: ")

change_count = 0
unchange_count = 0
space_count = 0
non_alphabetic_count = 0

for i in user_input:
    if 65 <= ord(i) <= 90:
        letter = chr(ord(i) + 32)
        change_count += 1

    elif 97 <= ord(i) <= 122:
        letter = i
        unchange_count += 1

    elif ord(i) == 32:
        letter = i
        space_count += 1
        non_alphabetic_count += 1

    else:
        letter = i
        non_alphabetic_count += 1

    print(letter,end ='')

print()    
print("Number of changed letters:",change_count)
print("Number of unchanged letters:",unchange_count)
print("Number of whitespace characters:",space_count)
print("Number of non-alphabetic characters:",non_alphabetic_count)
