def prompt_user_for_pw():
    pw = input("Enter a password: ")
    return pw

def is_strong_pw(pw):
    greater_check = False
    upper_check = False
    lower_check = False
    special_check = False

    if len(pw) >= 8:
        greater_check = True
    
    for letter in pw:
        if letter.isupper():
            upper_check = True
        elif letter.islower():
            lower_check = True
        elif letter == "!" or letter == "@" or letter == "#" or letter == "*":
            special_check = True
        elif letter.isdigit():
            num_check = True
    
    if greater_check == True and upper_check == True and lower_check == True and special_check == True and num_check == True:
        return True
    else:
        return False

def main():
    pw = prompt_user_for_pw()
    while is_strong_pw(pw) == False:
        print("Password too weak!")
        pw = prompt_user_for_pw()
    print("Thank you! Your password is considered strong.")
main()
