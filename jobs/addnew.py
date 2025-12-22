'''Module to add a new Pokemon to the Pokedex database'''
from user_interface import menus
from validation import (clear_console, sleep, validation_loop as vl)
from pokedex import Pokemon as pk, exist_in_db, add_pokemon
from update_stats import UpdateStats


menu = menus.AddNew().menu

class add_new():
    '''Class to add a new Pokemon to the Pokedex database'''
    def __init__(self):
        self.pkmn = pk()
        self.set_stats = UpdateStats().set_stats
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
            raise ValueError(f'This pokemon already exists!')

    @vl
    def set_number(self):
        self.pkmn.number = input("Enter number: ")                   
        if exist_in_db(self.pkmn.number):  # Check if the number already exists in the database
            raise ValueError(f'This pokemon already exists!')

    @vl
    def set_type1(self):
        self.pkmn.type1 = input("Enter type 1: ")

    @vl
    def set_type2(self):
        try:
            self.pkmn.type2 = input("Enter type 2 (or press Enter to skip): ")
        except ValueError:
            self.pkmn.type2 = None
        
    @vl
    def set_ability1(self):
        self.pkmn.ability1 = input("Enter ability 1: ")
    
    @vl
    def set_ability2(self):
        try:
            self.pkmn.ability2 = input("Enter ability 2: ")
        except ValueError:
            self.pkmn.ability2 = None
    
    @vl
    def set_hidden_ability(self):
        try:
            self.pkmn.hidden_ability = input("Enter hidden ability: ")
        except ValueError:
            self.pkmn.hidden_ability = None
    
    def create_pokemon(self):
        '''Method to create a new Pokemon and add it to the database.'''

        clear_console()
        print(menu(self.pkmn))

        choice = input()
        
        if choice in self.jobs:
 
            self.jobs[choice]()


        if choice == "8":
            # Ensure required fields are filled before saving
            if ("Default" not in [self.pkmn.name, self.pkmn.type1, self.pkmn.ability1] and 
                (self.pkmn.number != 0)):

                clear_console()
                add_pokemon(self.pkmn) # Add the new Pokemon to the database
                print(f"Successfully added {self.pkmn.name} to the Pokedex!\n")
                print(self.pkmn) # Display the added Pokemon's details
                sleep(2)

                clear_console()
                print("Would you like to enter stats for this Pokemon now?")
                cont = input("(PRESS ENTER TO CONTINUE OR ANY KEY TO SKIP) ").strip().lower()

                if cont == '':
                    self.set_stats(self.pkmn)
                else:
                    pass
                
                clear_console()
                cont = input("Add another new pokemon (PRESS ENTER TO CONTINUE) ").strip().lower()
                if cont != '':
                    raise ValueError
                else:
                    pass
            else:
                clear_console()
                print("Please fill in all required fields (Name, Number, Type 1, Ability 1) before saving.")
                sleep(1)


        elif choice == "0":
            cont = input("\nPRESS ENTER TO TRY AGAIN OR ANY KEY TO EXIT: ").strip().lower()
            if cont != '':
                raise ValueError
            else:
                pass
               
            self.pkmn = pk() # Reset to default Pokemon



    def main(self):
        while True:
            try:
                self.create_pokemon()
            except ValueError:
                break



if __name__ == "__main__":
    add_new().main()
