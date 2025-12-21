'''Module to search for a Pokemon in the database and display its details'''
from msvcrt import getch, kbhit
from pokedex import get_pokemon, pokemon_generator
from user_interface import show
from tools import clear_console, sleep

class search_dex():
    '''Class to search for a Pokemon in the database and display its details'''
    def __init__(self):
        super().__init__()

    def get_details(self):
        '''Method to get Pokemon details from user input'''
        identifier = input("Enter Pokemon Name or Number to search: ").strip().title()
        clear_console()
        result = get_pokemon(identifier)
        if identifier == '0':
            clear_console()
            return
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
            return

    def search_dex(self):
        menu = f"--------- Search Pokedex ---------\n\n"
        menu_options = ["1. Search by Name or Number", "2. Search by Type",
                       "3. View All Pokemon", "0. Return to Main Menu", "\n------ Enter your choice ------"]
        menu += "\n".join(menu_options)
        count = 1
        display_list = []
        for pokemon in pokemon_generator():
            count += 1
            display_list.append(f"{pokemon[0]:<13} | #{pokemon[1]:04}")
            
            if len(display_list) == 10:
                clear_console()
                print(menu)
                print("\n".join(display_list))
                display_list.pop(0)
                sleep(0.5)


            if kbhit():
                choice = getch()
                if choice.isdigit():
                    choice = int(choice)
                    if choice == 0:
                        clear_console()
                        print("Returning to Main Menu.")
                        raise ValueError
                    elif choice == 1:
                        clear_console()
                        while True:
                            clear_console()
                            self.show_details()
                            cont = input("(PRESS ENTER TO CONTINUE OR ANY KEY TO RETURN TO MENU) ").strip().lower()
                            if cont != "":
                                return
                    elif choice == 3:
                        print("Search by Type selected.")
                    elif choice == 4:
                        print("View All Pokemon selected.")
                elif choice == b'\x1b':  # Escape key
                    print("Search canceled.")

    def main(self):
        '''Main method to run the search dex functionality'''
        while True:
            try:
                self.search_dex()
            except ValueError:
                break

  


if __name__ == "__main__":
    main = search_dex().main
    main()

