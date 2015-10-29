# The Main Program

# In programs containing functions we often refer to part of program that's called 'main program'.
# This is collection of all statements outside the functions, plus definition of all functions.
# Complete example program:

from math import *          # in main

def f(x):                   # in main
    e = exp(-0.1*x)
    s = sin(6*pi*x)
    return e*s

x = 2                       # in main
y = f(x)                    # in main
print 'f(%g)=%g' % (x,y)    # in main

"""
Main program here consists of lines w/comment 'in main'. Execution alwys starts w/1st line
in main program. When function is encountered, its statements are just used to define the
function -- nothing gets computed inside the function before we explicitly call the function,
either from main program or from another function. All variables initialized in main program
become global variables.

Program flow in program above goes as follows:

1. Import function from math module,
2. define a function f(x),
3. define x,
4. call f and execture the function body,
5. define y as value returned from f,
6. print the string.

In point 4 we jump to f function & execute statement inside that function for 1st time.
Then we jump back to main program & assign 'float' object returned from f to y variable.

-------------

EXAMPLE OUTPUT:

bash-3.2$ python main_example.py 
f(2)=-1.20319e-15
"""

 
