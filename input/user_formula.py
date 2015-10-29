"""
The exec function executes a string containing arbitrary Python code, not only as an expression.
Suppose the user can write a formula as input to the program, & that we want to turn this formula
into a callable Python function...
"""
import math
from math import *
formula = raw_input('Write a formula involving x: ')
code = """
def f(x):
    return %s
""" % formula
exec(code)
# We add a while loop such that we can provide x values and get f(x) evaluated:
x = 0
while x is not None: 
    x = eval(raw_input('Give x (None to quit): '))
    if x is not None:
        print 'f(%g)=%g' % (x, f(x))
   
"""
Example: Writing sin(x)*cos(3*x) + x**2 as the formula, we would like to get a function:

def f(x):
    return sin(x)*cos(3*x) + x**2

So, in other words, if we respond w/the text sin(x)*cos(3*x) + x**2 to the quesiton,
'formula' will hold this text, which's inserted into the code string such that it becomes

def f(x):
    return sin(x)*cos(3*x) + x**2

Thereafter, exec(code) executes the code as if we had written the contents of the code string
directly into the program by hand. With this technique, we can turn any user-given formula into
a Python function.

As long as we provide numbers as input for x, we evalute the f(x) function, but when we provide the text
'None', x becomes a 'None' object and the test in the whil loop fails, i.e., the loop terminates.

SAMPLE runs:

bash-3.2$ python user_formula.py
Write a formula involving x: x**4 + x
Give x (None to quit): 1
f(1)=2
Give x (None to quit): 4
f(4)=260
Give x (None to quit): 2
f(2)=18
Give x (None to quit): None


bash-3.2$ python user_formula.py
Write a formula involving x: sin(x)*cos(3*x) + x**2
Give x (None to quit): 1
f(1)=0.16695
Give x (None to quit): 4
f(4)=15.3614
Give x (None to quit): 2
f(2)=4.87308
Give x (None to quit): None
bash-3.2$ 

"""
