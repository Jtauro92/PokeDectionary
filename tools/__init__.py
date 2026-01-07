import os
import sys
from time import sleep
from msvcrt import getwch, kbhit
from typing import Callable, Any
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

__all__ = ['clear_console', 'sleep',
          'move_up', 'hide_cursor', 'show_cursor', 'validation_loop', 'get_keypress']