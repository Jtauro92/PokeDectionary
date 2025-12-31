class MainMenu(object):
    def display_menu():
        pass

class StatsMenu:
    def __init__(self):
          pass
    def stats_menu(self, pkmn):
        menu = f"--- Update {pkmn.name}'s Stats ---\n\n"
        menu_options = [f"1. HP: {pkmn.stats.hp or ''} ", "2. Attack: ", "3. Defense: ", "4. Special Attack: ", "5. Special Defense: ", "6. Speed: ",
                        "7. Save", "0. Cancel", "\n------ Enter your choice ------"]

        if pkmn.stats.atk is not None:
            menu_options[1] += f"{pkmn.stats.atk}"
        if pkmn.stats.defn is not None:
            menu_options[2] += f"{pkmn.stats.defn}"
        if pkmn.stats.spatk is not None:
            menu_options[3] += f"{pkmn.stats.spatk}"
        if pkmn.stats.spdef is not None:
            menu_options[4] += f"{pkmn.stats.spdef}"
        if pkmn.stats.speed is not None:
            menu_options[5] += f"{pkmn.stats.speed}"

        menu += "\n".join(menu_options)
        return menu

class AddNew:
    def __init__(self):
        pass
    def menu(self,pkmn):

        menu = f"--------- Add Pokemon ---------\n\n"
        menu_options = ["1. Name: ", "2. Number: ", "3. Type: ", "4. Type 2: ",
                       "5: Ability: ", "6: Ability 2: ", "7: Hidden Ability: ","-"*30,
                       "8: Save", "0: Return to Main Menu", "\n------ Enter your choice ------"]

        if pkmn.name != "Default":
            menu_options[0] += f"{pkmn.name}"

        if pkmn.number != 0:
            menu_options[1] += f"{pkmn.number:04}"

        if pkmn.type1 != "Default":
            menu_options[2] += f"{pkmn.type1}"
        if pkmn.type2:
            menu_options[2] += f" / {pkmn.type2}"

        if pkmn.ability1 != "Default":
            menu_options[4] += f"{pkmn.ability1}"
        if pkmn.ability2:
            menu_options[5] += f"{pkmn.ability2}"
        if pkmn.hidden_ability:
            menu_options[6] += f"{pkmn.hidden_ability}"

        menu += "\n".join(menu_options)
        return menu

class SearchDex:
    def __init__(self):
        pass









if __name__ == "__main__":
    pokemon = ("Pikachu", 0, "Electric", "fire", "Static", None, "Lightning Rod")
    menu = SearchDex().menu
    menu()






