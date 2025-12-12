'''Module to search for a Pokemon in the database and display its details'''

from pokedex import Pokemon as pk, get_pokemon
from validation import( validation_loop as vl,
                        InvalidValueError,sqlite3_error,BackToStart)

class search_dex(pk):
    '''Class to search for a Pokemon in the database and display its details'''
    def __init__(self):
        super().__init__()

    
    @vl
    def get_details(self):
        '''Method to get Pokemon details from user input'''
        
        identifier = input("Enter Pokemon name or number to search: ").strip().title()
        if identifier == '0':
            raise BackToStart # Exit on '0' input

        try:
            name, number, t1, t2, a1, a2, ha = get_pokemon(identifier) # Retrieve details from the database
            self.name = name
            self.number = number
            self.type1 = t1
            self.type2 = t2
            self.ability1 = a1
            self.ability2 = a2
            self.hidden_ability = ha
        except TypeError:
                raise InvalidValueError("Pokemon not found in the database.") #Raise error if not found
        except sqlite3_error as e:
            raise e("Database error: self.fetchone(sql_search, (identifier, identifier))")


    def show_details(self):
        '''Method to get and display Pokemon details'''
        self.get_details() # Get details from user
        self.show() # Display the Pokemon's details
        print()
 

    def main(self):
        while True:
            try:
                self.show_details()
            except KeyboardInterrupt:
                print("Exiting search.")
                break

if __name__ == "__main__":
    sd = search_dex()
    sd.main()

