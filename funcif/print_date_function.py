# Functions may have no arguments and/or no return value(s):

# A common error is to forget the parentheses: 'print_date' is the function object itself, while 'print_date()'
# is a call to the function.
import time

def print_date():
    """Print the current date in the format 'Jan 07, 2007'."""
    print time.strftime("%b %d, %Y")

# call:
print_date()

"""
OUTPUT

bash-3.2$ python print_date_function.py 
Jun 30, 2015

"""
