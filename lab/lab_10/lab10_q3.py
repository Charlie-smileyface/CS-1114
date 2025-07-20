import random

def get_random_word(filepath):
    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        return "file not found"
    
    words = []
    for line in file:
        inside_words = line.strip().split(" ")
        words.extend(inside_words)
    
    file.close()

    length = len(words)
    print(length)
    random_num = random.randrange(0,length)
    print(words)

    return words[random_num]

def main():
    print(get_random_word("lab\lab_10\word.txt"))

if __name__ == '__main__':
    main()