from Pokemon import Pokemon as pk

np = pk()

class add_new(pk):
    def __init__(self):
        super().__init__()

    def add_name(self):
        np.name = input("Enter name: ")
            
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
            self.add_number()
            self.add_type()
            self.add_abilities()
            return self.get_pokemon()
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
            
    def main(self):
        while True:
            pokemon = self.create_pokemon()
            if pokemon:
                print("Pokemon added successfully:")
                print(self)
                break
            else:
                print("Failed to add Pokemon. Please try again.")

if __name__ == "__main__":
    p = add_new()
    p.main()



