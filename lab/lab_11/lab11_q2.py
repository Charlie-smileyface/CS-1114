my_dict = {"a": 15 , "c": 35 , "b": 20}
print(list(my_dict.keys()))
print(list(my_dict.values()))
print(my_dict.items())

lst = list(my_dict.items())
lst.sort() ## 在这里不能给这个改变后的list 赋值，不然print 不出来，print的新的list 是 None
print(lst)