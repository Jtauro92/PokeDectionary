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



