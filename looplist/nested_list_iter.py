# Exercise 2.17: Index a nested list

"""
We define the following nested list
q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

Index this list to extract 1) the letter 'a'; 2) the list
['d', 'e', 'f']; 3) the last element h; 4) the 'd' element.
Explain why q[-1][-2] has the value g. 

"""

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
for i in q:  # i is sub list of q
    for j in range(len(i)):  # j is integer
        print i[j],

"""
Sample run:
python nested_list_iter.py
a b c d e f g h
"""
