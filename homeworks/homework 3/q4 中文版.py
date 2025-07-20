"""
Author: [Your name here]
Assignment / Part: HW3 - Q1 (etc.)
Date due: 2023-02-23, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

## Q4
postive_integer = int(input("Please enter a postive integer: "))

for i in range(1,postive_integer + 1):

    number = i  ## 后面需要用到这个数来进行降 digits 的运算，但是又不想改变本身 for loop 中的值，所以在这里再构建一个variable number,而其初始值和 i 一样 
    even_count = 0
    odd_count = 0

    while number > 0:   ##这里套用while loop是因为不知道每一次处理的数字有几个 digits 所以只能用while loop 来判断每一位 digit 是奇还是偶
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
        number //= 10  ## 每次运行到这里通过 //10 来去掉刚刚判断过的末尾的 digit,然后进入新的循环再次判断，e.g 105//10 = 10

    if even_count > odd_count:
        print(i,end = " ")  ## end 用来把东西这一行的东西和下一行连起来，也就是从列写成行 ("\n"代表换下一行写，也就等于不用end)
                            ## ("\t" 代表把一列东西换成一行写，每一个之间中间空一个较大的空格）
                            ## (end = " " 代表把这一行和下一行写成一行，而用引号中间的东西连接起来，来这里是用空格连接）
