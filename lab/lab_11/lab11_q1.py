def f1(my_dict):
   temp = 0
   for val in my_dict.values(): 
     temp = temp + val 
   return temp

def f2(my_dict):
   temp = ""
   for key in my_dict: 
     if temp < key : 
        temp = key 
   return temp 

def f3 (my_dict, k, v):
   if k in my_dict: 
      my_dict[k] = v 

def main ():
   a_dict = {"Kim" : 13, "Sarah" : 27, "Semi" : 19, "Kevin" : 23} 
   print(f1(a_dict)) # line 1 
   print(f2(a_dict)) # line 2 
   f3(a_dict, "Sarah", 30) 
   print(a_dict) # line 3
main()

# line_1: 82
# line 2: "Semi"
# line 3: {"Kim" : 13, "Sarah" : 30, "Semi" : 19, "Kevin" : 23} 