## Q4

number = int(input("Please enter a number: "))

a0 = 1
a1 = 1

print(a0)
print(a1)

for number in range(2,number):
    a2 = a0 + a1
    print(a2)
    a0 = a1  ## 让 a0 a1 的值在循环中进行覆盖，然后也不断在重新覆盖 a2
    a1 = a2
