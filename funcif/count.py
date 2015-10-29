def count_v1(dna, base):
    dna = list(dna)  # convert string to list of letters
    i = 0            # counter
    for c in dna:
        if c == base:
            i += 1
    return i

def count_v2(dna, base):
    i = 0 # counter
    for c in dna:
        if c == base:
            i += 1
    return i

dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v2(dna, base)

# printf-style formatting
print '%s appears %d times in %s' % (base, n, dna)

# or (new) format string syntax
print '{base} appears {n} times in {dna}'.format(
    base=base, n=n, dna=dna)

def count_v2_demo(dna, base):
    print 'dna:', dna
    print 'base:', base
    i = 0 # counter
    for c in dna:
        print 'c:', c
        if c == base:
            print 'True if test'
            i += 1
    return i

dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v2_demo('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                        
print '%s appears %d times in %s' % (base, n, dna)
# or (new) format string syntax     
print '{base} appears {n} times in {dna}'.format(base=base, n=n, dna=dna)

# Index Iteration: Although it's natural in Python to iterate over letters in
# a string (or more generally over elements on a seqeuence), programmers w/
# eexperience in other languages (e.g., Fortran, C, Java) are used to for 
# loops w/integer counter running over all indices in string or array: 

def count_v3(dna, base):
    i = 0 # counter
    for j in range(len(dna)): # Python indices always start @ 0 so legal indices for our string
        if dna[j] == base:    # become 0,1,...,len(dna)-1, where len(dna) is number of letters in
            i += 1            # string dna. range(x) function returns list of integers 0, 1,...,
    return i                  # x-1, implying that range(len(data)) generates all legal indices for dna.
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v3('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                         
print '%s appears %d times in %s' % (base, n, dna)

# While Loops: The while loop equivalent to last function reads:

def count_v4(dna, base):
    i = 0 # counter
    j = 0 # string index
    while j < len(dna):
        if dna[j] == base:
            i += 1
        j += 1            # Correct indentation here's crucial: typical error is to fail indenting j += 1
    return i              # line correctly.
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v4('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                         
print '%s appears %d times in %s' % (base, n, dna)

# Summing a Boolean List: Next idea is to create list m where m[i] is True if dna[i] equals letter we search
# for (base). Number of True values in m is then number of base letters in dna. Can use sum function to find
# this number because doing arithmetic w/boolean lists automatically interprets True as 1 & False as 0, i.e.,
# sum(m) returns number of True elements in m. Possible functino doing this is:

def count_v5(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        if c == base:
            m.append(True)
        else:
            m.append(False)
    return sum(m)
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v5('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                     
print '%s appears %d times in %s' % (base, n, dna)
# or (new) format string syntax                                                                                                     
print '{base} appears {n} times in {dna}'.format(base=base, n=n, dna=dna)

# Inline If Test: Shorter, more compact code is often goal if compactness
# enhances readability. 4-line if test in previous function can be condensed
# to 1 line using inline if construction: 'if condition value1 else value2'

def count_v6(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        m.append(True if c == base else False)
    return sum(m)
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v6('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                         
print '%s appears %d times in %s' % (base, n, dna)                                                                                
# or (new) format string syntax
print '{base} appears {n} times in {dna}'.format(base=base, n=n, dna=dna)

# Using Boolean Values Directly: Inline if test is in fact reduntant in previous
# function because value of condition c == base can be used directly: it has value
# True or False. This saves some typing and adds clarity, @ least to Python programmers
# w/experience:

def count_v7(dna, base):
    m = []   # matches for base in dna: m[i]=True if dna[i]==base
    for c in dna:
        m.append(c == base)
    return sum(m)
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v7('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                         
print '%s appears %d times in %s' % (base, n, dna)


# List Comprehensions: Building a list w/aid of for loop can often be condensed to single
# line by using list comprehensions: [expr for e insequence], where expr is some expression
# normally involving iteration variable e. In next/last example, can introduce list
# comprehension:

def count_v8(dna, base):
    m = [c == base for c in dna]
    return sum(m)
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v8('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                         
print '%s appears %d times in %s' % (base, n, dna)

# Here it's tempting to get rid of m variable & reduce function body to single line:
def count_v9(dna, base):
    return sum([c == base for c in dna])
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v9('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                         
print '%s appears %d times in %s' % (base, n, dna)

# Using a Sum Iterator: DNA string is usually huge -- 3 billion letters of human species. Making a boolean array
# w/True & False values therefore increases memory usage by a factor of 2 in sample functions count_v5 to 
# count_v9. Summing w/out actually storing an extra list is desirable. Fortunately, sum([x for x in s]) can be
# replaced by sum(x for x in s), where latter sums elements in s as x visits elements of s one by one. Removing 
# brackets therefore avoids first making a list before applying sum on that list. This is minor modification of
# count_v9 function:
def count_v10(dna, base):
    return sum(c == base for c in dna)

# Below we measure impact of various program constructs on CPU time.
# Extracting Indices: Instead of making boolean list w/elements expressing
# whether letter matches given base or not, may collect all indices of matches.
# This can be done by adding if test to list comprehension:
def count_v11(dna, base):
    return len([i for i in range(len(dna)) if dna[i] == base])

# Using Python's Library: Very often when set out to do task in Python, there's already
# functionality for task in object itself, in Python libraries, or in 3rd-party libraries
# found on Internet. Counting how many times letter (or substring) base appears in string
# data is obviously very common task -- so, Python supports it by syntax 'dna.count(base)':
def count_v12(dna, base):
    return dna.count(base)
dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v12('ATGCGGACCTAT', 'C')
# printf-style formatting                                                                                                                         
print '%s appears %d times in %s' % (base, n, dna)

# Generating Random DNA Strings: Simplest way of generating long string is to repeat a character
# large number of times:
#
N = 100
# dna = 'A'*N
# 
# Resulting string is just 'AAA...A', of length N, which is fine for testing efficiency of Python
# functions. Nevertheless, more exciting to work w/DNA string w/letters from whole alphabet A, C,
# G, & T. To make DNA string w/random composition of letters we can 1st make list of random letters
# & then join all those letters to a string:
import random
alphabet = list('ATGC')
dna = [random.choice(alphabet) for i in range(N)]     # random.choice(x) function selects an element
dna = ''.join(dna)  # join list elements to a string  # in list x at random. 
 
# Note: N is very often large number. In Python v 2.x, range(N) generates list of N integers. Can 
# avoid list by using xrange, which generates an integer at a time & not whole list. In Python v3.x,
# range function is actually xrange function in v2.x . Using xrange, combining statements, &
# wrapping construction of random DNA string in function, gives
import random
def generate_string(N, alphabet='ACGT'):
    return ''.join([random.choice(alphabet) for i in xrange(N)])

dna = generate_string(600000)
#dna = generate_string(6000000)
# Example: The call generate_string(10) may generate something like AATGGCAGAA.

# Measuring CPU Time: Next goal is to see how much time various count_v* functions 
# spend on counting letters in a huge string, which is to be generated as shown above.
# Measuring time spent in program can be done by time module:
# import time
#...
# t0 = time.clock()    # time.clock() function returns CPU time spent in program since
# do stuff             # its start
# t1 = time.clock()
# cpu_time = t1-t0
# If interest is in total time, also including reading & writing files, time.time()
# is appropriate function to call.

# Running through all our functions made so far& recording timings can be done by:
import time
functions = [count_v1, count_v2, count_v3, count_v4,
             count_v5, count_v6, count_v7, count_v8,
             count_v9, count_v10, count_v11, count_v12]
timings = []  # timings[i] holds CPU time for functions[i]

for function in functions:
    t0 = time.clock()
    function(dna, 'A')
    t1 = time.clock()
    cpu_time = t1 - t0
    timings.append(cpu_time)
# In Python, functions are ordinary objects so making list of funcions is no more special 
# than making list of strings or numbers.

# Can now iterate over timings & functions simultaneouly via zip to make nice printout
# of results: 
for cpu_time, function in zip(timings, functions):
    print '{f:<9s}: {cpu:.2f} s'.format(
        f=function.func_name, cpu=cpu_time)

# Timings on MacBook Air 11 running Ubuntu show that functions using list.append require
# almost double of time of functions that work w/list comprehensions. Even faster is 
# simple iteration over string. However, built-in count functionality of strings
# (dna.count(base)) runs over 30 times faster than best of our handwritten Python 
# functions! Reason is that for loop needed to count dna.count(base) is actually implemented
# in C & runs very much faster than loops in Python.
# Clear lesson: google around before you start out to implement what seems to be quite common
# task. Others have probably done it for you, &, most likely, their solution is much better
# than what you can(easily) come up with.

# Time count_v12 better: repeat 100 times because it's so fast
t0 = time.clock()
for i in range(100):
    count_v12(dna, 'A')
t1 = time.clock()
print '{f:<9s}: {cpu:.2e} s'.format(
    f='count_v12', cpu=(t1-t0)/100.)

dna = 'ATTTGCGGTCCAAA'
exact = count_v12(dna, 'A')
for f in functions:
    assert f(dna, 'A') == exact

"""
OUTPUT:

bash-3.2$ python count.py
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
dna: ATGCGGACCTAT
base: C
c: A
c: T
c: G
c: C
True if test
c: G
c: G
c: A
c: C
True if test
c: C
True if test
c: T
c: A
c: T
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
count_v1 : 0.05 s
count_v2 : 0.04 s
count_v3 : 0.08 s
count_v4 : 0.15 s
count_v5 : 0.13 s
count_v6 : 0.13 s
count_v7 : 0.12 s
count_v8 : 0.07 s
count_v9 : 0.06 s
count_v10: 0.06 s
count_v11: 0.08 s
count_v12: 0.00 s
count_v12: 1.75e-03 s

--------------

ADDITIONAL NOTE: Can examine list comprehension in interactive Python shell:

>>> dna = 'AATGCTTA'
>>> base ='A'
>>> indices = [i for i in range (len(dna)) if dna[i] == base]
>>> indices
[0, 1, 7]
>>> print dna[0], dna[1], dna[7]  # check
A A A
>>> 

# Element i in list comprehension is only made for those i where dna[i] == base.
"""
