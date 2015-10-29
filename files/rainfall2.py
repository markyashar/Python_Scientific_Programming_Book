# Same as rainfall.py except that we've condensed the for loop over
# lines in the file by using list comprehension

from matplotlib.pylab import *

def extract_data(filename):
    infile = open(filename, 'r')    
    infile.readline() # skip the first line
    numbers = [float(line.split()[1]) for line in infile]
    infile.close()
    return numbers

values = extract_data('rainfall.dat')
month_indices = range(1, 13)
plot(month_indices, values[:-1], 'o')
show()


