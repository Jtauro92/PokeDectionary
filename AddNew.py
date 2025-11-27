from Database import Database as db
from Pokemon import Pokemon as pk


np = pk() # Create an instance of the Pokemon class

'''Class to add a new Pokemon'''
class add_new():
    
    def __init__(self):
        super().__init__()

    def add_name(self):
        np.name = input("Enter name: ")
        if db().if_name_exists(np.name) != False:  # Check if the name already exists in the database
            raise ValueError("Duplicate Pokemon name.")
        return np.name

    def add_number(self):
        np.number = input("Enter number: ")
                                
        return np.number

    def add_type(self):
        np.type1 = input("Enter type 1: ")
        np.type2 = input("Enter type 2: ")
        return np.type1, np.type2

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
        except ValueError as ve:
            print(ve)

            self.add_number()
        except ValueError as ve:
            print(ve)
        
            self.add_type()
        except ValueError as ve:
            print(ve)
       
            self.add_abilities()
        except ValueError as ve:
            print(ve)
            return None


        return (np.name, np.number, np.type1, np.type2, np.ability1, np.ability2, np.hidden_ability))

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
    p.main()



