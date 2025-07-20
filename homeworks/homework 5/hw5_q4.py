"""
Author: [Cheng Li]
Assignment / Part: HW5 - Q4 (etc.)
Date due: 2023-03-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

encoded_string = input("Enter an encoded string: ")
skip_key = input("Enter a key: ")

skipped_string = encoded_string[0:len(encoded_string):int(skip_key)+1]

line = ''
for i in skipped_string:
    letter = i
    if 48 <= ord(i) <= 57:
        letter = ''

    line += letter

inverse_line = line[len(line)::-1]

print(f"Your massage is '{inverse_line}'")  
