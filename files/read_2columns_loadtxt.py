# Excercise 6.3
# Author: Noah Waterfield Price (w/slight modifications by Mark Yashar, 11/5/2015)

# Look up the documentation of numpy.load.txt function and use it to load file data 
# in Exercise 6.1 into arrays.

"""
The file xy.dat contains 2 columns of numbers, corresponding to x and y coordinates on a curve.
The start of file looks like this:

-1.0000       -0.0000
-0.9933       -0.0087
-0.9867       -0.0179
-0.9800       -0.0274
-0.9733       -0.0374
-0.9667       -0.0477

Make program that reads 1st column into list x & 2nd column into list y. Then convert lists to 
arrays, & plot curve. Print out max. and min. y coordinates.
"""

import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('xy.dat', unpack=True)

print 'Minimum x value = %f' % x.min()
print 'Maximum x value = %f' % x.max()
print 'Minimum y value = %f' % y.min()
print 'Maximum y value = %f' % y.max()

print 'Mean x value = %f' % x.mean()
print 'Standard deviation of x value = %f' % x.std()
print 'Mean y value = %f' % y.mean()
print 'Standard deviation of y value = %f' % y.std()

plt.plot(x, y, color='#053061', linewidth=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('read_2columns_loadtxt.png')
plt.show()


"""
Sample run:
python read_2columns_loadtxt.py
Minimum x value = -1.000000
Maximum x value = 1.000000
Minimum y value = -0.948200
Maximum y value = 0.948200
Mean x value = 0.000000
Standard deviation of x value = 0.579271
Mean y value = 0.000000
Standard deviation of y value = 0.469008

"""
