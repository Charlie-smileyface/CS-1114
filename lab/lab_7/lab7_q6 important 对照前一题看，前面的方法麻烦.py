## Q6
massage = input("Please enter your massage: ")
print(massage)
massage += " " #用来保证massage 的最后一个字符是空格这样方便后面一个个筛选单词，对照上一题看，上一题方法麻烦

start = 0
secret = ''
for i in range(len(massage)):
    if massage[i] == " ":
        part = massage[start:i]

        if part[0].isupper() and part[1:].islower():
            secret += part[0]

        start = i+1


print(f"Your secret massafe is {secret}.")
