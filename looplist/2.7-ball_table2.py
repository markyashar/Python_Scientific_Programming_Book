"""
Store values from a formula in lists:
Modify the program from Exercise 2.6 so that the t and y values are stored in
2 lists t and y. Thereafter, traverse the lists with a 'for' loop and write out
a nicely formatted table of t and y values (using a 'zip' or 'range' 
construction). Set v0 = 10 and i=6.

""" 


t = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

def y(t):
    # formula 1.1 - find the vertical position of a ball at a specific (t) time
    v0 = 5 # initial velocity
    g = 9.81 # gravity 
    
    return (v0*t)- (0.5*g*(t**2))

# calculate the y for the different t values
y = [y(T) for T in t]

i = 0
print '---------------------'
print '|__t______|y(t)_____|'

# loop through our two lists and print the values
while i < len(y):
    print '|  %g   |%4.4f    |' % (t[i], y[i])
    i = i+1
print '---------------------'

"""
Running program for v0 = 5:
Unix>python 2.7-ball_table2.py
---------------------
|__t______|y(t)_____|
|  0.1   |0.4509    |
|  0.2   |0.8038    |
|  0.3   |1.0585    |
|  0.4   |1.2152    |
|  0.5   |1.2737    |
|  0.6   |1.2342    |
---------------------

Running program for v0 = 10:
Unix>python 2.7-ball_table2.py
src/looplist> ---------------------
|__t______|y(t)_____|
|  0.1   |0.4509    |
|  0.2   |0.8038    |
|  0.3   |1.0585    |
|  0.4   |1.2152    |
|  0.5   |1.2737    |
|  0.6   |1.2342    |
---------------------

"""
