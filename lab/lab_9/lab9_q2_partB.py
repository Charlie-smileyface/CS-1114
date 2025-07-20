def squared_numbers(filename, outfile):
    try:
        r_file = open(filename,'r')
    except FileNotFoundError:
        return 
    w_file = open(outfile,'w')

    for line in r_file:
        squared_line = int(line)**2
        print(squared_line, file = w_file)

def main():
    squared_num = squared_numbers("lab\lab_9\snumbers.txt", "SquaredNumbers.txt")
main()