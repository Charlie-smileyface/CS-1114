class Pet:
    def __init__(self, name, type, age, fav_treats = None): ## 不能用可而变的object来作为 default value(例如一个空的lst []), 可以先用 None，然后用 if 区分
        self.name = name
        self.type = type
        self.age = age
        if fav_treats == None:
            self.fav_treats = []
        else:
            self.fav_treats = fav_treats
    
    def rename(self, new_name):
        self.name = new_name
    
    def brithday(self):
        self.age += 1
    
    def add_treat(self, treat):
        self.fav_treats.append(treat)
    
    def __str__(self):
        intro = f"{self.name} is a {self.type} that {self.age} years old."
        title = "Favorite treats:"
        str_treats = "\n".join([treat for treat in self.fav_treats])
        return intro + "\n" + title + "\n" + str_treats
    

def main():
    pet_lst = []
    user_input = input("Enter a command: ")
    while user_input != "Q" and user_input != "q":
        if user_input == "adopt":
            name = input("What is the name of the pet? ")
            type = input("What is the type of the pet? ")
            age = int(input("How old is the pet? "))
            pet = Pet(name, type, age)
            pet_lst.append(pet)
        
        elif user_input == "rename":
            old_name  = input("What is the current name? ")
            new_name = input("What is the new name? ")
            for pet in pet_lst:
                if pet.name == old_name:
                    pet.rename(new_name)
        
        elif user_input == "birthday":
            name = input("What is the name of pet? ")
            for pet in pet_lst:
                if pet.name == name:
                    pet.brithday()
        
        elif user_input == "treat":
            name = input("What is the name of pet? ")
            treat = input("What is the name of treat? ")
            for pet in pet_lst:
                if pet.name == name:
                    pet.add_treat(treat)
        
        elif user_input == "pets":
            for pet in pet_lst:
                print(pet)
        
        user_input = input("Enter a command: ")
main()



