class MainMenu(object):
    def display_menu():
        pass

class StatsMenu:
    def __init__(self):
          pass
    def stats_menu(self, pkmn):

        return "\n".join([f"--- Update {pkmn.name}'s Stats ---\n", 
                        f"1. HP: {pkmn.stats.hp or ''} ", 
                        f"2. Attack: {pkmn.stats.atk or ''}", 
                        f"3. Defense: {pkmn.stats.defn or ''}", 
                        f"4. Special Attack: {pkmn.stats.spatk or ''}", 
                        f"5. Special Defense: {pkmn.stats.spdef or ''}", 
                        f"6. Speed: {pkmn.stats.speed or ''}",
                        "7. Save", 
                        "0. Cancel", 
                        "\n------ Enter your choice ------"])

class AddNewMenu:
    def __init__(self,pkmn):

        self.menu =    [f"--------- Add Pokemon ---------\n",
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
                         "\n------ Enter your choice ------"]

    def __str__(self):
        return "\n".join(self.menu)

class SearchDex:
    def __init__(self):
        pass









if __name__ == "__main__":
    pokemon = ("Pikachu", 0, "Electric", "fire", "Static", None, "Lightning Rod")
    menu = SearchDex().menu
    menu()






