from pokedex.pokemon import Pokemon
from pokedex import get_pokemon, update_stats
from validation import sleep, clear_console
from user_interface import stats_menu


class UpdateStats:
    """Class to handle updating Pokemon stats."""

    def __init__(self):
        self.jobs = {
            '1': ('hp', "Enter HP: "),
            '2': ('atk', "Enter Attack: "),
            '3': ('defn', "Enter Defense: "),
            '4': ('spatk', "Enter Special Attack: "),
            '5': ('spdef', "Enter Special Defense: "),
            '6': ('speed', "Enter Speed: ")
        }
        self.pokemon = Pokemon()

    def _update_stat(self, stat_attr: str, prompt: str):
        """Generic method to update a stat with validation loop."""
        while True:
            try:
                clear_console()
                value = input(prompt)
                setattr(self.pokemon.stats, stat_attr, value)
                break
            except ValueError as e:
                clear_console()
                print(f"Error: {e}")
                sleep(1)

    def _load_pokemon(self):
        """Load a Pokemon from the database if not already loaded."""
        if self.pokemon.name != None:
            return
        while True:
            clear_console()
            identifier = input("Enter Pokemon name or number: ").strip()
            if identifier == "0":
                raise ValueError

            result = get_pokemon(identifier)
            if result:
                # Unpack result to create Pokemon object
                return Pokemon(*result[0:7], result[7:13])
            else:
                clear_console()
                print("Pokemon not found")
                sleep(1)

    def set_stats(self, pkmn=None):
        """Method to set stats for a Pokemon."""
        self.pokemon = pkmn if pkmn else self._load_pokemon()

        while True:
            clear_console()
            print(stats_menu(self.pokemon))
            choice = input()

            if choice in self.jobs:
                stat_attr, prompt = self.jobs[choice]
                self._update_stat(stat_attr, prompt)
                clear_console()

            elif choice == "7":
                if None in self.pokemon.stats:
                    clear_console()
                    print("All stats must be set before exiting")
                    sleep(1)
                else:
                    update_stats(self.pokemon)
                    clear_console()
                    print(f"Stats for {self.pokemon.name} updated successfully!")
                    sleep(1)
                    break

            elif choice == "0":
                break

    def main(self):
        """Main loop for updating stats."""
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
    app = UpdateStats()
    app.main()
