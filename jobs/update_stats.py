
from pokedex import pokemon, update_stats, get_pokemon, Pokemon as pk
from validation import validation_loop as vl, sleep, clear_console
from user_interface import stats_menu as sm


class UpdateStats():
    def __init__(self):
        self.jobs = {'1': self.set_hp, 
                     '2': self.set_atk, 
                     '3': self.set_defn, 
                     '4': self.set_spatk, 
                     '5': self.set_spdef, 
                     '6': self.set_speed
                     }
        self.pokemon = pk()
    @vl
    def set_hp(self):
        self.pokemon.stats.hp = input("Enter HP: ")

    @vl
    def set_atk(self):
        self.pokemon.stats.atk = input("Enter Attack: ")

    @vl
    def set_defn(self):
        self.pokemon.stats.defn = input("Enter Defense: ")

    @vl
    def set_spatk(self):
        self.pokemon.stats.spatk = input("Enter Special Attack: ")

    @vl
    def set_spdef(self):
        self.pokemon.stats.spdef = input("Enter Special Defense: ")

    @vl
    def set_speed(self):
        self.pokemon.stats.speed = input("Enter Speed: ")

    def set_stats(self, pkmn):
        '''Method to set stats for a Pokemon'''
        self.pokemon = pkmn
        if self.pokemon.name =="Default":
            clear_console()
            identifier = input("Enter Pokemon name or number: ").strip()
            if identifier == "0":
                raise ValueError
     
            result = get_pokemon(identifier)
            if result:
                self.pokemon = pk(*result[0:7],result[7:13])
            else:
                clear_console()
                print("Pokemon not found")
                sleep(1)

        while True:
            clear_console()
            print(sm(self.pokemon))
            choice = input()
            if choice in self.jobs:
                self.jobs[choice]()
                clear_console()

            if choice == "7":
                if [*self.pokemon.stats].count(None) > 0:
                    clear_console()
                    print("All stats must be set before exiting")
                    sleep(1)
                else:
                    update_stats(self.pokemon)
                    clear_console()
                    print(f"Stats for {self.pokemon.name} updated successfully!")
                    sleep(1)
                    break

            if choice == "0":
                break

        pkmn = pk()

    
    def main(self):
        while True:
            try:
                self.set_stats()
                cont = input("\nUpdate another Pokemon's stats (PRESS ENTER TO CONTINUE) ").strip().lower()
                if cont != "":
                    break
            except ValueError:
                cont = input("\nPRESS ENTER TO TRY AGAIN OR ANY KEY TO EXIT: ").strip().lower()
                if cont != "":
                    break


if __name__ == "__main__":
    main = UpdateStats().main
    main()
    
                
     
