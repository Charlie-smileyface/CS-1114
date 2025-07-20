"""
Author: [Cheng Li]
Assignment / Part: HW8 - Q5 (etc.)
Date due: 2023-04-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def get_matryoshka_list(list):
    matryoshka_list = []
    temp_list = []
    for i in range(len(list)):
        if i == 0 or list[i] > list[i-1]:
            temp_list.append(list[i])
        else:
            matryoshka_list.append(temp_list)
            temp_list = [list[i]]
    
    matryoshka_list.append(temp_list)

    return matryoshka_list
            

def main():
    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)
    print(matryoshka_list)
main()
