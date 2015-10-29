# Exercise 3.34: Find pairs of characters. Write function count_pairs(dna, pair) that returns number
# of occurrences of a pair of characters (pair) in a DNA string (dna), e.g., calling the function 
# w/dna as 'ACTGCTATCCATT' and pair as 'AT' will return 2.
def count_pairs(dna, pair):
    pair = tuple(pair)   # Tuples are very similar to lists, except tuples can't be changed, i.e.,
                         # a tuple can be viewed as a "constant list". tuple([iterable]) returns a tuple
                         # whose items are same and in same order as iterable's items. iterable may be
                         # a sequence, a container that supports iteration, or iterator object. If iterable
                         # is already a tuple, it's returned unchanged, e.g., tuple('abc') returns ('a', 'b', 'c')
                         # and tuple([1,2,3]) returns (1,2,3). 
    i = 0
    for p1, p2 in zip(dna[:-1], dna[1:]):  # zip function turns n lists (list1, list2, list3,...) into 1 list 
                                           # of n-tuples where each n-tuple (e1, e2, e3,...) has its 1st element
                                           # (e1) from first list (list1), 2nd element (e2) from 2nd list (list2),
                                           # and so forth. Loop stops when end of shortest list is reached
        if (p1, p2) == pair:
            i += 1
    return i

dna = 'ATATGCGGACCTAT'
pair = 'AT'
print count_pairs(dna, pair)


"""

OUTPUT:

bash-3.2$ python count_pairs.py
3

-------------

ADDITIONAL NOTES:
Recall that [:-1] is list indexing, and it returns all elements [:] except the last one, -1

Example:  
>>> a = [1,2,3,4,5,6]
>>> a[:-1]
[1, 2, 3, 4, 5] 

Also, 

>>> a = [1,2,3,4,5]
>>> a[1:]
[2, 3, 4, 5]
>>> 
"""
