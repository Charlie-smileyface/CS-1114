def remove_Es(msg):
    removed_msg = ""
    for i in msg:
        if i == "E" or i == "e":
            i = ""
        removed_msg += i
    return removed_msg

def remove_Es_new_file(filename):
    try:
        r_file = open(filename,'r')
    except FileNotFoundError:
        return False
    
    w_file = open("removed_Es.txt",'w')
    for line in r_file:
        line = line.strip()
        removed_line = remove_Es(line)
        print(removed_line, file = w_file)
    return True

def remove_Es_same_file(filename):
    try:
        a_file = open(filename, 'a')
    except FileNotFoundError:
        return False
    print("", file = a_file)
    r_file = open(filename, 'r')
    for line in r_file:
        line = line.strip()
        removed_line = remove_Es(line)
        print(removed_line, file = a_file)
    return True

def main():
    remove_Es_new_file("lab\lab_9\evil_es_msg.txt")
    remove_Es_same_file("lab\lab_9\evil_es_copy.txt")
main()