# Q1
lst1 = [2**num for num in range(8)]
print(lst1)

# Q2
lst2 = [num for num in range(9) if num % 2 == 0]
print(lst2)

# Q3
dict3 = {num : num ** 2 for num in range(26) if num % 5 == 0}
print(dict3)

# Q4
dict4 = {num : [num * i for i in range(1,5)] for num in range(5,9)} # comprehension 套 comprehension 也是和正常loop 一样，先进外面的loop，再进内部的loop
print(dict4) 