"""
Find errors in code
"""
"""
Original code
s = 0; k = 1; M = 100  
while k < M:            
    s +=1/k            
print s

This program does not work correctly. What are the 3 errors? I you try to run
the program, nothing will happen on the screen. Type Ctrl-C to stop the program.
Write a correct program.

There are 2 basic ways to find errors in a program: (i) read the program 
carefully & think about the consequences of each statement, & (ii) print out
intermediate results and compare with hand calculations. First, try method (i)
and find as many errors as you can. Then, try method (ii) for M=3 and compare
the evolution of s with you own hand calculations.

"""
"""
The three errors:
    Doesn't increase the counter. On the initial run you will
    get an infinite loop as k will never increase to the size
    of M. Need to increment k at the end of the while
    An integer error will happen. At the start of the program
    k is an integer, and in the while loop 1/k will not produce
    a float. Need to make either the 1 or the k a float.
    The sum is supposed to include the last number, M. The
    original code will only include up to 100, not including
    100. This can be achieved by making M = 101, or making the
    condition of the while loop while <= 100
Below is the modified code:
"""
s = 0; k = 1.; M = 100
while k <= M:
    s += 1/k
    k += 1
print "sum = ",s

"""
Running program
Unix>python 2.12-compute_sum_while.py
5.18737751764

or

src/looplist> python 2.12-compute_sum_while.py
sum =  5.18737751764

"""
