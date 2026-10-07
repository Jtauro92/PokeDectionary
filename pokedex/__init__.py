'''Pokedex package initializer'''
from .database import Database 
from .constants import NUM_OF_POKEMON

_db = Database()
get_pokemon = _db.get_pokemon
fetch_one = _db.fetchone
add_pokemon = _db.add_pokemon
update_stats = _db.update_stats
get_stats = _db.get_stats
update_stats = _db.update_stats



def pokemon_generator():
    count = 1
    while True:
        if count > NUM_OF_POKEMON:
            count = 1
        pkmn = get_pokemon(count)
        if pkmn:
           yield pkmn
        count += 1


