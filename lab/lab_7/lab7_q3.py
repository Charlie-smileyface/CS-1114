user_input = input("Enter your massage: ")
vowels = "aeiou"
count = 0

for letter in user_input.lower():
    if letter in vowels: ##不能用=，反过来想用 in 先 define vowles
        count += 1
print("Total number of vowels: ",count)
