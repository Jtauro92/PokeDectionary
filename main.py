from jobs import add_new as an, search_dex as sd
from validation import sleep
from tools import clear_console as clear_screen



class Main:
    
    def __init__(self):
        self.jobs ={
                '1': an().main,
                '2': sd().main,
               }
    
    def display_menu(self):
        clear_screen()
        print('-'*30)
        print("Menu:")
        print("1. Add Pokemon")
        print("2. Search Dex")
        print("3. Option 3")
        print("4. Option 4")
        print("0. Exit")
        print('-'*30)
        print("Select an option to proceed: ")

    def process_job(self):
            self.display_menu()
            choice = input().strip()
            clear_screen()
            if choice == '0':
                raise KeyboardInterrupt
            elif any(choice == key for key in self.jobs):
                self.jobs[choice]()
            else:
                print("Invalid choice. Please try again.\n")
                sleep(1)
                clear_screen()

    def main(self):
        while True:
            try:
                self.process_job()
                clear_screen()
            except KeyboardInterrupt:
                clear_screen()
                print("Exiting program. Goodbye!")
                break

        
Main().main()
