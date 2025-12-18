'''Module to add a new Pokemon to the Pokedex database'''
from user_interface import menus, show
from validation import (DuplicateValueError as dv, EmptyFieldError as ef, clear_console, sleep,
                       validation_loop as vl, BackToStart, sqlite3_error)
from pokedex import Pokemon, exist_in_db, add_pokemon, get_pokemon


menu = menus.AddNew().menu

class add_new():
    '''Class to add a new Pokemon to the Pokedex database'''
    def __init__(self):
        self.pkmn = Pokemon()
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
    @vl
    def set_name(self):
        self.pkmn.name = input("Enter name: ")
        if exist_in_db(self.pkmn.name):  # Check if the name already exists in the database
            raise dv(f'This pokemon already exists!')

    @vl
    def set_number(self):
        self.pkmn.number = input("Enter number: ")                   
        if exist_in_db(self.pkmn.number):  # Check if the number already exists in the database
            raise dv(f'This pokemon already exists!')

    @vl
    def set_type1(self):
        self.pkmn.type1 = input("Enter type 1: ")

    @vl
    def set_type2(self):
        try:
            self.pkmn.type2 = input("Enter type 2 (or press Enter to skip): ")
        except (dv,ef):
            self.pkmn.type2 = None
        
    @vl
    def set_ability1(self):
        self.pkmn.ability1 = input("Enter ability 1: ")
    
    @vl
    def set_ability2(self):
        try:
            self.pkmn.ability2 = input("Enter ability 2: ")
        except (dv,ef):
            self.pkmn.ability2 = None
    
    @vl
    def set_hidden_ability(self):
        try:
            self.pkmn.hidden_ability = input("Enter hidden ability: ")
        except (dv,ef):
            self.pkmn.hidden_ability = None
    
    def create_pokemon(self):
        '''Method to create a new Pokemon and add it to the database.'''

        while True:
            print(menu(self.pkmn))
            choice = input()
            clear_console()
            if choice in self.jobs:
                try:
                    self.jobs[choice]()
                except (dv, ef) as e:
                    clear_console()
        
                    print(e)

            elif choice == "8":
                clear_console()
                if self.pkmn.name != "Default":
                    add_pokemon(self.pkmn)
                    sleep(1)
                    clear_console()
                    print(f"\nSuccessfully added {self.pkmn.name} to the Pokedex!\n")
                    sleep(1)
                    clear_console()
                    show(get_pokemon(self.pkmn.name))
                else:
                    print("Please fill in at least the Name field before saving.")
                 
  
                    clear_console()

            elif choice == "0":
                break
                    



        


    def main(self):
        while True:
            try:
                self.create_pokemon()
            except ValueError as ve:
                print(ve)

            cont = input("\nAdd another new pokemon (PRESS ENTER TO CONTINUE) ").strip().lower()
            if cont != '':
                break

if __name__ == "__main__":
    add_new().main()
