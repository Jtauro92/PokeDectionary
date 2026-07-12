from jobs import AddNewPokemon as an, search_dex as sd, UpdateStats as us
from tools import kbhit
from user_interface.menus import MainMenu
from tools import *
import sys
class Main:
    
    def __init__(self):
        self.jobs ={"1": an().main,
                    "2": sd().main,
                    "3": us().main}

    def _navigation(self):
        index = 1
        while True:
            kbhit()
            getwch()
            key = getwch()

            if key == "H":
                index -=1
            if key == "P":
                index  +=1

            if index > 4:
                index = 1

            if index < -4:
                index = 4
            print(index)
            if getwch() == '':
                return index



    def process_job(self):
        print(MainMenu())
        choice = getwch()
        clear_console()
        if choice == '0':
            sys.exit("Exiting the program. Goodbye!")
        elif choice in self.jobs:
            self.jobs[choice]()
        else:
            print("Invalid choice. Please try again.\n")
            sleep(1)
            clear_console()

    def main(self):
        while True:

            self.process_job()

       
Main().main()
