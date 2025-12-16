from pokedex import get_stats, update_stats, get_pokemon, Pokemon as pk
from validation import validation_loop as vl
from user_interface import stats_menu as sm
from tools import *

class UpdateStats(pk):
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

    def set_stats(self, identifier=None):
        '''Method to set stats for a given Pokemon.'''
        if identifier is None:
            identifier = input("Enter Pokemon name or number to update stats: ").strip()
           

        elif identifier == '0':
            return # Exit if user chooses to go back

        result = get_pokemon(identifier) # Fetch pokemon details

        if not result:
            raise ValueError("Pokemon not found in the database.")

        name, number,current_stats = result[0], result[1], result[7:]

        while True:
            clear_console()

            # Merge existing stats with current object stats
            updated_stats = [ self.hp, self.atk, self.defn, self.spatk, self.spdef, self.speed]
            merged_stats = [ new if new is not None else old 
                            for new, old in zip(updated_stats, current_stats)]

            print(sm(name,merged_stats))
            choice = input().strip()
            clear_console()

            if choice == '0':
                break

            if choice == '7':
                update_stats(*merged_stats, number)
                print(f"Stats for {name} updated successfully.")
                sleep(1)
                clear_console()
                break

            if choice in self.jobs:
                self.jobs[choice]()
            else:
                raise ValueError("Invalid choice. Please select a valid option.")
    
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
