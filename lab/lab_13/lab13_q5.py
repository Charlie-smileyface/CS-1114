class Pirate:
    def __init__(self, name, loot = 0):
        self.name = name
        self.status = "Solo"
        self.loot = loot
    
    def __str__(self):
        return f"{self.status} {self.name}"
    
    def update_loot(self, loot_change):
        self.loot += loot_change
        if self.loot < 0:
            self.loot = 0
    
    def update_status(self, status):
        self.status = status
    
    def get_loot(self):
        return self.loot
    
class Crew:
    def __init__(self, name):
        self.name = name
        self.pirates = []
        self.captain = None
        self.total_loot = 0
    
    def __str__(self):
        pirate_members = "\n".join([pirate.name for pirate in self.pirates])
        if self.pirates == []:
            return f"{self.name} under captain {self.captain} with the following crew members:\n No crew members yet. \nWith a total loot of: {self.total_loot}"
        else:
            return f"{self.name} under captain {self.captain} with the following crew members: \n{pirate_members}. \nWith a total loot of: {self.total_loot}"
    
    def add_crew_member(self, pirate, role):
        if role == "Captain":
            if self.captain == None:
                self.pirates.append(pirate)
                self.total_loot += pirate.loot
                self.captain = pirate.name 
                return True
            else:
                return False
        else:
            self.pirates.append(pirate)
            self.total_loot += pirate.loot
            return True
            
    
    def remove_crew_member(self, pirate):
        if pirate in self.pirates:
            self.pirates.remove(pirate)
            self.total_loot -= pirate.loot
            if self.captain == pirate.name:
                self.captain = None
            return True
        else:
            return False

def main():
     # Creating our pirates
    pirate_jack = Pirate("Jack Sparrow")
    pirate_will = Pirate("Will Turner", 5)
    pirate_eliza = Pirate("Elizabeth Swann", 100)
    pirate_barbossa = Pirate("Hector Barbossa")
    pirate_rag = Pirate("Ragetti")
    pirate_pin = Pirate("Pintel", 10)
    # Updating the loot of some pirates
    pirate_barbossa.update_loot(40)
    pirate_eliza.update_loot(-20)
    pirate_rag.update_loot(-10)
    # Printing the current status of all our pirates
    all_pirates = [pirate_jack, pirate_will, pirate_eliza, pirate_barbossa, pirate_rag, pirate_pin]
    for pirate in all_pirates:
        print(pirate, pirate.get_loot())
    print()
    
    # Creating our 2 crews
    crew1 = all_pirates[:3]
    crew2 = all_pirates[3:]
    jack_sparrow_crew = Crew("Jack Sparrow Crew")
    black_pearl_crew = Crew("Black Pearl Crew")
    # Print the empty crews
    print("---------------------------Printing empty crews---------------------------")
    print(jack_sparrow_crew)
    print()
    print(black_pearl_crew)
    print()
    # Add members to each crew
    for pirate in crew1:
        is_pirate_added = jack_sparrow_crew.add_crew_member(pirate, "Captain")
        if not is_pirate_added:# Unable to add pirate due to attempting to add a 2nd captain  # Intead, add the pirate as a member
            jack_sparrow_crew.add_crew_member(pirate, "Member")
    
    for pirate in crew2:
        is_pirate_added = black_pearl_crew.add_crew_member(pirate, "Captain")
        if not is_pirate_added: # Unable to add pirate due to attempting to add a 2nd captain # Instead, add the pirate as a member
            black_pearl_crew.add_crew_member(pirate, "Member")
    # Print the newly made crews
    print("---------------------------Printing the newly made crews---------------------------")
    print(jack_sparrow_crew)
    print()
    print(black_pearl_crew)
    print()
    # Adding and removing a Pirate to a crew
    pirate_blackbeard = Pirate("Blackbeard", 50)
    # Removing a pirate not part of the crew
    black_pearl_crew.remove_crew_member(pirate_blackbeard)
    # Adding a Pirate to the crew then removing the pirate
    black_pearl_crew.remove_crew_member(pirate_barbossa)
    black_pearl_crew.add_crew_member(pirate_blackbeard, "Captain")
    print("---------------------------Printing the new crew after captain changes---------------------------")
    print(black_pearl_crew)
    print()
    print(pirate_barbossa)
main()
