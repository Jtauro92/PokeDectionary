from .menus import StatsMenu

stats_menu = StatsMenu().stats_menu


def show(values:tuple):
    '''Method to display the Pokemon's details in a formatted manner.'''
    #retrieve details from the database
    (name, number, t1, t2, a1, a2, ha, 
        hp, atk, defn, spatk, spdef, speed) = values

    #start the formatted output
    output = f"*----- {name} #{number:04} -----*\n"

    #build type string
    type_str = f"Type: {t1}"
    if t2 is not None:
        type_str += f" / {t2}"

    output += type_str + "\n" #append type string to output

    #build abilities strings
    output += f"Ability #1: {a1}\n"
    ability2_str = "Ability #2: "
    if a2:
        ability2_str += a2
    output += ability2_str + "\n"
    hidden_ability_str = "Hidden Ability: "
    if ha:
        hidden_ability_str += ha
    output += hidden_ability_str + "\n"

    stats_output =( '*--------Stats--------*\n' +
                        f"HP: {hp}\nATK: {atk}\nDEF: {defn}\n" +
                        f"SP.ATK: {spatk}\nSP.DEF: {spdef}\nSPEED: {speed}")

    output += stats_output.center(70)  # Center the stats output
    print(output)