"""
Example: Function w/Default Parameters. Consider function of t which also
contains some parameters, here A, a, and w:

f(t;A,a,w) = A*exp(-a*t)*sin(w*t)

Can implement f as Python function where independent variable t is ordinary
positional argument, & parameters A, a, and w are keyword arguments w/suitable
default values:

"""

from math import pi, exp, sin

def f(t, A=1, a=1, omega=2*pi):
    return A*exp(-a*t)*sin(omega*t)

# Calling f w/just the t argument specified is possible:

v1=f(0.2)

# In this case we evaluate expression exp(-0.2)*sin(2*pi*0.2). Other possible
# calls include:

v2 = f(0.2, omega=1)
v3 = f(1, A=5, omega=pi, a=pi**2)
v4 = f(A=5, a=2, t=0.01, omega=0.1)
v5 = f(0.2, 0.5, 1, 1)

# For v3, observe that positional argument, t in that case, can appear in 
# between keyword arguments if we write positional argument on keyword argument
# form name=value. For v5, we demonstrate that keyword arguments can be used
# as positional argument, i.e., name part can be skipped, but then sequence of
# keyword arguments in call must match sequence in function definition exactly.

print 'v1=%5g , v2=%5g , v3=%5g , v4=%5g , v5=%5g' %(v1, v2, v3, v4, v5)

"""
OUTPUT:

bash-3.2$ python example_function_exp.py
v1=0.778659 , v2=0.162657 , v3=3.16713e-20 , v4=0.00490099 , v5=0.0813283
