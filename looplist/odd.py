"""
Generate odd numbers
This program generates odd numbers from 1 to n.
It sets n in the beginning of the program and uses
a while loop to compute the numbers (making sure that
if n is an even number, the largest generated odd number
is n-1).
"""

n = 9                   # The upper limit
odd = 1                 # Start at 1

while odd < n:
    print odd
    odd = odd + 2       # To get odd number

"""
Running program
Unix>python odd.py
1
3
5
7
"""
