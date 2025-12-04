from Database import Database as db
from ErrorHandling import (DuplicateValueError as dv, 
                          EmptyFieldError as ef, 
                          validation_loop
                          )
from Pokemon import Pokemon as pk


'''Class to add a new Pokemon'''

class add_new(pk):
    def __init__(self):
        super().__init__()
    
    '''Setters with validation loops for each attribute'''    
    @validation_loop
    def set_name(self):
        self.name = input("Enter name: ")
        if db().if_name_exist(self.name) != False:  # Check if the name already exists in the database
            raise ValueError("Duplicate Pokemon name.")

    @validation_loop
    def set_number(self):
        self.number = input("Enter number: ")                   
        if db().if_number_exist(self.number) != False:  # Check if the number already exists in the database
            raise ValueError("Duplicate Pokemon number.")

    @validation_loop
    def set_type1(self):
        self.type1 = input("Enter type 1: ")

    @validation_loop
    def set_type2(self):
        try:
            self.type2 = input("Enter type 2 (or press Enter to skip): ")
        except (dv,ef):
            self.type2 = None
        
    @validation_loop
    def set_ability1(self):
        self.ability1 = input("Enter ability 1: ")
    
    @validation_loop
    def set_ability2(self):
        try:
            self.ability2 = input("Enter ability 2: ")
        except (dv,ef):
            self.ability2 = None
    
    @validation_loop
    def set_hidden_ability(self):
        try:
            self.hidden_ability = input("Enter hidden ability: ")
        except (dv,ef):
            self.hidden_ability = None
    
    def create_pokemon(self):
        self.set_name()
        self.set_number()
        self.set_type1()
        self.set_type2()
        self.set_ability1()
        self.set_ability2()
        self.set_hidden_ability()
        self.add_to_dex()

    def main(self):
        while True:
            self.create_pokemon()
            cont = input("Add another Pokemon? (y/n): ").strip().lower()
            if cont != 'y':
                break

if __name__ == "__main__":
    p = add_new()
    p.main()

    print(p)

