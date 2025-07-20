print([3*5] + [4, 7])

num_lst = [1,57,15]
num_lst[2] = 25
print(num_lst*3)

str_lst = ["good", "better"]
str_lst.append("best")
print(str_lst)
str_lst.pop()
str_lst += str_lst
print(str_lst[::2])

lst = []
for i in range(3):
    lst.append(i**2)
print(lst)

my_lst = []
for i in range(3,6):
    for k in range(2):
        my_lst.append(i + k)
print(my_lst)