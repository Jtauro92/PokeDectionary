from Database import Database as db
from Pokemon import Pokemon as pk


np = pk() # Create an instance of the Pokemon class

'''Class to add a new Pokemon'''
class add_new():
    
    def __init__(self):
        super().__init__()

    def add_name(self):
        np.name = input("Enter name: ")
        if db().if_name_exist(np.name) != False:  # Check if the name already exists in the database
            raise ValueError("Duplicate Pokemon name.")

    def add_number(self):
        np.number = input("Enter number: ")                   
        if db().if_number_exist(np.number) != False:  # Check if the number already exists in the database
            raise ValueError("Duplicate Pokemon number.")


    def add_type(self):
        try:
            np.type1 = input("Enter type 1: ")

            np.type2 = input("Enter type 2: ")

        except ValueError as ve:
            msg = str(ve)
            if "already assigned" in msg:
                pass

        return (np.type1, np.type2)




    def add_abilities(self):
        np.ability1 = input("Enter ability 1: ")
        np.ability2 = input("Enter ability 2: ")
        np.hidden_ability = input("Enter hidden ability: ")
        return (np.ability1, np.ability2, np.hidden_ability)
    
    def get_pokemon(self):
        return np

    def create_pokemon(self):
        try:
            self.add_name()

            self.add_number()
        
            self.add_type()

            self.add_abilities()
        except ValueError as ve:
            print(ve)
            return None


    def main(self):
        while True:
            pokemon = self.create_pokemon()
            if pokemon:
                db().add_pokemon(pokemon)
                print("Pokemon added successfully:")
                break
            else:
                print("Failed to add Pokemon. Please try again.")

if __name__ == "__main__":
    p = add_new()
    print(p.create_pokemon())




