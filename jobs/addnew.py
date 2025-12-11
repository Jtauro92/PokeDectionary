from jobs import dv, ef, vl, BackToStart, pk, sql

'''Class to add a new Pokemon'''

class add_new(pk):
    def __init__(self):
        super().__init__()
    
    '''Setters with validation loops for each attribute'''    
    @vl
    def set_name(self):
        self.name = input("Enter name: ")
        if self.exists_in_db(self.name):  # Check if the name already exists in the database
            raise dv(f'This pokemon already exists!')

    @vl
    def set_number(self):
        self.number = input("Enter number: ")                   
        if self.exists_in_db(self.number):  # Check if the number already exists in the database
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
            self.add_pokemon()
        except sql:
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
    p = add_new()
    p.main()

