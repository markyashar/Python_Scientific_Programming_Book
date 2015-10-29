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
x = zeros(n)
"""

nrep = 80  # repeat x*x and x**2 nrep times

t = timeit.Timer('x*x', setup=initcode)
t1 = t.timeit(nrep)
t = timeit.Timer('x**2', setup=initcode)
t2 = t.timeit(nrep)
print 't2(x**2)/t1(x*x) = ', t2/t1
print 'It looks like x**2 is more efficient than x*x for a large array x (e.g., length of array n = 1000000).'

"""
EXAMPLE OUTPUT:

bash-3.2$ python time_test.py
t2(x**2)/t1(x*x) =  0.986373068346
It looks like x**2 is more efficient than x*x for a large array x (e.g., length of array n = 1000000).

"""
