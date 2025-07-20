def get_last_char(filename):
    try:
        file = open(filename,'r')
    except FileNotFoundError:
        last_char = ""
        return last_char
    
    for letter in file:
        last_char = letter
    return last_char

def alphabet_soup(filename):
    last_char = get_last_char(filename)
    
    if last_char == "":
        w_file = open(filename,'w')       
        for i in range(26):
            idx = ord("a") + i
            letter = chr(idx)
            print(letter, file = w_file)
    else:
        a_file = open(filename,'a')
        print("",file = a_file)
        start_idx = ord(last_char)
        end_idx = ord("z")
        for i in range(start_idx + 1, end_idx + 1):
            letter = chr(i)
            print(letter, file = a_file)

def main():
    alphabet_soup("lab\lab_9\salphabet.txt")
main()