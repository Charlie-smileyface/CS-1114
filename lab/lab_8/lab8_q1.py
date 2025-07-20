## Q1
'''
def mystery(num, string):
    secret = ""
    for char in string:
        secret += char * num
    return secret

def main():
 print(mystery(5, "hello"))
main()
'''

#output >> hhhhheeeeellllllllllooooo



def func_one(val):
    num = 10
    if val % 3 == 0:
        print(num)
        print("whoop")
        return True

def func_two(num):
    while num < 20:
        if func_one(num):
            print(num)
        num += 1
    print(num)

def main():
    func_two(13)
main()

#output >> 10 whoop 15 10 whoop 18 20
