"""
Author: [Cheng Li]
Assignment / Part: HW5 - Q2 (etc.)
Date due: 2023-03-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

dna_1 = input("Enter a DNA sequence: ")
dna_2 = input("Enter a second DNA sequence: ")

dna_1_length = len(dna_1)
dna_2_length = len(dna_2)
dna_sequence = ''

if dna_1_length >= dna_2_length:
    for i in range(dna_2_length):
        letter_1 = dna_1[i]
        letter_2 = dna_2[i]

        dna_sequence += letter_1 + letter_2

    dna_sequence += dna_1[i+1:dna_1_length]

else:
    for i in range(dna_1_length):
        letter_1 = dna_1[i]
        letter_2 = dna_2[i]

        dna_sequence += letter_1 + letter_2

    dna_sequence += dna_2[i+1:dna_2_length]

fused_sequence = ''
invalid_count = 0
for i in dna_sequence:
    
    if i == "A":
        letter = "T"

    elif i == "T":
        letter = "A"

    elif i == "C":
        letter = "G"
    
    elif i == "G":
        letter = "C"

    else:
        letter = ''
        invalid_count += 1
    
    fused_sequence += letter

print("Fused sequence:",fused_sequence,"| Invalid characters:",invalid_count)
   
        
    
