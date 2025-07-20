def numberify(word):
    word_up = word.upper()
    msg = ""
    for letter in word_up:
        if letter == "A":
            letter = "4"
        elif letter == "E":
            letter = "3"
        elif letter == "I":
            letter = "1"
        elif letter == "S":
            letter = "5"
        elif letter == "T":
            letter = "7"
        elif letter == "O":
            letter = "0"
        msg += letter

    return msg

def main():
    word = input("Please enter a message to numberify: ")
    word += " " 
    msg = ""
    start = 0
    for i in range(len(word)):
        if word[i] == " ":
            end = i
            part = word[start:end]
            if len(part) > 3:
                change_part = numberify(part)
            else:
                change_part = part.upper()
            start = end + 1
            msg += change_part + " "
    print(msg)
main()        


