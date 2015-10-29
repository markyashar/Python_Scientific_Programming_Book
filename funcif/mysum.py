# Exercise 3.4: Implement the sum function.
# The standard Python function called 'sum' takes a list as argument and computes the
# sum of the elements in the list, e.g., 
# >>> sum([1,3,5,-5])
# 4
# Implement your own version of sum.

def mysum(L):
    s = 0
    for e in L:
        s += e
    return s

print mysum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

"""
SAMPLE OUTPUT:
 
bash-3.2$ python mysum.py 
55
55
"""
