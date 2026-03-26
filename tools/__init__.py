import os
import sys
from time import sleep
from msvcrt import getwch, kbhit
from typing import Callable
from functools import wraps
               
def clear_console():
    """Clears the console screen."""
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def clear_line ():
    """Clears the current line in the console."""
    sys.stdout.write('\033[2K\r') # Clear the line
    sys.stdout.flush() # Flush the output buffer

def move_up(lines=1):
    """Moves the cursor up by the specified number of lines."""
    sys.stdout.write(f"\033[{lines}A")
    sys.stdout.flush()

def hide_cursor():
    """Hides the cursor in the console."""
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    """Shows the cursor in the console."""
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def get_keypress():
    """Waits for a keypress and returns the character."""
    if kbhit():
        getwch()
        return getwch()  # Return the actual character

def validation_loop(func: Callable) -> Callable:
    '''Function to create a validation loop for methods'''
    
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        while True:
            try:
                clear_console()
                return func(self, *args, **kwargs)
            except ValueError as e:
                clear_console()
                print(f"Error: {e}")
                # Add sleep to allow user to read the error before clearing
                if hasattr(e, 'message'): # Optional: if you have custom errors
                    pass 
                sleep(1)
    return wrapper

class Table:
    COL_NAMES = ["Ability 1", 
                 "Ability 2", "HAbility", "HP", "Attack", "Defense", "SP.ATK", "SP.DEF", "Speed"]
    COL_WIDTHS = [15, 15, 15, 8, 9, 7, 8, 6, 6]

    def __init__(self, data: object | list[str | int] =[]):
        self._data = data

    @property
    def data(self) -> list[str | int]:
        return self._data

    @data.setter
    def data(self, value: object | list[str | int]):
        if isinstance(value, object):
            self._data = [atr for atr in value]
        elif isinstance(value, list):
            self._data = value
        else:
            raise ValueError("Data must be a string, integer, or list of strings/integers.")

    def __str__(self) -> str:
        header = f"{f'Name: {self.data[0]} | ID: {self.data[1]}':^90}"
        typing = f"{f"Type: {self.data[2]} / {self.data[3]}":^90}" if self.data[3] else f"{f'Type: {self.data[2]}':^90}"
        self.data[5] = self.data[5] if self.data[5] else ""
        self.data[6] = self.data[6] if self.data[6] else ""
        columns = [f"{name:^{width}}" for name, width in zip(self.COL_NAMES, self.COL_WIDTHS)]
        row = [f"{value:^{width}}" for value, width in zip(self.data[4:], self.COL_WIDTHS)]
        separator = "*" + "=" * (sum(self.COL_WIDTHS) + 5) + "*"

        return "\n".join([
            header,
            typing,
            separator,
            "|".join(columns),
            separator,
            "|".join(row),
            ""
        ])

__all__ = ['clear_console', 'sleep',
          'move_up', 'hide_cursor', 'show_cursor', 'validation_loop', 'get_keypress', 'getwch']