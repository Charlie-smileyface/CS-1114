"""
Author: [Cheng Li]
Assignment / Part: HW10
Date due: 2023-05-04, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import random 

class Instrument:
    def __init__(self, model, brand, strength):
        self.model = model
        self.brand = brand
        self.strength = strength
    
    def __str__(self):
        return f"{self.brand} {self.model} ({round(self.strength * 100,1)} / 100 strength)"
    
    def does_break(self):
        random_num = random.random()
        if random_num < 0.5 * self.strength:
            return True
        else:
            return False
        
class Musician:
    def __init__(self, stage_name, instruments):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(self.instruments)
    
    def __str__(self):
        output = f"Musician object {self.stage_name}, owning a "
        for i in range(self.number_of_instruments - 1):
            output += str(self.instruments[i]) + ", "
        output += "and a " + str(self.instruments[-1])
        return output

    def pick_instrument(self, instrument_index = None):
        if self.number_of_instruments != 0:
            if instrument_index == None:
                rand_num = random.randrange(0, self.number_of_instruments)
                return self.instruments[rand_num]
            elif instrument_index >= self.number_of_instruments:
                return self.instruments[-1]
            else:
                return self.instruments[instrument_index]
        else:
            return None

def get_name_of_battle_winner(mu_1, mu_2):
    if mu_1.number_of_instruments == 0 and mu_2.number_of_instruments == 0:
        return "NO CONTEST"
    elif mu_1.number_of_instruments == 0 and mu_2.number_of_instruments != 0:
        return mu_2.stage_name
    elif mu_1.number_of_instruments != 0 and mu_2.number_of_instruments == 0:
        return mu_1.stage_name
    else:
        instrument_1 = mu_1.pick_instrument()
        instrument_2 = mu_2.pick_instrument()
        if instrument_1.strength > instrument_2.strength:
            print(f"{mu_1.stage_name} picked a {instrument_1}")
            print(f"{mu_2.stage_name} picked a {instrument_2}")
            return mu_1.stage_name if not instrument_1.does_break() else mu_2.stage_name
        
        elif instrument_2.strength > instrument_1.strength:
            print(f"{mu_1.stage_name} picked a {instrument_1}")
            print(f"{mu_2.stage_name} picked a {instrument_2}")
            return mu_2.stage_name if not instrument_2.does_break() else mu_1.stage_name
        
        else:
            print(f"{mu_1.stage_name} picked a {instrument_1}")
            print(f"{mu_2.stage_name} picked a {instrument_2}")
            print("Both musician's instruments are the same strength. The winner will be decided by the whim of chance.")
            return mu_1.stage_name if random.random() > 0.5 else mu_2.stage_name

def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]
    # Let's say both musicians have access to the same gear
    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)
    # Testing the get_name_of_battle_winner method a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician, less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!", end="\n\n")
main()

