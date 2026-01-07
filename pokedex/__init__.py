'''Pokedex package initializer'''
from .database import Database 

from validation import NUM_OF_POKEMON

get_pokemon = Database().get_pokemon
fetch_one = Database().fetchone
exist_in_db = Database().exists_in_db
add_pokemon = Database().add_pokemon
update_stats = Database().update_stats
get_stats = Database().get_stats
update_stats = Database().update_stats


def pokemon_generator():
    count = 1
    while True:
        if count > NUM_OF_POKEMON:
            count = 1
        pkmn = get_pokemon(count)
        if pkmn:
           yield pkmn
        count += 1


