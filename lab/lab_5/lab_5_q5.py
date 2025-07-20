## Q5

width = int(input("Python needs to tell you a secret. How many characters wide can its message be? "))

for row in range(1,width+1):  ## X 部分，这里都用的是1到width+1 是因为后面的if中要使用相关的数学运算
    result = ''
    for column in range(1,width+1):
        if row == column:
            result += "X"
        elif row + column == width+1:
            result += "X"
        else:
            result += " "

    print(result)


for row in range(1,width+1):  ## O 部分
    result = ''
    for column in range(1,width+1):
        if row == 1:
            result = " " + (width-2)*"O" + " "
        elif row == width:
            result = " " + (width-2)*"O" + " "
        else:
            result = "O" + (width-2)*" " + "O"

    print(result)


for row in range(1,width+1):  ## 第二个 X 部分,和第一个相同
    result = ''
    for column in range(1,width+1):
        if row == column:
            result += "X"
        elif row + column == width+1:
            result += "X"
        else:
            result += " "

    print(result)
