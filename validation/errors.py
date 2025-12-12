'''`Module for error handling decorators for Pokemon attributes'''

from sqlite3 import Error as sqlite3_error

'''Custom Error Classes'''

class EmptyFieldError(Exception):
    '''Custom error for empty fields'''
    def __init__(self, message="This field cannot be empty!"):
        self.message = message
        super().__init__(self.message)

class OutOfDexRangeError(Exception):
    '''Custom error for out of Pokedex range'''
    def __init__(self, message="Number is out of Pokedex range!"):
        self.message = message
        super().__init__(self.message)

class InvalidValueError(Exception):
    '''Custom error for invalid Pokemon types'''
    def __init__(self, message="Invalid value provided!"):
        self.message = message
        super().__init__(self.message)

class DuplicateValueError(Exception):
    '''Custom error for duplicate Pokemon types'''
    def __init__(self, message="Duplicate value provided!"):
        self.message = message
        super().__init__(self.message)

class BackToStart(Exception):
    '''Custom error to return to the start of the program'''
    def __init__(self, message="Returning to start..."):
        self.message = message
        super().__init__(self.message)


