"""
Author: [Cheng Li]
Assignment / Part: HW7 - Q3 (etc.)
Date due: 2023-04-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def create_error_log(sequence,filepath):
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        print("FILENOTFOUNDERROR: The file specified was not found or could not be opened.")
    report = open("homeworks\homework 7\error_log.txt", 'w')
    
    line = 0
    for number in file:
        line += 1
        index_string = number.strip()
        try:
            index_number = int(index_string)
            element = sequence[index_number]        
        except IndexError:
            print(f"INDEXERROR at LINE {line}: The value read, {index_string}, is larger than the sequence length of {len(sequence)}.", file = report)
        except ValueError:
            print(f"VALUEERROR at LINE {line}: The value read,{index_string}, cannot be casted into an integer to be used as an index.", file = report)
    file.close()
    report.close()  

def main():
    create_error_log("ACTGC AXT","homeworks\homework 7\indices.txt")
main()