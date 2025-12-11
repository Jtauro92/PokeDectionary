from .database import Database
from validation import set_name, set_number, set_type, set_ability

db = Database()
exists_in_db = db.exists_in_db
get_pokemon = db.get_pokemon




