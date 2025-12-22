import os
import sys
from time import sleep
from msvcrt import getwch, kbhit
               
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

__all__ = ['clear_console', 'sleep', 'getwch', 'kbhit', 'move_up', 'hide_cursor', 'show_cursor']