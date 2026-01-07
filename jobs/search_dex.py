'''Module to search for a Pokemon in the database and display its details'''
from pokedex import get_pokemon, pokemon_generator
from pokedex.pokemon import Pokemon as pk

from tools import clear_console, move_up, sleep, get_keypress, hide_cursor, show_cursor

class search_dex():
    '''Class to search for a Pokemon in the database and display its details'''

    def search_alphanum(self,pkmn = None):
        '''Method to get and display Pokemon details'''
        while True:
            if not pkmn:
                identifier = input(
                    "Enter Pokemon Name or Number to search: ").strip().title()
                if identifier == '0':
                   return
                result = get_pokemon(identifier)
                if result:
                    pkmn = pk(*result[0:7], result[7:13])
                else:
                    clear_console()
                    raise ValueError("Pokemon not found in the database.")

            clear_console()
            print(pkmn)
            print("\nPRESS ENTER TO RETURN TO SEARCH MENU")
            if input().strip() == '':
                return


    def search_dex(self):
        menu = f"--------- Search Pokedex ---------\n\n"
        menu_options = ["1. Search by Name or Number", "2. Search by Type",
                       "3. View All Pokemon", "0. Return to Main Menu", "\n------ Enter your choice ------"]
        clear_console()
        menu = menu + "\n".join(menu_options)
        menu = menu + "\n" + "-" * 31
        print(menu)

        display_list = []
        


        for pokemon in pokemon_generator():
            hide_cursor()
            item = f"{pokemon[0]:<13} | #{pokemon[1]:04}"
            display_list.append(item)


            choice = get_keypress()

            if choice == '0':
                return

            elif choice == '1':
                while True:
                    clear_console()
                    show_cursor()
                    try:
                        self.search_alphanum()

                        clear_console()
                        return
                        
                    except ValueError as e:
                        clear_console()
                        print(f"Error: {e}")
                        sleep(1)
                        continue

            elif choice == '2':
                clear_console()
                print("Search by Type selected.")
                sleep(1)
                return

            elif choice == '3':
                clear_console()
                print("View All Pokemon selected.")
                sleep(1)
                return
                
            if len(display_list) < 10:
                continue
                
            if len(display_list) == 10:
                print("\n".join(display_list))
            else:
                display_list.pop(0)
                move_up(10)
                print("\n".join(display_list))
                
                sleep(0.5)


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

