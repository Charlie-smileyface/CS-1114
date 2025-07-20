"""
Author: [Cheng Li]
Assignment / Part: HW7 - Q2 (etc.)
Date due: 2023-04-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import math

def get_root_of_average(filepath, root = 2):
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        print(f"WARNING: the file {filepath} does not exist")
        return 0
    
    line = file.readline().strip()
    line += " "
    index1 = 0
    acc = 0
    counter = 0
    for i in range(len(line)):
        if line[i] == " ":
            element = line[index1:i]
            index1 = i
            try:
                element = float(element)
            except ValueError:
                print(f"WARNING: Could not cast '{element}' into a float.")
            else:
                acc += element
                counter += 1
    file.close()
    
    if counter == 0:
        result = 0
    else:
        average = acc / counter
        result = math.pow(average,1/root)
    
    return result

def main():
    cubed_root = get_root_of_average("homeworks\homework 7\q2numbers.txt",3)
    print(cubed_root)
main()