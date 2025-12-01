'''`Module for error handling decorators for Pokemon attributes'''



#Constants
from ast import Pass


NUM_OF_POKEMON = 1025
TYPE_LIST = [
    "NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING",
    "POISON", "GROUND", "FLYING", "PSYCHIC", "BUG", "ROCK", "GHOST",
    "DRAGON", "DARK", "STEEL", "FAIRY"
]

class EmptyFieldError(ValueError):
    '''Custom error for empty fields'''

class OutOfDexRangeError(ValueError):
    '''Custom error for out of Pokedex range'''

class FakeTypeError(ValueError):
    '''Custom error for invalid Pokemon types'''

class DuplicateTypeError(ValueError):
    '''Custom error for duplicate Pokemon types'''

class FakeAbilityError(ValueError):
    '''Custom error for invalid Pokemon abilities'''





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
        if (1 <= number <= NUM_OF_POKEMON):
            pass
        else:
            raise OutOfDexRangeError(f"Number must be between 1 and {NUM_OF_POKEMON}!")
            
        return func(self,number)
    return wrapper


'''Function to validate and set a Pokemon's Type'''
def set_type(func):
    def wrapper(self,value):
        value = value.upper().strip()

        # Check if type exists
        if (value in TYPE_LIST):
            pass
        else:
            raise FakeTypeError("This type does not exist!")

        # Check for duplicate types
        if ([self.type1].count(value) > 0):
            raise DuplicateTypeError(f"This type ({self.type1}) is already assigned to this Pokemon!")

        return func(self,value)
    return wrapper


''' Function to validate and set a Pokemon's ability'''
def set_ability(func):

    def wrapper(self,value):
        value = value.title().strip()

        with open("abilities.txt", "r") as file:
            abilities = file.read().split(",")
            abilities = [ability.strip() for ability in abilities]

        if (value not in abilities):
            raise FakeAbilityError("This ability does not exist!")

        elif ([self.ability1,self.ability2,self.hidden_ability].count(value) > 0): 
            raise ValueError("Ability already assigned to this Pokemon!")

        return func(self,value)
    return wrapper
