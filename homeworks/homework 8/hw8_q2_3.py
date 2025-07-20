"""
Author: [Cheng Li]
Assignment / Part: HW8 - Q2, Q3 (etc.)
Date due: 2023-04-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
def is_haiku(string):
    line = string.split('/')
    if len(line) == 3:
        line1 = line[0].split(',')
        line2 = line[1].split(',')
        line3 = line[2].split(',')
        if len(line1) == 5:
            if len(line2) == 7:
                if len(line3) == 5:
                    return True
                else:
                    print("WARNING: The third line is not 5 syllables long.")
                    return False
            else:
                print("WARNING: The second line is not 7 syllables long.")
                return False
        else:
            print("WARNING: The first line is not 5 syllables long.")
            return False                            

    else:
        print("WARNING: This is not three lines")
        return False

def haiku_string_parser(string):
    haiku = is_haiku(string)
    if haiku == True:
        remove_comma_haiku = "".join(string.split(','))
        formatted_haiku = "\n".join(remove_comma_haiku.split('/'))
        return formatted_haiku
    else:
        return ""

def main():
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)
main()
