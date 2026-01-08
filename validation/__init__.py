"""
Validation package for Pokemon data.
"""
from .validators import (
    validate_name, 
    validate_number,
    set_type, 
    set_ability, 
    set_stat, 
)

from tools import validation_loop
#Expose constants here for backward compatibility:
from pokedex.constants import ABILITIES, NUM_OF_POKEMON, TYPE_LIST, DEFAULT

__all__ = [
    'validate_name', 
    'validate_number', 
    'set_type', 
    'set_ability', 
    'set_stat', 
    'validation_loop',
    'ABILITIES', 
    'NUM_OF_POKEMON', 
    'TYPE_LIST', 
    'DEFAULT'
]