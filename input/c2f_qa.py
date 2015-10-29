C = raw_input('C=? ')     # In general, the raw_input function takes a string as argument, displays this string in the terminal window, waits
C = float(C)              # until user presses Return key, & then returns a string object containing the sequence of characters that the user
F = (9./5)*C + 32         # typed in.
print F

"""
EXAMPLE OUTPUT:

bash-3.2$ python c2f_qa.py
C=? 45
113.0

-----------------

We may ask user a question C=? & wait for user to enter a number. Program can then read this number and store it in
a variable C. These actions are performed by the statement 'C = raw_input('C=? ')

The raw_input function always returns the user input as a string object, i.e., the variable C above refers to a string
object. If we want to compute w/this C, must convert the string to a floating-point number: C = float(C).

In this particular example, the raw_input function reads the characters 45 from keyboard & returns string '45',
which we refer to by the variable C. Then we create a new 'float' object by 'float(C)' & let the name 'C' refer
to this float object, w/value 45.

"""
