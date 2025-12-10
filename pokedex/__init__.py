from validation.setters import (set_name, set_number, set_type, set_ability)
from .database import Database as db
get_pokemon = db().get_pokemon
