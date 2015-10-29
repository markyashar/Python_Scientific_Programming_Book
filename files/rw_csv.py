# Python code for loading spreadsheet data into a table. Table is technically a nested list, where each list element is 
# a row of the table, & each row is list of table's column values. The program reads the budget.csv file, processing its
# data, and writing the budget2_practice.csv file

infile = open('budget.csv', 'r')  # CSV files can be read, row by row, using the csv module from Python's standard library.
import csv
table = []
for row in csv.reader(infile):  # The row variable is a list of column values that are read from the file
    table.append(row)           # by the csv module. These 3 lines compute the table.
infile.close()

import pprint
pprint.pprint(table)  # The table is printed here and is represented as a nested list.

# Note: The csv module reads all cells into string objects. To compute w/the numbers,
# need to transform the string objects into float objects. 

# Transform numbers in table into float objects
# (let first row and first column remain strings). Transformation should not be applied
# to 1st row & 1st column, since the cells here hold text.
for r in range(1,len(table)):     # The transformation from strings to numbers therefore
    for c in range(1, len(table[0])):   # applies to indices r and c in table (table[r][c]),
        table[r][c] = float(table[r][c])  # such that the row counter r goes from 1 to
# len(table)-1, & column counter c goes from 1 to len(table[0])-1 (len(table[0]) is the
# length of first row, asuming the lengths of all rows are equal to length of 1st row).
pprint.pprint(table)    
# The numbers now have a decimal and no quotes, indicating that numbers are float objects
# and hence ready fro mathematical calculations 

# Processing Data: We perform a very simple calculation w/table, namely adding a final row
# w/sum of numbers in the columns:
# Add a new row with sums
row = [0.0]*len(table[0])   # We first create a list row consisting of zeros. 
row[0] = 'sum'              # Then we insert a text in the first column, before
for c in range(1, len(row)):   # we invoke a loop over the numbers in the table and
    s = 0                      # compute the sum of each column. The table list now
    for r in range(1, len(table)):  # represents a spreadsheet w/4 columns & 5 rows.
        s += table[r][c]
    row[c] = s
table.append(row)
pprint.pprint(table)

# Writing CSV Files: Final task is to write modified table list back to a CSV file so that
# data can be loaded into a spreadsheet program.
outfile = open('budget2_practice.csv', 'w')
writer = csv.writer(outfile)
for row in table:
    writer.writerow(row)
outfile.close()

"""
OUTPUT:

bash-3.2$ python rw_csv.py
[['', 'year 1', 'year 2', 'year 3'],
 ['person 1', '651000', '651000', '651000'],
 ['person 2', '1100500', '950100', '340000'],
 ['person 3', '740000', '780000', '800000']]
[['', 'year 1', 'year 2', 'year 3'],
 ['person 1', 651000.0, 651000.0, 651000.0],
 ['person 2', 1100500.0, 950100.0, 340000.0],
 ['person 3', 740000.0, 780000.0, 800000.0]]
[['', 'year 1', 'year 2', 'year 3'],
 ['person 1', 651000.0, 651000.0, 651000.0],
 ['person 2', 1100500.0, 950100.0, 340000.0],
 ['person 3', 740000.0, 780000.0, 800000.0],
 ['sum', 2491500.0, 2381100.0, 1791000.0]]

and

bash-3.2$ more budget2_practice.csv
,year 1,year 2,year 3
person 1,651000.0,651000.0,651000.0
person 2,1100500.0,950100.0,340000.0
person 3,740000.0,780000.0,800000.0
sum,2491500.0,2381100.0,1791000.0

and

bash-3.2$ more  budget.csv
,"year 1","year 2","year 3"
"person 1",651000,651000,651000
"person 2",1100500,950100,340000
"person 3",740000,780000,800000

"""
