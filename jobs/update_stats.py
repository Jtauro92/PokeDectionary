from pokedex import update_stats, get_full_pokemon, stats
from validation import validation_loop as vl
from user_interface import stats_menu as sm
from tools import *

class UpdateStats(stats):
    def __init__(self):
        super().__init__()
        self.jobs = {'1': self.set_hp, 
                     '2': self.set_atk, 
                     '3': self.set_defn, 
                     '4': self.set_spatk, 
                     '5': self.set_spdef, 
                     '6': self.set_speed
                     }
    @vl
    def set_hp(self):
        self.hp = input("Enter HP: ")

    @vl
    def set_atk(self):
        self.atk = input("Enter Attack: ")

    @vl
    def set_defn(self):
        self.defn = input("Enter Defense: ")

    @vl
    def set_spatk(self):
        self.spatk = input("Enter Special Attack: ")

    @vl
    def set_spdef(self):
        self.spdef = input("Enter Special Defense: ")

    @vl
    def set_speed(self):
        self.speed = input("Enter Speed: ")

    def set_stats(self):
        identifier = input("Enter Pokemon name or number to update stats: ").strip()
        
        if identifier == '0':
            return
        
        result = get_full_pokemon(identifier.strip())
        if result:
            name,number = result[0:2]
            while True:
                clear_console()
                stats = list(result[7:])
                stats[0] = self.hp if self.hp is not None else stats[0]
                stats[1] = self.atk if self.atk is not None else stats[1]
                stats[2] = self.defn if self.defn is not None else stats[2]
                stats[3] = self.spatk if self.spatk is not None else stats[3]
                stats[4] = self.spdef if self.spdef is not None else stats[4]
                stats[5] = self.speed if self.speed is not None else stats[5]
                print(sm(name,stats)) # Display the stats menu
                choice = input()
                clear_console()

                if choice == '0':
                    return

                if choice == '7':
                    update_stats(number, self.hp, self.atk, self.defn, self.spatk, self.spdef, self.speed)
                    print(f"{name}'s stats have been updated successfully.")
                    sleep(1)
                    clear_console()
                    break

                if any(choice == key for key in self.jobs):
                    self.jobs[choice]()
                else:
                    raise ValueError("Invalid choice. Please try again.")
        else:
            raise ValueError("Pokemon not found in the database.")


        
    
    def main(self):
        while True:
            try:
                self.set_stats()
            except ValueError as ve:
                print(ve)

            cont = input("Update another pokemon's stats (y/n): ").strip().lower()
            if cont != 'y':
                break
                
     
        

if __name__ == "__main__":
    us = UpdateStats()
    us.main()
