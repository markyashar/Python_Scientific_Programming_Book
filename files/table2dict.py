"""
Example: File Data in Nested Dictionaries
Problem: We're given data file 'table.dat' w/measurements of some properties
w/given names (here A, B, C...). Each property is measured given number of times.
Data are organized as a table where rows contain measurements & columns represent
measured properties.

The word "no" stands for no data, i.e., we lack a measurement. Want to read
this data table into a dictionary data so that we can look up measurement number
i of (say) property C as data['C'][i]. For each property p, want to compute mean of
all measurements & store this as data[p]['mean'].

Algorithm: algorithm for creating data dictionary goes as follows:

examine 1st line: split it into words &
        initialize a dictionary w/property names
        as keys & empty dictionaries ({}) as values
for each of remaining lines in file:
    split line into words
    for each word after 1st:
        if word is not "no":
          transform word to real number and store
                 number in relevant dictionary

In summary: Want to load tabular data in file 'table.dat' into nested
dictionary data and compute mean values

"""
import pprint
infile = open('table.dat', 'r')
lines = infile.readlines()  # We load all lines of file into a list of strings called 'lines'.
infile.close()
data = {}   #  data[property][measurement_no] = propertyvalue
first_line = lines[0]   # The 'first_line' variable refers to the string '   A   B   C   D'    
properties = first_line.split()  # We split this line into a list of words, called 'properties',
                                 # which then contains ['A', 'B', 'C', 'D']
for p in properties:    # With each of these property names we associate a dictionary w/measurement                      
    data[p] = {}        # number as key & property value as value, but 1st must create these "inner"
                        # dictionaries as emtpy before can add the measurements.
for line in lines[1:]:  # First pass in for loop picks out string '1   11.7   0.035   2017   99.1'
    words = line.split() # as the 'line variable. We split this line into words, 1st word (words[0]) is
    i = int(words[0])    # measurement number, while rest words[1:] is a list of
    values = words[1:]   # values of properties, here named 'values'. To pair up the right properties
                         # & values, loop over properties and values lists simultaneously:
    for p, v in zip(properties, values):
        if v != 'no':     # Recall that some values may be missing and we drop to record that value.
            data[p][i] = float(v) # Because 'values' list contains strings (words) read from thefile,
                                  # need to explicitly transform each string to a 'float' number 
                                  # before can compute w/values.

# It remains to compute average values. For each property name p, i.e., key in the data dictionary, can
# extract recorded values as the list data[p].values() and simply send this list to Python's sum function
# and divide by numbered measured values of this property, i.e., length of list: 
# Compute mean values
for p in data:
    values = data[p].values()
    data[p]['mean'] = sum(values)/len(values)

# Alternatively, can write an explicit loop to computer the average:
# for p in data:
#     sum_values = 0
#     for value in data[p]:
#         sum_values += value
#     data[p]['mean'] = sum_values/len(data[p]) 

for p in sorted(data):
    print 'Mean value of property %s = %g' % (p, data[p]['mean'])

# import scitools.pprint2
# scitools.pprint2.pprint(data)

pprint.pprint(data)

# Additional Note: When want to look up measurement number n of property B, must recall that this particular
# measurement may be missing so must do test if n is key in dictionary data[p]:

# if n in data['B']
#    value = data['B'][n]

# alternative:
# value = data['B'][n] if n in data['B'] else None

"""
OUTPUT: Corresponding output from this program becomes:

bash-3.2$ python table2dict.py
Mean value of property A = 10.1667
Mean value of property B = 0.0344
Mean value of property C = 2015
Mean value of property D = 102.133

# And this is a view of the nested data dictionary

{'A': {1: 11.7,
       2: 9.2,
       3: 12.2,
       4: 10.1,
       5: 9.1,
       6: 8.7,
       'mean': 10.166666666666666},
 'B': {1: 0.035, 2: 0.037, 4: 0.031, 5: 0.033, 6: 0.036, 'mean': 0.0344},
 'C': {1: 2017.0, 2: 2019.0, 5: 2009.0, 6: 2015.0, 'mean': 2015.0},
 'D': {1: 99.1,
       2: 101.2,
       3: 105.2,
       4: 102.1,
       5: 103.3,
       6: 101.9,
       'mean': 102.13333333333334}}

"""
