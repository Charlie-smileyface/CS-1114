# Q2

print("Press ENTER to calculate a product or Q to quit: ")
integer_1 = int(input("Please input your first factor: "))
integer_2 = int(input("Please input your second factor: "))

while integer_1 <= 0 or integer_2 <= 0:
    print("ERROR: Positive integers must be entered.")

    print("Press ENTER to calculate a product or Q to quit: ")
    integer_1 = int(input("Please input your first factor: "))
    integer_2 = int(input("Please input your second factor: "))

product = 0

for i in range(integer_1):
    product += integer_2


print("Your product is " + str(product))
