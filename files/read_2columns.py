# Excercise 6.1: Read a two-column data file.
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
arrays, & plot curve. Print out max. and min. y coordinates. (Hint: Read file line by line, 
split each line into words, convert to float, and append x and y).


"""

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

# infile = open('write_cml_function.txt', 'r')
infile = open('xy.dat', 'r')
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))
    y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)

print 'Minimum x value = %f' % x.min()
print 'Maximum x value = %f' % x.max()
print 'Minimum y value = %f' % y.min()
print 'Maximum y value = %f' % y.max()

plt.plot(x, y, color='#053061', linewidth=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('read_2columns_xy.dat.pdf')
plt.show()
"""
Example Output:

bash-3.2$ python read_2columns.py
Minimum x value = -1.000000
Maximum x value = 1.000000
Minimum y value = -0.948200
Maximum y value = 0.948200

"""

"""
Sample run:
python read_2columns.py
Minimum x value = -1.000000
Maximum x value = 1.000000
Minimum y value = -0.948200
Maximum y value = 0.948200
"""
