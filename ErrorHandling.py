'''`Module for error handling decorators for Pokemon attributes'''



#Constants
from ast import Pass


NUM_OF_POKEMON = 1025
TYPE_LIST = [
    "NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING",
    "POISON", "GROUND", "FLYING", "PSYCHIC", "BUG", "ROCK", "GHOST",
    "DRAGON", "DARK", "STEEL", "FAIRY"
]

with open("abilities.txt", "r") as file:
    abilities = file.read().split(",")
    ABILITIES = [ability.strip() for ability in abilities]
'''Custom Error Classes'''

class EmptyFieldError(ValueError):
    '''Custom error for empty fields'''

class OutOfDexRangeError(ValueError):
    '''Custom error for out of Pokedex range'''

class FakeTypeError(ValueError):
    '''Custom error for invalid Pokemon types'''
class EmptyTypeError(ValueError):
    '''Custom error for empty Pokemon types'''

class DuplicateTypeError(ValueError):
    '''Custom error for duplicate Pokemon types'''

class FakeAbilityError(ValueError):
    '''Custom error for invalid Pokemon abilities'''

class DuplicateAbilityError(ValueError):
    '''Custom error for duplicate Pokemon abilities'''

'''Decorator Functions'''

'''Function to validate and set a Pokemon's name'''
def set_name(func):
    def wrapper(self,value):
        name = value.title().strip()
        if name.isnumeric():
            raise ValueError("Names cannot be numerical!")
        
        elif name.strip() == '':
            raise EmptyFieldError("Names cannot be empty!!")
            
        return func(self,name)
    return wrapper

'''Function to validate and set a Pokemon's number'''
def set_number(func):
    def wrapper(self,value):

        # Validate input is numeric and not empty
        if value.strip() == '':
            raise EmptyFieldError("Number cannot be empty!")

        elif (value.isnumeric()):
            number = int(value)
        else:
            raise ValueError("Number must be an interger")

        # Check if number is within valid range
        if number not in range(1, NUM_OF_POKEMON + 1):
            raise OutOfDexRangeError(f"Number must be between 1 and {NUM_OF_POKEMON}!")
            
        return func(self,number)
    return wrapper


'''Function to validate and set a Pokemon's Type'''
def set_type(func):
    def wrapper(self,value):

        # Standardize input, return None if not a string
        try:
            value = value.upper().strip()
        except AttributeError:
           return

        # Check if type exists
        if value != '':
            if not (value in TYPE_LIST):
                    raise FakeTypeError("This type does not exist!")
        else:
            raise EmptyTypeError("Type cannot be empty!")

        # Check for duplicate types
        if ([self.type1].count(value) == 0): #Pass if not duplicate
            pass
        else:
            value = None 
            
        return func(self,value)
    return wrapper


''' Function to validate and set a Pokemon's ability'''
def set_ability(func):

    def wrapper(self,value):

        try:
            value = value.title().strip()
        except AttributeError:
             pass #Return None if not a string

        if (value not in ABILITIES):
            raise FakeAbilityError("This ability does not exist!")

        elif ([self.ability1,self.ability2,self.hidden_ability].count(value) == 0): 
            pass #Pass if not duplicate
        else:
            value = None

        return func(self,value)
    return wrapper


def validation_loop(setter_method):
    def wrapper(self):
        while True:
            try:
                setter_method(self)
                break
            except (ValueError, EmptyFieldError, OutOfDexRangeError, FakeTypeError, DuplicateTypeError, FakeAbilityError, DuplicateAbilityError) as e:
                print(e)
                continue
    return wrapper
