# Exercise 3.23: Find max & min elements in a list.
"""
Given a list a, the max function in Python's standard library computes the largest element in a: max(a).
Similarly, min(a) returns the smallest element in a. Purpose of this exercise is to write your own max
and min function. Use following technique: Initialize a variable max_elem by 1st element in list, then
visit all remaining elemnts (a[1:]), compare each element to max_elem, & if greater, make max_elem
refer to that element. Use similar technique to compute min. element. Collect the 2 pieces of code
in functions.
"""

def mymax(a):
    max_elem = a[0]
    for elem in a:
        if elem > max_elem:
            max_elem = elem
    return max_elem


def mymin(a):
    min_elem = a[0]
    for elem in a:
        if elem < min_elem:
            min_elem = elem
    return min_elem

print mymax([1, 5, 6, -2, 4, -7, -4, 2, 6, 5, 11, 3, 5])
print mymin([1, 5, 6, -2, 4, -7, -4, 2, 6, 5, 11, 3, 5])

"""
EXAMPLE OUTPUT:
bash-3.2$ python maxmin_list.py
11
-7

"""
