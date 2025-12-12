from pokedex import update_stats, get_pokemon, stats, Pokemon
from validation import validation_loop as vl

class UpdateStats(stats):
    def __init__(self):
        super().__init__()
        self.jobs = {'1': self.set_hp, 
                     '2': self.set_atk, 
                     '3': self.set_defn, 
                     '4': self.set_spatk, 
                     '5': self.set_spdef, 
                     '6': self.set_speed
                     }
    @vl
    def set_hp(self):
        self.hp = input("Enter HP: ")

    @vl
    def set_atk(self):
        self.atk = input("Enter Attack: ")

    @vl
    def set_defn(self):
        self.defn = input("Enter Defense: ")

    @vl
    def set_spatk(self):
        self.spatk = input("Enter Special Attack: ")

    @vl
    def set_spdef(self):
        self.spdef = input("Enter Special Defense: ")

    @vl
    def set_speed(self):
        self.speed = input("Enter Speed: ")

    def set_stats(self, identifier):
        result = get_pokemon(identifier.strip())
        
        choice = input("Select stat to update: ")
        if choice == '0':
            return

        elif any(choice == key for key in self.jobs):
            self.jobs[choice]()

        else:
            raise ValueError("Invalid choice. Please try again.")

        update_stats(result[1], self.hp, self.atk, self.defn, self.spatk, self.spdef, self.speed)
        print(f"{self.jobs[choice]} updated successfully for {result[0]}.")
    
    def main(self):
        while True:
            try:
                identifier = input("Enter Pokemon name or number to update stats: ")
                if identifier.strip() == '0':
                    break
                self.set_stats(identifier)
            except KeyboardInterrupt:
                print("Exiting update stats.")
                return
     
        

if __name__ == "__main__":
    us = UpdateStats()
    us.set_stats(input("Enter Pokemon name or number to update stats: "))
