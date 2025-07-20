"""
Author: [Cheng Li]
Assignment / Part: HW8 - Q1 (etc.)
Date due: 2023-04-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def update_frequencies(old,new):
    a_count, c_count, t_count, g_count = 0,0,0,0
    for letter in new:
        if letter == 'A':
            a_count += 1
        elif letter == 'C':
            c_count += 1
        elif letter == 'T':
            t_count += 1
        elif letter == 'G':
            g_count += 1
    total_count_a, total_count_c, total_count_t, total_count_g = old[0][1] + a_count, old[1][1] + c_count, old[2][1] + t_count, old[3][1] + g_count
    new_frequencies = [("A", total_count_a), ("C", total_count_c), ("T", total_count_t), ("G", total_count_g)]
    return f"Number of nucleotides added: A -> {a_count} | C -> {c_count} | T -> {t_count} | G -> {g_count} \n {new_frequencies}"
    
def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print(new_frequencies)
main()