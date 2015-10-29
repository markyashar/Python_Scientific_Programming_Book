# To read a file, first need to open file. This action creates a file object,
# here stored in variable 'infile':

infile = open('data1.txt', 'r')

# 2nd argument to 'open' function, string 'r', tells that we want to open
# file for reading. After file is read, should close file object with
# 'infile.close()

# Basic recipe for reading file line by line applies a for loop as follows:
lines = []
for line in infile:
    print line
    lines.append(line)
infile.close()
print lines

# We've loaded the file into the list 'lines'.

# Next task is to compute average of numbers in file and making
# sure to convert each line to a float in the process.

mean = 0
for line in lines:
    number = float(line)
    mean = mean + number
mean = mean/len(lines)
print mean

"""
OUTPUT:

bash-3.2$ python mean1.py
21.8

18.1

19

23

26

17.8

['21.8\n', '18.1\n', '19\n', '23\n', '26\n', '17.8\n']
20.95

"""
