from Database import Database as db
from ErrorHandling import DuplicateAbilityError, DuplicateTypeError, validation_loop
from Pokemon import Pokemon as pk



np = pk() # Create an instance of the Pokemon class

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
        np.type1 = input("Enter type 1: ")
    
    def set_type2(self):
        try:
            np.type2 = input("Enter type 2 (or press Enter to skip): ")
        except DuplicateTypeError:
            np.type2 = None
        
    @validation_loop
    def set_ability1(self):
        np.ability1 = input("Enter ability 1: ")
    
    def set_ability2(self):
        try:
            np.ability2 = input("Enter ability 2: ")
        except DuplicateAbilityError:
            np.ability2 = None

    def set_hidden_ability(self):
        try:
            np.hidden_ability = input("Enter hidden ability: ")
        except DuplicateAbilityError:
            np.hidden_ability = None
    
    def create_pokemon(self):
        self.set_name()
        self.set_number()
        self.set_type1()
        self.set_type2()
        self.set_ability1()
        self.set_ability2()
        self.set_hidden_ability()
            
    def get_pokemon(self):
        return (
            self.name,
            self.number,
            self.type1,
            self.type2,
            self.ability1,
            self.ability2,
            self.hidden_ability
        )

    
    def main(self):
        add = db().add_pokemon
        while True:
            pokemon = self.create_pokemon()
            if pokemon:
                add(self.get_pokemon)
                print("Pokemon added successfully:")
                break
            else:
                print("Failed to add Pokemon. Please try again.")

if __name__ == "__main__":
    p = add_new()
    p.main()



