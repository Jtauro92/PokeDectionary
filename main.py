from jobs import AddNewPokemon as an, search_dex as sd, UpdateStats as us
from user_interface.menus import MainMenu
from tools import *

class Main:
    
    def __init__(self):
        self.jobs ={
                '1': an().main,
                '2': sd().main,
                '3': us().main,
               }

    def process_job(self):
        print(MainMenu())
        choice = getwch()
        clear_console()
        if choice == '0':
            print("Exiting the program. Goodbye!")
            raise SystemExit
        elif choice in self.jobs:
            self.jobs[choice]()
        else:
            print("Invalid choice. Please try again.\n")
            sleep(1)
            clear_console()

    def main(self):
        while True:
            try:
                self.process_job()
                clear_console()
            except SystemExit:
                return


        
Main().main()
