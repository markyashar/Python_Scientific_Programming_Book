"""
The data associated w/polynomial p(x) = -1 + x**2 + 3*x**7 can be viewed as
set of power-coefficient pairs, in this case coefficient -1 belongs to power
0, coefficient 1 belongs to power 2, & coefficient 3 belongs to power 7. 
Dictionary can be used to map a power to a coefficient:

p = {0: -1, 2:1, 7:3}

A list can, of course, also be used , but in this case must fill in all zero
coefficients too, since index must match the power:

p = [-1, 0, 1, 0, 0 ,0 ,0, 3]

Advantage w/dictionary is that we need to store only non-zero coefficients.
E.g., for polynomial 1 + x**100 dictionary holds 2 elements while list holds
101 elements. 
"""

def poly1(data,x):
    sum = 0.0
    for power in data:
        sum += data[power]*x**power
    return sum
print poly1({0: -1, 2: 1, 7: 3}, 2)
print poly1([-1, 0, 1, 0, 0, 0, 0, 3],2),'\n'

def poly2(data, x):
    return sum([data[p]*x**p for p in data])
print poly2([-1, 0, 1, 0, 0, 0, 0, 3],2)
print poly2({0: -1, 2: 1, 7: 3}, 2), '\n'

def poly3(data, x):
    sum = 0
    for power in range (len(data)):
        sum += data[power]*x**power
    return sum
print poly3([-1, 0, 1, 0, 0, 0, 0, 3],2)

"""
OUTPUT (think abou this -- does it make sense?):
bash-3.2$ python poly_dictionaries.py 
387.0
-3.5 

-3.5
387 

387
bash-3.2$ 
"""
