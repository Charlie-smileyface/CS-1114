"""
Author: [Cheng Li]
Assignment / Part: HW7 - Q1 (etc.)
Date due: 2023-04-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def get_word_count(filepath):
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        print(f"WARNING: file {filepath} does not exist")
        return 0
    
    total_count = 0
    for line in file:
        word_count = 1
        line = line.strip()
        for letter in line:
            if letter == " ":
                word_count += 1
        
        total_count += word_count
    
    file.close()
    return total_count

def main():
    count =  get_word_count("homeworks\homework 7\svoltaire.txt")
    print(f"This file has {count} word(s).")
main()