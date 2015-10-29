"""
What type of objects are i and j?
"""
q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

for i in q:
    for j in range(len(i)):
        print i[j]
print "q[-1][-2] = ", q[-1][-2]

"""
Answer: i is a list object
        j is a list element
"""

"""
Running program
Unix>python 2.16-nested_list_iter.py
a
b
c
d
e
f
g
h
q[-1][-2] =  g
"""
