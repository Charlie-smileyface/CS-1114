## Q4
# define inputs
num_1 = float(input("Enter your first number: "))
operator = input("Enter the operation (+, -, *, /): ")
num_2 = float(input("Enter your second number: "))

# if statements
if operator == '/':
    if num_2 == 0:
        result = None
    else:
        result = num_1/num_2
elif operator == '+':
    result = num_1 + num_2
elif operator == '-':
    result = num_1 - num_2
elif operator == '*':
    result = num_1 * num_2
else:
    result = None

# another if statement
if result == None:
    print(num_1, operator, num_2," is an invalid operation")
else:
    print(num_1, operator, num_2, " = ", result)
