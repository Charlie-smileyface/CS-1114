def single_letter_encode(char,key):
   if char.islower():
      start_point = ord("a")
   else:
      start_point = ord("A")
   
   num_alpha = ord(char) - start_point + key
   encoded_letter = chr(num_alpha % 26 + start_point)
   return encoded_letter
   

def decode_caesar(line, decryption_key):
   encoded_massage = ""
   for letter in line:
      if letter.isalpha():
         encoded_letter = single_letter_encode(letter,decryption_key)
      else:
         encoded_letter = letter
      
      encoded_massage += encoded_letter
    
   return encoded_massage 
      
    
def main():
   decryption_key = 3
   line = input("Enter the encoded line: ")
   decryption = decode_caesar(line,decryption_key)
   print(decryption)
main()
