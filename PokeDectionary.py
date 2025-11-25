choice = input("Enter Choice: ")

while True:
    try:
        choice = int(choice)

        if choice == 1:
            print("You chose 1")
            break

        elif choice == 2:
            print("You chose 2")
            break

        elif choice == 3:
            print("You chose 3")
            break

        elif choice == 4:
            print("You chose 4")
            break

        elif choice == 0:
            print("Exiting...")
            break
    except ValueError:
         print("Invalid input. Please enter a number between 0 and 4.")
   
    