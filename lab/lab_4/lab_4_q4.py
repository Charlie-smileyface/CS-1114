## Q4

base = float(input("Please enter a positive integer to serve as the base: "))
power = float(input("Please enter a positive integer to serve as the highest power: "))

if base % 1 != 0 or power % 1 != 0: ## 先从 input 默认输入的为 float 然后再通过余数出发看除 1 看余数是否为 0 来进行筛选是否输入的为整数
    print("ERROR: Both values must be POSITIVE INTEGERS.")

elif base <= 0 or power <= 0 :
    print("ERROR: Both values must be POSITIVE INTEGERS.")

else:
    for i in range(int(power) + 1):
        result = int(base ** i)
        print(str(int(base)) + " ^ " + str(i) + " = " + str(result))
