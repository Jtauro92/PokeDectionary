import os
from pathlib import Path

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
ABILITIES_FILE = BASE_DIR / "abilities.txt"

ABILITIES = []
if ABILITIES_FILE.exists():
    with open(ABILITIES_FILE, "r") as file:
        content = file.read()
        if content:
            ABILITIES = [ability.strip().title() for ability in content.split(",")]
else:
    # Fallback or empty if file missing (prevents crash on import)
    ABILITIES = []

if __name__ == "__main__":
    print(ABILITIES)