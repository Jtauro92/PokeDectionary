import os

from AddNew import add_new as an
class Main:
    def __init__(self):
        self.jobs ={
                '1': an().main,
               }
    
    def display_menu(self):
        print('-'*30)
        print("Menu:")
        print("1 Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("0. Exit")
        print('-'*30)
        print("Select an option to proceed: ")

    def process_job(self):
        try:
            self.display_menu()
            choice = input().strip()
            if choice == '0':
                raise KeyboardInterrupt
            elif any(choice == key for key in self.jobs):
                os.system('cls')
                self.jobs[choice]()
            else:
                os.system('cls')
                print("Invalid choice. Please try again.\n")
        except KeyboardInterrupt:
            raise KeyboardInterrupt

    def main(self):
        while True:
            try:
                self.process_job()
            except KeyboardInterrupt:
                os.system('cls')
                print("Exiting program. Goodbye!")
                break

        

if __name__ == "__main__":
    Main().main()
