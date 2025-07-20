## Q5

num_of_value = int(input("Please enter how many positive values you want to consider: "))

print("Enter your values: ")

max_value = 0  #因为无法在loop 结束后来直接比较大小，所以只能体检设定好一个最大值，然后在loop中让输出值，和比较值相比，大的那个作为新的最大值，用于下一次循环时继续比较

if num_of_value <= 0:
    print("Invalid input.")
else:
    for i in range(num_of_value):
        value = float(input( ))
        if value >=  max_value: ## 如果value的值大于以前设定号的max value，则给 max value 附上这个新的最大值，这样在每一轮循环中都进行了比较，能始终确保max value 是所有输入值中最大的
            max_value = value

print("The largest of these values is",max_value) 
