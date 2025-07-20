class Library: 
   def __init__(self):
     self.books = [] 
   
   def __str__(self):  # 如果没有这个就没办法正常的 print(self)
     return str(self.books) 

   def add_book(self, book):
     self.books.append(book) 
 
   def borrow_book(self, book):
     ind = self.available(book) 
     if ind >= 0: 
       self.books.pop(ind) 
       return True
     else: 
       return False
 
   def available(self, book):
     for i in range(len(self.books)): 
       if self.books[i] == book: 
         return i 
     return -1 

def main():
  lib = Library() 
  lib.add_book("A Game of Thrones") 
  lib.add_book("1984") 
  lib.add_book("Moby Dick") 
  print(lib.available("1984"))
  print(lib)
  print(lib.borrow_book("Moby Dick")) 
  print(lib) 
  print(lib.borrow_book("Becoming")) 
main()