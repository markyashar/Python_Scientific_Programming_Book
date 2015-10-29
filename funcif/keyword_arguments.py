"""
Keyword Arguments: Function arguments w/default values are called keyword arguments, & they help document meaning of arguments
in function calls. They also make it possible to specify just a subset of arguments in function calls. They also make it possible
to specify just a subset of arguments in function calls.
"""
from math import exp, sin, pi

def f(x, A=1, a=1, w=pi):
    return A*exp(-a*x)*sin(w*x)

f1 = f(0)
x2 = 0.1
f2 = f(x2, w=2*pi)
f3 = f(x2, w=4*pi, A=10, a=0.1)
f4 = f(w=4*pi, A=10, a=0.1, x=x2)

print f1, f2, f3, f4
"""
The sequence of keyword arguments can be arbitrary, & keyword arguments that are not listed in the call get their default values according
to the function definition. The "non-keyword arguments" are called positional arguments, which's x in this example. Positional arguments must
be listed before keyword arguments. However, a positional argument can also appear as 'name=value' in the call (see last line above), & this
last syntax allows any positional argument to be listed anywhere in the call.

OUTPUT:

bash-3.2$ python keyword_arguments.py
0.0 0.531850090044 9.41593345844 9.41593345844

"""
