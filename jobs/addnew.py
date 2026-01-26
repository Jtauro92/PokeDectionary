'''Module to add a new Pokemon to the Pokedex database'''
from genericpath import exists
from user_interface.menus import AddNewMenu
from tools import (clear_console, sleep, validation_loop as vl, getwch)
from pokedex.pokemon import Pokemon as pk
from pokedex import add_pokemon
from jobs.update_stats import UpdateStats, get_pokemon


menu = AddNewMenu

class AddNewPokemon:
    '''Class to add a new Pokemon to the Pokedex database'''
    def __init__(self):
        self.pkmn = pk()
        self.update_stats = UpdateStats().set_stats
        self.jobs = {
            "1": self.set_name,
            "2": self.set_number,
            "3": self.set_type1,
            "4": self.set_type2,
            "5": self.set_ability1,
            "6": self.set_ability2,
            "7": self.set_hidden_ability
        }


    '''Setters with validation loops for each attribute'''    
    def set_name(self):
        if get_pokemon(name := input("Enter name: ").title()):  # Check if the name already exists in the database
            raise ValueError(f'This pokemon already exists!')
        self.pkmn.name = name

    def set_number(self):
        if get_pokemon(number := input("Enter number: ")):# Check if the number already exists in the database
            raise ValueError(f'This pokemon already exists!')                 
        self.pkmn.number = number

    def set_type1(self):
        self.pkmn.type1 = input("Enter type 1: ")

    def set_type2(self):
        try:
            self.pkmn.type2 = input("Enter type 2 (or press Enter to skip): ")
        except ValueError:
            self.pkmn.type2 = None
        
    def set_ability1(self):
        self.pkmn.ability1 = input("Enter ability 1: ")
    
    def set_ability2(self):
        try:
            self.pkmn.ability2 = input("Enter ability 2: ")
        except ValueError:
            self.pkmn.ability2 = None
    
    def set_hidden_ability(self):
        try:
            self.pkmn.hidden_ability = input("Enter hidden ability: ")
        except ValueError:
            self.pkmn.hidden_ability = None

    @vl
    def _process_jobs(self, choice):
        if choice in self.jobs:
            self.jobs[choice]()
    
    def create_pokemon(self):
        '''Method to create a new Pokemon and add it to the database.'''

        clear_console()
        print(menu(self.pkmn))

        choice = getwch()
        
        self._process_jobs(choice)

        if choice == "8":
            
            try:
                self._save_data()
            except ValueError:
                return


        elif choice == "0":
            self.pkmn = pk()  # Reset to default Pokemon
            clear_console()
            print('PRESS ENTER TO TRY AGAIN OR ANY KEY TO EXIT: ')
            cont = getwch()
            if cont != '':
                raise ValueError
               

    def _save_data(self):
        # Ensure required fields are filled before saving
        required = [self.pkmn.name, self.pkmn.number,
                    self.pkmn.type1, self.pkmn.ability1]
        if all(required) and (self.pkmn.number != 0):
            clear_console()
            try:
                add_pokemon(self.pkmn)
                print(f"Successfully added {self.pkmn.name} to the Pokedex!\n")
                print(self.pkmn)
                sleep(2)
                
                clear_console()
                print("Would you like to set {}'s stats now?".format(self.pkmn.name))
                if input("Press ENTER to set stats or any other key to skip: ").strip() == '':
                    self.update_stats(self.pkmn)
                else:
                    return
            except Exception as e:
                print(f"Error adding Pokemon: {e}")

        if input("\nPRESS ENTER TO CONTINUE").strip() != '':
            raise ValueError
            

    def main(self):
        while True:
            try:
                self.create_pokemon()
            except ValueError:
                break



if __name__ == "__main__":
    AddNewPokemon().main()
