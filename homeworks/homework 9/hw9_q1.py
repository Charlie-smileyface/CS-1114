"""
Author: [Cheng Li]
Assignment / Part: HW9
Date due: 2023-04-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
from pprint import pprint
def get_chord_dictionary(filepath):
    chord_dict = {}
    inner_dict = {}
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        return chord_dict
    
    file.readline()
    
    for line in file:
        line_lst = line.strip().split(',')
        root = line_lst[0]
        chord = line_lst[1]
        note = tuple(line_lst[2].split('-'))
        
        if chord not in inner_dict:
            inner_dict[chord] = note
        else:
            inner_dict = {}
            inner_dict[chord] = note
        
        if root not in chord_dict:
            chord_dict[root] = inner_dict
    file.close()

    return chord_dict

def get_possible_chords(lst_of_notes,chord_dict):
    outter_key = lst_of_notes[0]
    inner_dict = chord_dict[outter_key]
    output_lst = []
    values = list(inner_dict.items())
    for key,value in values:
        count = 0
        for element in lst_of_notes:
            if element in value:
                count +=1
        if count == len(lst_of_notes):
            output_lst.append(outter_key + key)
    output_lst = tuple(output_lst)
    return output_lst

def get_chord_progression(filepath_1, filepath_2):
    output_lst = []
    try:
        file_obj = open(filepath_1,'r')
    except FileNotFoundError:
        return output_lst 
    
    for line in file_obj:
        line_lst = line.strip().split(',')
        while "" in line_lst: ## !!
            line_lst.remove("")
            
        chord_dictionary = get_chord_dictionary(filepath_2)
        possible_chord_tuple = get_possible_chords(line_lst, chord_dictionary)
        output_lst.append(possible_chord_tuple)
    
    file_obj.close()
    return output_lst

def write_prograssion_file(progression_lst):
    file_w = open("progression_file.csv",'w')
    for element in progression_lst:
        line = ",".join(element)
        print(line, file = file_w)
    file_w.close()

def main():
    chord_progression = get_chord_progression("homeworks\homework 9\progression.csv", "homeworks\homework 9\chords-normalised.csv")
    write_prograssion_file(chord_progression)
main()

