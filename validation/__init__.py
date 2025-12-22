from tools import *
from .constants import ABILITIES, NUM_OF_POKEMON, TYPE_LIST
from _collections_abc import Callable

'''Decorator Functions'''
def set_name(func:Callable[[str], str]) -> Callable[[str], str]:
    '''Function to validate and set a Pokemon's name'''

    def wrapper(self, value: str):
        '''Wrapper function to validate name input'''
        
        name = value.title().strip()

        if name == '':
            raise ValueError("Name cannot be empty!")

        elif name.isnumeric():
            if value == '0':
                return
            else:
                raise ValueError("Names cannot be numerical!")
            
        return func(self,name)
    return wrapper

# Function to validate and set a Pokemon's number
def set_number(func):
    def wrapper(self,value):

        # Validate input is numeric and not empty
        if value == '':
            raise ValueError("Number cannot be empty!")

        try:
            number = int(value)
            if number == 0:
                return
        except:
            raise ValueError("Number must be an interger")

        # Check if number is within valid range
        if number not in range(1, NUM_OF_POKEMON + 1):
            raise ValueError(f"Number must be between 1 and {NUM_OF_POKEMON}!")
            
        return func(self,number)
    return wrapper



def set_type(func):
    '''Function to validate and set a Pokemon's Type'''
    def wrapper(self,value):

        # Standardize input, return None if not a string
        try:
            value = value.upper().strip()
            if value == '0':
                return
            # Check if type exists
            if value != '':
                if value not in TYPE_LIST:
                    raise ValueError("This type does not exist!")

                #Check for duplicate types
                elif not ([self.type1, self.type2].count(value) == 0):
                    raise ValueError("Duplicate types are not allowed!")
            
            else:
                raise ValueError #Return None if empty string
        
        except AttributeError: 
            pass #Return None if not a string
           
        return func(self,value)
    return wrapper


def set_ability(func):
    ''' Function to validate and set a Pokemon's ability'''

    def wrapper(self, value:str):
        "wrapper function to validate ability input"
        try:
            value = value.title().strip()

            if value == '0':
                return

            #Check for empty string
            if value != '':
                
                #Raise error if ability1 is empty
                if value not in ABILITIES:
                    raise ValueError("This ability does not exist!")

                #Check for duplicate abilities
                elif ([self.ability1,self.ability2,self.hidden_ability].count(value) > 0): 
                    raise ValueError("Duplicate abilities are not allowed!")
            
            else:
                raise ValueError #Return None if empty string

        except AttributeError:
            pass #Return None if not a string

        return func(self,value)
    return wrapper

def set_stat(func):
    def wrapper(self,value):
        # Validate input is numeric and not empty
        if value == '':
            raise ValueError("Stat cannot be empty!")
        try:
            stat = int(value)
            if stat == 0:
                return
        except:
            raise ValueError("Stat must be an interger")

        # Check if stat is within valid range
        if stat not in range(1, 800):
            raise ValueError("Stat must be between 1 and 800!")
            
        return func(self,stat)
    return wrapper

'''Function to create a validation loop for setter methods'''
def validation_loop(setter_method):
    def wrapper(self):
        while True:
            try:
                clear_console()
                setter_method(self)
                break
            except ValueError as e:
                clear_console()
                print(e)
                sleep(1)
                continue
    return wrapper

__all__ = [sleep, clear_console, ABILITIES, NUM_OF_POKEMON, TYPE_LIST]