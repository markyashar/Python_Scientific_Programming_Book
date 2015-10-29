"""
Couting Letters in DNA Strings: Given some string dna containing letters A, C, G, or T, 
representing bases that make up DNA, we ask question: how many times does a certain base
occur in DNA string? Example: If dna is ATGGCATTA & ask how many times base A occur in this
string, answer is 3.

List Iteration: Most straightforward solution is to loop over letters in the string, test if current equals
desired one, and if so, increase a counter. Looping over letters is obvious if letters are stored in a list.
"""

def count_v1(dna, base):
    dna = list(dna)  # convert string to list of letters
    i = 0            # counter
    for c in dna:
        if c == base:
            i += 1
    return i

dna = 'ATGCGGACCTAT'
base = 'C'
n = count_v1(dna, base)

# printf-style formatting
print '%s appears %d times in %s' % (base, n, dna)

# or (new) format string syntax
print '{base} appears {n} times in {dna}'.format(base=base, n=n, dna=dna)

""" 
We have here illustrated two alternative ways of writing out text where the value of variables
are to be inserted in "slots" in the string.

OUTPUT:

bash-3.2$ python  List_Iteration_DNA_String.py
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT
bash-3.2$ 

# Looping over letters is obvious if letters are stored in a list. This is easily
# done by converting a string to a list:
>>> list('ATGC')
['A', 'T', 'G', 'C']
>>> 

# String Interation: Python allows us to iterate directly over a string w/out converting it to a list:
>>> for c in 'ATGC':
...     print c
... 
A
T
G
C
>>> 

# In fact, all built-in objects in Python that contain a set of elements in a particular sequence allow
# a for loop construction of the type 'for element in object.' 

"""
