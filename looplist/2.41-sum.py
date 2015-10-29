"""
Implement the sum function
"""

def sum(list):
    s = 0
    for element in list:
        s += element
    return s
print 'sum = ',sum([1,3,5,-5])


"""
Running program
Unix>python 2.41-sum.py
4

src/looplist> python 2.41-sum.py &
[2] 9208
src/looplist> sum =  4




"""
