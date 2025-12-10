from os import system
from time import sleep
import setters
from validation.error_handling import (validation_loop as vl, 
                                       EmptyFieldError as ef,
                                       OutOfDexRangeError as odr,
                                       InvalidValueError as iv,
                                       DuplicateValueError as dv,
                                       BackToStart,
                                       )
from sqlite3 import Error as sql_error
