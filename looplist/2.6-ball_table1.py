"""
Make a table from formula (1.1)
Write a program that prints a nicely formatted table of t  and y(t) values,
where 

y(t) = v_0 * t - (1/2)*g*t^2

Use n uniformly spaced t vaues throughout the interval [0,2*v_0/g]. Set v_0=5
and n = 11. Name of program file: 2.6-ball_table1.py
Note: when y = 0, t = 2*v_0/g
"""

v = 5.0         # Initial velocity of the ball
g = 9.81        # Acceleration of gravity
t = 0.0         # Time

end = 2.0*(v / g)
i = 0
step = end/11

print "t\t\ty(t)"
while t < end:    
    y = (v * t) - (0.5 * g * t**2)
    print "%f\t%f" % (t, y)
    t += step    

"""
Running program
Unix>python 2.6-ball_table1.py
t		y(t)
0.000000	0.000000
0.092670	0.421226
0.185340	0.758208
0.278009	1.010943
0.370679	1.179434
0.463349	1.263679
0.556019	1.263679
0.648689	1.179434
0.741359	1.010943
0.834028	0.758208
0.926698	0.421226
"""
