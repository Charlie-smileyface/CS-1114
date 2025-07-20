my_str = input("Enter a string: ")
length = len(my_str)

print([my_str[i] if i < length else my_str[i-length] for i in range(length * 2)])