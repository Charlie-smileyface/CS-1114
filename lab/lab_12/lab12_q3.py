def count_vowels(filename):
    try:
        file_obj = open(filename, 'r')
    except FileNotFoundError:
        return {}
    
    vowels = "AEIOU"
    file_content = file_obj.read()
    file_obj.close()
    
    dict = {vowel : file_content.count(vowel) for vowel in vowels}
    
    return dict

print(count_vowels("lab\lab_12\count_vowels.txt"))