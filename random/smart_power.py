"""
Is x*x more efficient than x**2 for a large array x?

This program applies the timeit module to investigate this
question.
"""
import timeit
n = 1000000  # length of array

initcode = """
from numpy import zeros
from __main__ import n    

# Relevant Example: If you want to time a function, say f, defined in same program as where
# you have timeit call, setup procedure must import f and perhaps other variables form 
# program, as exemplified in:
# 
# t = timeit.Timer('f(a,b)', setup='from __main__ import f, a, b')
#
# Here, f, a, & b are names initialized in main program.

x = zeros(n)
"""

nrep = 80  # repeat x*x and x**2 nrep times

t = timeit.Timer('x*x', setup=initcode)
t1 = t.timeit(nrep)
t = timeit.Timer('x**2', setup=initcode)
t2 = t.timeit(nrep)
print 'x*x and x**2 repeated %d times' % nrep
print 'x**2 vs x*x for arrays of length %d, t2/t1 = ' % n, t2/t1
print '\n'

# Repeat the test for math.pow and ** for scalars

nrep = 8000000

t = timeit.Timer('2.0*2.0')
t1 = t.timeit(nrep)
t = timeit.Timer('2.0**2')
t2 = t.timeit(nrep)
print '2.0*2.0 and 2.0**2.0 repeated %d times' % nrep
print '2.0**2 vs 2.0*2.0 for arrays of length %d, t2/t1 = ' %n, t2/t1
print '\n'
t = timeit.Timer('2.0**2.0')
t2 = t.timeit(nrep)
t = timeit.Timer('pow(2.0,2)', setup='from math import pow')
t2 = t.timeit(nrep)
print 'pow(2.0,2) and 2.0*2.0 repeated %d times' % nrep
print 'pow(2.0,2) vs 2.0*2.0 for arrays of lenght %d, t2/t1 = ' %n, t2/t1

"""
EXAMPLE OUTPUT:

bash-3.2$ python smart_power.py
x*x and x**2 repeated 80 times
x**2 vs x*x for arrays of length 1000000, t2/t1 =  0.987484471368


2.0*2.0 and 2.0**2.0 repeated 8000000 times
2.0**2 vs 2.0*2.0 for arrays of length 1000000, t2/t1 =  1.03634776292


pow(2.0,2) and 2.0*2.0 repeated 8000000 times
pow(2.0,2) vs 2.0*2.0 for arrays of lenght 1000000, t2/t1 =  6.03099178832
bash-3.2$ 
"""
