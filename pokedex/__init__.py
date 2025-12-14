'''Pokedex package initializer'''
from .database import Database 


get_pokemon = Database().get_pokemon
fetch_one = Database().fetchone
exist_in_db = Database().exists_in_db
add_pokemon = Database().add_pokemon
update_stats = Database().update_stats

from .pokemon import Pokemon
from .stats import stats 




