'''Module to search for a Pokemon in the database and display its details'''

from pokedex import get_pokemon
from user_interface import show
from tools import clear_console, sleep

class search_dex():
    '''Class to search for a Pokemon in the database and display its details'''
    def __init__(self):
        super().__init__()

    def get_details(self):
        '''Method to get Pokemon details from user input'''
        identifier = input("Enter Pokemon Name or Number to search: ").strip()
        clear_console()
        result = get_pokemon(identifier)
        if identifier == '0':
            clear_console()
            raise ValueError
        if result is None:
            clear_console()
            raise TypeError("Pokemon not found in the database.")
            
        return result


    def show_details(self):
        '''Method to get and display Pokemon details'''
        try:
            result = self.get_details() # Get details from user
            show(result) # Display the Pokemon's details
            print()
        except TypeError as te:
            print(te)
            sleep(1)
            clear_console()

    def main(self):
        while True:
           try:
               self.show_details()
           except ValueError as ve:
               break
\


if __name__ == "__main__":
    main = search_dex().main
    main()

