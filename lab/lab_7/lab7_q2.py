## Q2
# A.
user_input = input("Enter your phrase: ")
print(user_input[len(user_input)::-1])

#B.
user_input2 = input("Enter your phrase: ")
line = ''
for i in range(len(user_input2)-1,-1,-1): ## range()当中是可以可以规定范围和变成倒序的
                                          ## 这里要用 len -1是因为一个str[index]的最后以为对应的序号是 len(str)-1
    letter = user_input2[i]
    line += letter

print(line)
