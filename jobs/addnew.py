'''Module to add a new Pokemon to the Pokedex database'''
from user_interface import show
from validation import (DuplicateValueError as dv, EmptyFieldError as ef,
                       validation_loop as vl, BackToStart, sqlite3_error)
from pokedex import Pokemon as pk, exist_in_db, add_pokemon


class add_new(pk):
    def __init__(self):
        super().__init__()
    
    '''Setters with validation loops for each attribute'''    
    @vl
    def set_name(self):
        self.name = input("Enter name: ")
        if exist_in_db(self.name):  # Check if the name already exists in the database
            raise dv(f'This pokemon already exists!')

    @vl
    def set_number(self):
        self.number = input("Enter number: ")                   
        if exist_in_db(self.number):  # Check if the number already exists in the database
            raise dv(f'This pokemon already exists!')

    @vl
    def set_type1(self):
        self.type1 = input("Enter type 1: ")

    @vl
    def set_type2(self):
        try:
            self.type2 = input("Enter type 2 (or press Enter to skip): ")
        except (dv,ef):
            self.type2 = None
        
    @vl
    def set_ability1(self):
        self.ability1 = input("Enter ability 1: ")
    
    @vl
    def set_ability2(self):
        try:
            self.ability2 = input("Enter ability 2: ")
        except (dv,ef):
            self.ability2 = None
    
    @vl
    def set_hidden_ability(self):
        try:
            self.hidden_ability = input("Enter hidden ability: ")
        except (dv,ef):
            self.hidden_ability = None
    
    def create_pokemon(self):
        try:
            self.set_name()
            self.set_number()
            self.set_type1()
            self.set_type2()
            self.set_ability1()
            self.set_ability2()
            self.set_hidden_ability()          
            add_pokemon(self.name, self.number, self.type1, self.type2,
                        self.ability1, self.ability2, self.hidden_ability)
        except sqlite3_error as sql:
            raise sql
        except BackToStart:
            return
        except ValueError as ve:
            raise ve
        


    def main(self):
        while True:
            try:
                self.create_pokemon()
            except ValueError as ve:
                print(ve)

            cont = input("Add another Pokemon? (y/n): ").strip().lower()
            if cont != 'y':
                break

if __name__ == "__main__":
    pass

