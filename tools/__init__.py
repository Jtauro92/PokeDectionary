import os
from time import sleep

def clear_console():
    """Clears the console screen."""
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

__all__ = ['clear_console', 'sleep']
