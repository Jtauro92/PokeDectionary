from time import sleep
from os import system
from sqlite3 import Error as sqlite3_error

#Constants
NUM_OF_POKEMON = 1025
TYPE_LIST = [
    "NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING",
    "POISON", "GROUND", "FLYING", "PSYCHIC", "BUG", "ROCK", "GHOST",
    "DRAGON", "DARK", "STEEL", "FAIRY"
]

# Load abilities from the abilities.txt file
with open("validation/abilities.txt", "r") as file:
    ABILITIES = [ability.strip() for ability in file.read().split(",")]

from .errors import (EmptyFieldError , OutOfDexRangeError , 
                     DuplicateValueError, InvalidValueError, BackToStart)
from .decorators import (set_name, set_number, set_type, set_ability, 
                         validation_loop)
__all__ = [EmptyFieldError, OutOfDexRangeError,
           DuplicateValueError, InvalidValueError, BackToStart, sleep, system, ABILITIES, NUM_OF_POKEMON, TYPE_LIST]