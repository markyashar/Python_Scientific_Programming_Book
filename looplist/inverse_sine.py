# Exercise 2.15 -- Explore the Python Library Reference

"""
Suppose you want to compute the inverse sine funcion: sin^-1(x).
The math module has a function for computing sin^-1(x), but what's
the right name for this function? Read Chapt. 2.6.3 and use the math
entry in the index of the Python Library Reference to find out how to 
comput sin^-1(x). Make a program where you compute sin^-1(x) for n x
values uniformally distributed between 0 and 1, and write out the results
in a nicely formatted table. For each x value, check that the sine of
sin^-1(x) equals x.


"""
from math import asin, pi

n = 10
x_list = [i * 1. / n for i in range(n + 1)]

print '------------------'
print '%-3s %13s ' % ('x', 'arcsin(x)')
for x in x_list:
    print '%-3.2f %12.2f' % (x, asin(x) * 180 / pi)
print '------------------'

"""
Sample run:
python inverse_sin.py
------------------
x       arcsin(x)
0.00         0.00
0.10         5.74
0.20        11.54
0.30        17.46
0.40        23.58
0.50        30.00
0.60        36.87
0.70        44.43
0.80        53.13
0.90        64.16
1.00        90.00
------------------*
"""
