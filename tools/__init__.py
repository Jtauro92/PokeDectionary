import os
from time import sleep
               
def clear_console():
    """Clears the console screen."""
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def pokemon_generator():
    count = 1
    while True:
        if count > NUM_OF_POKEMON:
            count = 0
        pkmn = get_pokemon(count)
        if pkmn is None:
            count += 1
        else:
            yield pkmn
            count += 1
