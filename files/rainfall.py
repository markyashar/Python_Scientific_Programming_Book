# Here we read the file line by line, and for each line split the line into words,
# pick out the last (second) word on the line, convert this word to 'float', and 
# store the 'float' objects in a list. Having the rainfall values in a list of real
# numbers, we can make a plot of the values vs. month number.

# Note: 1st line in file is just a comment line and of no interest to us. We
# therefore read this line by infile.readline(). The for loop over the lines
# in the file will then start from the next (2nd) line.

# Note: 'numbers' conatin data for 12 months plus the average annual rainfall. 
# Want to plot average rainfall for months only, i.e., values[0:12] or simply
# values[:-1] (everything except last entry). Along "x" axis, put index of a 
# month, starting w/1. Call to range (1,13) generates these indices.

from matplotlib.pylab import *

def extract_data(filename):
    infile = open(filename, 'r')    
    infile.readline() # skip the first line
    numbers = []
    for line in infile:
        words = line.split()
        number = float(words[1])
        numbers.append(number)
    infile.close()
    return numbers

values = extract_data('rainfall.dat')
month_indices = range(1, 13)
plot(month_indices, values[:-1], 'o')
show()


