print '------------------'     # table heading
C = -20                        # start value for C
dC = 5                         # increment of C in loop
while C <= 40:                 # loop heading with condition
    F = (9.0/5)*C + 32         # 1st statement inside loop
    print F, C                 # 2nd statement inside loop
    C = C + dC                 # 3rd statement inside loop
print '------------------'     # end of table line (after loop)

"""
This program prints out a table w/Fahrenheit degrees 0,10,20,...,40 in the 2nd
column and the corresponding Celsius degrees in the 1st column.

OUTPUT:

src/looplist> python c2f_table_while.py
------------------
-4.0 -20
5.0 -15
14.0 -10
23.0 -5
32.0 0
41.0 5
50.0 10
59.0 15
68.0 20
77.0 25
86.0 30
95.0 35
104.0 40
------------------

"""
