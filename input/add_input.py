"""
This program reads in 2 values and adds them. The values could be strings, floats, integers, lists, & so forth, as long 
as we can apply and '+' operator to the values. Since we don't know if user supplies a string, float, integer, or
something else, we just convert the input by 'eval', which means that user's syntax will determine the type.
"""
i1 = eval(raw_input('Give input: '))
i2 = eval(raw_input('Give input: '))
r = i1 + i2
print '%s + %s becomes %s\nwith value %s' % \
      (type(i1), type(i2), type(r), r)

"""
Observe that we write out the 2 supplied values, together w/types of the values (obtained by 'eval'), & the sum.
Let's run the program w/an integer & real number as input:

bash-3.2$ python add_input.py
Give input: 4
Give input: 3.1
<type 'int'> + <type 'float'> becomes <type 'float'>
with value 7.1

Ths string '4', returned by the 1st call to 'raw_input', is interpreted as an int by eval,
while '3.1' gives rise to a float object.

Supplying 2 lists also works fine:

bash-3.2$ python add_input.py
Give input: [-1, 3.2]
Give input: [9,-2,0,0]
<type 'list'> + <type 'list'> becomes <type 'list'>
with value [-1, 3.2, 9, -2, 0, 0]

If we want to use the program to add 2 strings, the strings must
be enclosed in quotes for eval to recognize the texts as tring
objects (w/out the quotes, eval aborts w/an error):

bash-3.2$ python add_input.py
Give input: 'one string'
Give input: " and another string"
<type 'str'> + <type 'str'> becomes <type 'str'>
with value one string and another string

Not all objects are meaningful to add:

bash-3.2$ python add_input.py
Give input: 3.2
Give input: [-1,10]
Traceback (most recent call last):
  File "add_input.py", line 8, in <module>
    r = i1 + i2
TypeError: unsupported operand type(s) for +: 'float' and 'list'

"""
