from os import system

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

