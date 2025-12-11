from jobs import an, sleep, system


class Main:
    
    def __init__(self):
        self.jobs ={
                '1': an().main,
               }
    
    def display_menu(self):
        system('cls')
        print('-'*30)
        print("Menu:")
        print("1 Add Pokemon")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("0. Exit")
        print('-'*30)
        print("Select an option to proceed: ")

    def process_job(self):
            self.display_menu()
            choice = input().strip()
            system('cls')
            if choice == '0':
                raise KeyboardInterrupt
            elif any(choice == key for key in self.jobs):
                self.jobs[choice]()
            else:
                print("Invalid choice. Please try again.\n")
                sleep(1)
                system('cls')

    def main(self):
        while True:
            try:
                self.process_job()
                system('cls')
            except KeyboardInterrupt:
                system('cls')
                print("Exiting program. Goodbye!")
                break

        

if __name__ == "__main__":
    Main().main()
