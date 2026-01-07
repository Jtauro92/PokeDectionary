
class Menu:
    def __init__(self, menu_items = []):
        self.menu_items = menu_items
    def __str__(self):
        return "\n".join(self.menu_items)

class MainMenu(Menu):
    def __init__(self):
        super().__init__(["------- Pokedex Main Menu -------\n",
                          "1. Add New Pokemon",
                          "2. Search Pokedex",
                          "3. Update Stats",
                          "4. Delete Pokemon", 
                          "0. Exit",
                          "\n------ Enter your choice ------"])

class StatsMenu(Menu):
    def __init__(self, pkmn):
        super().__init__([f"--- Update {pkmn.name}'s Stats ---\n", 
                        f"1. HP: {pkmn.stats.hp or ''} ", 
                        f"2. Attack: {pkmn.stats.atk or ''}", 
                        f"3. Defense: {pkmn.stats.defn or ''}", 
                        f"4. Special Attack: {pkmn.stats.spatk or ''}", 
                        f"5. Special Defense: {pkmn.stats.spdef or ''}", 
                        f"6. Speed: {pkmn.stats.speed or ''}",
                        "7. Save", 
                        "0. Cancel", 
                        "\n------ Enter your choice ------]"])


class AddNewMenu(Menu):
    def __init__(self,pkmn):
        super().__init__([f"--------- Add Pokemon ---------\n",
                        f"1. Name: {pkmn.name or ''}",
                        f"2. Number: {pkmn.number or ''}",
                        f"3. Type: {pkmn.type1 or ''}" if not (not pkmn.type1 and pkmn.type2) else pkmn.type2,
                        f"4. Type 2: {pkmn.type2 or ''}",
                        f"5: Ability: {pkmn.ability1 or ''}",
                        f"6: Ability 2: {pkmn.ability2 or ''}",
                        f"7: Hidden Ability: {pkmn.hidden_ability or ''}",
                        "-"*30,
                        "8: Save",
                        "0: Return to Main Menu",
                         "\n------ Enter your choice ------"])

class SearchDex(Menu):
    def __init__(self):
        super().__init__(["--------- Search Pokedex ---------\n",
                          "1. Search by Name or Number", 
                          "2. Search by Type",
                          "3. View All Pokemon", 
                          "0. Return to Main Menu", 
                          "\n------ Enter your choice ------\n"])




if __name__ == "__main__":
    pokemon = ("Pikachu", 0, "Electric", "fire", "Static", None, "Lightning Rod")
    menu = SearchDex
    print(menu())






