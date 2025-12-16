'''Pokedex package initializer'''
from gc import get_stats
from .database import Database 
from .pokemon import Pokemon
from .stats import stats


get_pokemon = Database().get_pokemon
fetch_one = Database().fetchone
exist_in_db = Database().exists_in_db
add_pokemon = Database().add_pokemon
update_stats = Database().update_stats

get_stats = Database().get_stats


