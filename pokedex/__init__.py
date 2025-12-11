from validation import set_name, set_number, set_type, set_ability # Import validation decorators

from .database import Database
get_pokemon = Database().get_pokemon
fetch_one = Database().fetchone
exist_in_db = Database().exists_in_db
add_pokemon = Database().add_pokemon

from .pokemon import Pokemon


