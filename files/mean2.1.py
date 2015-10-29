# Inside the loop we test if 'line' is False, and it is False when we reach
# end of file, because 'line' then becomes empty string, which if Python
# evaluates to False. When line is False, 'break' statement breaks the loop
# and makes the program flow jump to 1st statement after the 'while' block.

infile = open('data1.txt', 'r')
mean = 0
n = 0
while True:
    line = infile.readline()
    if not line:
       break
    mean += float(line)
    n += 1
mean = mean/float(n)
print mean

"""
OUTPUT:

bash-3.2$ python mean2.1.py
20.95
"""

"""
The call infile.read() reads the whole file and returns text as a string object.
Following interactive session illustrates use and result of infile.read()

bash-3.2$ python 
Python 2.7.1 (r271:86832, Jul 31 2011, 19:30:53) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> infile = open('data1.txt', 'r')
>>> filestr = infile.read()
>>> filestr
'21.8\n18.1\n19\n23\n26\n17.8\n'
>>> print filestr
21.8
18.1
19
23
26
17.8

-----------------

Note difference between just writing 'filestr' & writing 'print filestr'. Former
dumps string w/newlines as "backslash n" characters, whiile latter is "pretty print"
where string is written out w/out quotes and w/newline characters as visible line
shifts.

String ofjects have many useful functions for extracting info. Very useful feature
is split: filestr.split() will split string into words (separated by blanks or any
other sequence of characters you've defined). "Words" in this file are the
numbers:

>>> words = filestr.split()
>>> words
['21.8', '18.1', '19', '23', '26', '17.8']
>>> numbers = [float(w) for w in words]
>>> mean = sum(numbers)/len(numbers)
>>> print mean
20.95
>>>  
