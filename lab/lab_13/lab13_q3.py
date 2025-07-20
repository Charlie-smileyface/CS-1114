class Passenger:
    def __init__(self, name, country, number_of_bags):
        self.name = name
        self.country = country
        self.number_of_bags = number_of_bags
    
    def __str__(self):
        return f"{self.name} is a citizen of {self.country} and has {self.number_of_bags} bags"
    
    def add_bag(self):
        self.number_of_bags += 1
   
    def remove_bag(self):
        self.number_of_bags -= 1

class Flight:
    def __init__(self, number, aircraft, departure_location, arrival_location, departure_time, arrival_time):
        self.number = number
        self.aircraft = aircraft
        self.departure_location = departure_location
        self.arrival_location = arrival_location
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.passengers = [] ## 题目虽然没有提到，但是后面需要用到，也define在 init 当中

    def __str__(self):
        return f"{self.number} {self.aircraft} departs {self.departure_location} at {self.departure_time} and arrives at {self.arrival_location} at {self.arrival_time}"
    
    def print_passengers(self):
        pass

    def add_passenger(self, passenger):
        if passenger not in self.passengers:
            self.passengers.append(passenger)
            return True
        else:
            return False
    
    def remove_passenger(self,passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            return True
        else:
            return False
    
    def get_passenger_count(self):
        return len(self.passengers)

    
def main():
    flight_eu = Flight(6783, "Airbus A320", "London", "Paris", "12:00", "14:00")
    bob = Passenger("Bob", "France", 2)
    alice = Passenger("Alice", "France", 1)
    henry = Passenger("Henry", "UK", 1)
    print(bob)
    print(alice)
    print(henry)
    flight_eu.add_passenger(bob)
    flight_eu.add_passenger(alice)
    flight_eu.add_passenger(henry)
    flight_eu.add_passenger(henry)
    print(flight_eu)
    flight_eu.print_passengers()
    print("There are", flight_eu.get_passenger_count(), "passengers on this flight")
    flight_eu.remove_passenger(bob)
    flight_eu.print_passengers()
main()
