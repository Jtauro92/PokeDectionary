from jobs import add_new as an, search_dex as sd, UpdateStats as us
from tools import *

class Main:
    
    def __init__(self):
        self.jobs ={
                '1': an().main,
                '2': sd().main,
                '3': us().main,
               }
    
    def display_menu(self):
        clear_console()
        print('-'*30)
        print("Menu:")
        print("1. Add Pokemon")
        print("2. Search Dex")
        print("3. Update Stats")
        print("4. Delete Pokemon")
        print("0. Exit")
        print('-'*30)
        print("Select an option to proceed: ")

    def process_job(self):
            self.display_menu()
            choice = input().strip()
            clear_console()
            if choice == '0':
                print("Exiting the program. Goodbye!")
                exit() 
            elif choice in self.jobs:
                self.jobs[choice]()
            else:
                print("Invalid choice. Please try again.\n")
                sleep(1)
                clear_console()

    def main(self):
        while True:
            self.process_job()
            clear_console()


        
Main().main()
