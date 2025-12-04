'''`Module for error handling decorators for Pokemon attributes'''

#Constants
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
    def __init__(self, message="This field cannot be empty!"):
        self.message = message
        super().__init__(self.message)

class OutOfDexRangeError(ValueError):
    '''Custom error for out of Pokedex range'''
    def __init__(self, message="Number is out of Pokedex range!"):
        self.message = message
        super().__init__(self.message)

class InvalidValueError(ValueError):
    '''Custom error for invalid Pokemon types'''
    def __init__(self, message="Invalid value provided!"):
        self.message = message
        super().__init__(self.message)

class DuplicateValueError(ValueError):
    '''Custom error for duplicate Pokemon types'''
    def __init__(self, message="Duplicate value provided!"):
        self.message = message
        super().__init__(self.message)


'''Decorator Functions'''
'''Function to validate and set a Pokemon's name'''
def set_name(func):
    def wrapper(self,value):
        name = value.title().strip()

        if name == '':
            raise EmptyFieldError

        elif name.isnumeric():
            if value == '0':
                raise KeyboardInterrupt
            else:
                raise InvalidValueError("Names cannot be numerical!")
            
        return func(self,name)
    return wrapper

'''Function to validate and set a Pokemon's number'''
def set_number(func):
    def wrapper(self,value):
        value=value.strip()

        # Validate input is numeric and not empty
        if value == '':
            raise EmptyFieldError("Number cannot be empty!")

        elif (value.isnumeric()):
            number = int(value)
            if number == 0:
                raise KeyboardInterrupt
        else:
            raise InvalidValueError("Number must be an interger")

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
            if value == '0':
                raise KeyboardInterrupt
            # Check if type exists
            if value != '':
                if value not in TYPE_LIST:
                    raise InvalidValueError("This type does not exist!")
                
                #Check for duplicate types
                elif not ([self.type1, self.type2].count(value) == 0):
                    raise DuplicateValueError
            
            else:
                raise EmptyFieldError #Return None if empty string
        
        except AttributeError: 
            pass #Return None if not a string
           
        return func(self,value)
    return wrapper


''' Function to validate and set a Pokemon's ability'''
def set_ability(func):

    def wrapper(self,value):

        try:
            value = value.title().strip()

            if value == '0':
                raise KeyboardInterrupt

            #Check for empty string
            if value != '':
                
                #Raise error if ability1 is empty
                if value not in ABILITIES:
                    raise InvalidValueError("This ability does not exist!")

                #Check for duplicate abilities
                elif ([self.ability1,self.ability2,self.hidden_ability].count(value) > 0): 
                    raise DuplicateValueError

            else:
                raise EmptyFieldError #Return None if empty string

        except AttributeError:
            pass #Return None if not a string

        return func(self,value)
    return wrapper

'''Function to create a validation loop for setter methods'''
def validation_loop(setter_method):
    def wrapper(self):
        while True:
            try:
                setter_method(self)
                break
            except KeyboardInterrupt:
                print('Goodbye!')
                exit()
            except (OutOfDexRangeError, InvalidValueError, EmptyFieldError, DuplicateValueError) as e:
                print(e)
                continue
    return wrapper
