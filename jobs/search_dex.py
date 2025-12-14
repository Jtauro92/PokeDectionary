'''Module to search for a Pokemon in the database and display its details'''

from pokedex import Pokemon as pk, get_pokemon
from validation import( validation_loop as vl,
                        InvalidValueError,sqlite3_error,BackToStart)

class search_dex(pk):
    '''Class to search for a Pokemon in the database and display its details'''
    def __init__(self):
        super().__init__()

    
    def get_details(self):
        '''Method to get Pokemon details from user input'''
        
        result = get_pokemon(input("Enter Pokemon Name or Number to search: ").strip())
        if result is None:
            raise ValueError("Pokemon not found in the database.")
        return result


    def show_details(self):
        '''Method to get and display Pokemon details'''
        result = self.get_details() # Get details from user
        self.show(result) # Display the Pokemon's details
        print()
 

    def main(self):
        while True:
           try:
               self.show_details()
           except ValueError as ve:
               print(ve)
               break


if __name__ == "__main__":
    main = search_dex().main
    main()

