'''Module containing validation decorators for Pokemon attributes'''
from functools import wraps
from typing import Callable, Any
from tools import sleep, clear_console
from .constants import ABILITIES, NUM_OF_POKEMON, TYPE_LIST


def validate_name(func: Callable[[Any, str], None]) -> Callable[[Any, str], None]:
    '''Function to validate and set a Pokemon's name'''

    @wraps(func)  # Preserve metadata of the original function
    def wrapper(self, value: str):
        if not value:
            return func(self, None)

        # Standardize input
        name = value.strip().title()

        # Check for '0' skip/default convention if intended, 
        # based on original code: if value == '0': name = value
        if name == '0':
            return func(self, name)

        if name.isnumeric():
            raise ValueError("Names cannot be numerical!")



        return func(self, name)

    return wrapper


def validate_number(func: Callable[[Any, int], None]) -> Callable[[Any, Any], None]:
    '''Function to validate and set a Pokemon's Number'''

    @wraps(func)
    def wrapper(self, value: Any):
        if not value:
            return func(self, None)

        if isinstance(value, str):
            value = value.strip()
            if not value:
                raise ValueError("Number cannot be empty!")
        
        try:
            number = int(value)
        except (ValueError, TypeError) as ne:
            raise ValueError(f"Number must be an integer. Error: {ne}")

        # Check for '0' skip convention
        if number == 0:
            # Original code: if value != 0: check range. 
            # If 0, it just calls func(self, 0)
            pass 
        elif not (1 <= number <= NUM_OF_POKEMON):
            raise ValueError(f"Number must be between 1 and {NUM_OF_POKEMON}!")

        return func(self, number)
        
    return wrapper


def set_type(func: Callable[[Any, str], None]) -> Callable[[Any, str], None]:
    '''Function to validate and set a Pokemon's Type'''

    @wraps(func)
    def wrapper(self, value: str):
        if not isinstance(value, str):
            return func(self, value)

        value = value.strip().upper()
        
        if value == '0':
            return # Abort/Skip

        if not value:
             raise ValueError("Type cannot be empty!")

        if value not in TYPE_LIST:
            raise ValueError("This type does not exist!")

        # Check for duplicate types
        # Note: This prevents setting type1 to "FIRE" if type2 is "FIRE".
        # It also prevents setting type1 to "FIRE" if type1 is already "FIRE" (which is fine, but maybe redundant).
        if value in [self.type1, self.type2]:
            raise ValueError("Duplicate types are not allowed!")
           
        return func(self, value)
        
    return wrapper


def set_ability(func: Callable[[Any, str], None]) -> Callable[[Any, str], None]:
    ''' Function to validate and set a Pokemon's ability'''

    @wraps(func)
    def wrapper(self, value: str):
        if not isinstance(value, str):
            return func(self, value)

        value = value.strip().title()

        if value == '0':
            return # Abort/Skip

        if not value:
            raise ValueError("Ability cannot be empty!")
            
        if value not in ABILITIES:
            raise ValueError("This ability does not exist!")

        # Check for duplicate abilities
        if value in [self.ability1, self.ability2, self.hidden_ability]: 
            raise ValueError("Duplicate abilities are not allowed!")

        return func(self, value)
        
    return wrapper


def set_stat(func: Callable[[Any, int], None]) -> Callable[[Any, Any], None]:
    '''Function to validate and set a Pokemon's Stat'''
    
    @wraps(func)
    def wrapper(self, value: Any):
        if value == '' or value is None:
             raise ValueError("Stat cannot be empty!")

        try:
            stat = int(value)
        except (ValueError, TypeError):
            raise ValueError("Stat must be an integer")

        if stat == 0:
            return # Abort/Skip

        # Check if stat is within valid range
        if stat not in range(1, 800):
            raise ValueError("Stat must be between 1 and 800!")
            
        return func(self, stat)
        
    return wrapper

class ValidatedProperty:
    """Descriptor to handle validated attributes."""
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        @self.validator
        def setter(inst, val):
            setattr(inst, self.private_name, val)
        setter(instance, value)


__all__ = ['validate_name', 'validate_number', 'set_type', 'set_ability', 'set_stat', 'validation_loop', 'sleep', 'clear_console', 'ABILITIES', 'NUM_OF_POKEMON', 'TYPE_LIST', 'DEFAULT']