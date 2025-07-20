def consecutive_number(filename,n):
    w_file = open(filename,'w')
    for i in range(1, n+1):
        print(i,file = w_file)
    

def main():
    consecutive_number("numbers.txt", 5)
main()