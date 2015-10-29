#x = 1; print 'sin(%g)=%g' % (x, sin(x))

"""
This program will produce an error because sin has not been imported.
To make this program functional do a 'from math import sin'

"""

from math import sin
x = 1; print('sin(%g)=%g' % (x, sin(x)))

"""
OUTPUT:
src/formulas>python python Ex1.7_sin_test.py
sin(1)=0.841471
"""
