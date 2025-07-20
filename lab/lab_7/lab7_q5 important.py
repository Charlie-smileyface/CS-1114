user_input = input("Enter a phase: ")

start = 0
output = ''

for i in range(len(user_input)):
    if user_input[i] == " ":
        part = user_input[start:i]

        if part.isdigit():
            part = "x" * len(part)

        output += part + " "
        start = i+1

last_part = user_input[start:len(user_input)]
if last_part.isdigit():
    last_part = "x"*len(last_part)

output += last_part
    
print(output)
        
