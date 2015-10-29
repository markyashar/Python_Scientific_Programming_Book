# Tuples are very similar to lists, but tuples cannot be changed. That is, a tuple can be viewed as a
# "constant list". While lists employ square brackets, tuples are written with or withou standard parentheses
# in many cases:

>>> t = 2, 4, 6, 'temp.pdf'
>>> for element in 'myfile.txt', 'yourfile.txt', 'herfile.txt':

...     print element,
... 
myfile.txt yourfile.txt herfile.txt
>>> print t
(2, 4, 6, 'temp.pdf')

# The for loop here is over a tuple, because a comma separated sequence of objects, even w/out enclosing 
# parentheses, becomes a tuple. Note the trailing comma in the print statement. This comma supresses the
# final newline that the 'print' command automatically adds to the output string. This is way to make
# several print statements build up one line of output.

>>> t = t + (-1.0, -2.0)
>>> t
(2, 4, 6, 'temp.pdf', -1.0, -2.0)   # add two tuples
>>> t[1]                            # indexing
4
>>> t[2:]                           # subtuple/slice
(6, 'temp.pdf', -1.0, -2.0)
>>> 6 in t                          # membership
True

# Any list operation that changes the list will not work for tuples:

>>> t[1] = -1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t.append(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> del t[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion

