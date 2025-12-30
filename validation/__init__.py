'''Module containing validation decorators for Pokemon attributes'''
from tools import *
from .constants import ABILITIES, NUM_OF_POKEMON, TYPE_LIST, DEFAULT
from _collections_abc import Callable


def validate_name(func: Callable[[str], None]) -> Callable[[str], None]:
    '''Function to validate and set a Pokemon's name
        arg: func - callable function to set name
        return: wrapper - callable function that validates name input
    '''
    
    def wrapper(self, value: str):
        '''Wrapper function to validate name input
           arg: self - instance of a class
           arg: value - name to validate
           return: func(self,name) - calls the original function with validated name
        '''
        if value:
            # Standardize input
            name = value.title().strip()

            # Validate name is not empty or numeric
            name_is_empty = name == ''
            name_is_number = name.isnumeric()

            # Raise errors for invalid names
            if name_is_empty:
                raise ValueError("Name cannot be empty!")

            elif name_is_number:
                if value == '0':
                    name = value
                else:
                    raise ValueError("Names cannot be numerical!")
        else:
            name = DEFAULT
            
        return func(self,name)

    return wrapper


def validate_number(func: Callable[[str], None]) -> Callable[[str], None]:
    '''Function to validate and set a Pokemon's Number
       arg: func - callable function to set number
       return: wrapper - callable function that validates number input
    '''

    def wrapper(self,value):
        '''
        Wrapper function to standrdize and validate number input
        arg: self - instance of a class
        arg: value - number to validate
        return: func(self,number) - calls the original function with validated number
        '''
        if value:
            value = value.strip()
            if value == '':
                raise ValueError("Number cannot be empty!")
            try:
                value = int(value)
            except ValueError as ne:
                raise ValueError(f"Number must be an interger. Error: {ne}")

            if value != 0:
                if not (1 <= value <= NUM_OF_POKEMON):
                    raise ValueError(f"Number must be between 1 and {NUM_OF_POKEMON}!")
        else:
            value = DEFAULT

        return func(self,value)
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