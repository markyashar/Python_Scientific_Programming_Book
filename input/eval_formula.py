"""
Another important example on usefulness of eval is to turn formulas,
given as input, into mathematics in this program.
"""

formula = raw_input('Give a formula involving x: ')   
x = eval(raw_input('Give x: '))
from math import *   # make all math functions available
result = eval(formula)
print '%s for x=%g yields %g' % (formula, x, result)

"""
First, ask user to provide a formula, e.g., 2*sin(x)+1. Result is a string object
referred to by 'formula' variable. Then, we ask for an 'x' value, typically a real
number resulting in a 'float' object. The key statement involves 'eval(formula)',
which in present example evaluates the expression 2*sin(x)+1. The 'x' variable
is defined, & 'sin' function is also defined because of the 'import' statement.

EXAMPLE RUN:

bash-3.2$ python eval_formula.py
Give a formula involving x: 2*sin(x)+1
Give x: 3.14
2*sin(x)+1 for x=3.14 yields 1.00319

bash-3.2$ python eval_formula.py
Give a formula involving x: 5+x**2-cos(x**3)            
Give x: 56
5+x**2-cos(x**3) for x=56 yields 3140.44

"""
