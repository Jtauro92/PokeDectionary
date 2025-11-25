from Pokemon import Pokemon as pk

np = pk()

class add_new(pk):
    def __init__(self):
        super().__init__()

    def add_name(self):
        try:
            self.name = input("Enter name: ")
        except ValueError:
            print("Incorrect Value")
        return self.name

            

if __name__ == "__main__":
    p = add_new()
    p.add_name()
    print(p)



