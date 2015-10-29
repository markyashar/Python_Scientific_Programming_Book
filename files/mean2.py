# Here, we load the lines into a list of 'float' objects directly. 
# The call infile.readline() returns a string containing the text at
# the current line. A new infile.readline() will read the next line.

infile = open('data1.txt', 'r')
numbers = [float(line) for line in infile.readlines()]
infile.close()
mean = sum(numbers)/len(numbers)
print mean

"""
OUTPUT:

bash-3.2$ python mean2.py
20.95

"""
