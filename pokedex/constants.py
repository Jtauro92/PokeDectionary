import os
from pathlib import Path
import requests

# Constants
NUM_OF_POKEMON = 1025
TYPE_LIST = [
    "NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING",
    "POISON", "GROUND", "FLYING", "PSYCHIC", "BUG", "ROCK", "GHOST",
    "DRAGON", "DARK", "STEEL", "FAIRY"
]
DEFAULT = None

# Dynamically locate the abilities file relative to the project root or this file
# Assuming abilities.txt is in the validation folder as per previous context, 
# or we move it. For now, I'll locate it relative to this file's parent's sibling 'validation'.
BASE_DIR = Path(__file__).resolve().parent
base_url = "https://pokeapi.co/api/v2/ability?limit=100000&offset=0"
response = requests.get(base_url)
if response.status_code == 200:
    data = response.json()
    ABILITIES = [ability['name'].replace('-', ' ').title() for ability in data['results']]
else:
    ABILITIES = []


if __name__ == "__main__":
    print(ABILITIES)