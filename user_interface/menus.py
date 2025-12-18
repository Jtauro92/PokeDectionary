class MainMenu(object):
    def display_menu():
        pass

class StatsMenu:
    def stats_menu(name, stats):
        hp,atk, defn, spatk, spdefn, speed = stats
        msg = f"--- Update {name}'s Stats ---\n"
        
        msg+= "1. HP"
        if hp is not None:
            msg += f": {hp}\n"
        else:
            msg+= "\n"

        msg+="2. Attack"
        if atk is not None:
            msg+= f": {atk}\n"
        else:
            msg+= "\n"

        msg+="3. Defense"
        if defn is not None:
            msg+= f": {defn}\n"
        else:
            msg+= "\n"

        msg+="4. Special Attack"
        if spatk is not None:
            msg+= f": {spatk}\n"
        else:
            msg+= "\n"

        msg+="5. Special Defense"
        if spdefn is not None:
            msg+= f": {spdefn}\n"
        else:
            msg+= "\n"

        msg+="6. Speed"
        if speed is not None:
            msg+= f": {speed}\n"
        else:
            msg+= "\n"
        
        msg+="7. Save and Exit\n"
        msg+="0. Return to Main Menu\n"
        msg += "\nSelect a stat to update:\n"

        return msg

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

if __name__ == "__main__":
    pokemon = ("Pikachu", 0, "Electric", "fire", "Static", None, "Lightning Rod")
    menu = AddNew().menu(pokemon)
    print(menu)





