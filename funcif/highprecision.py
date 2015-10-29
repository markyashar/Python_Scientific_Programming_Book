import decimal                  # floats with arbitrarily many digits
decimal.getcontext().prec = 25  # use 25 digits
D = decimal.Decimal             # short form for new float type

def diff2(f, x, h=1E-9):  # h is a small number. The approximation becomes exact in limit h -> 0. 
    x = D(str(x));  h = D(str(h))  # convert to high precision
    r = (f(x-h) - 2*f(x) + f(x+h))/(h*h)
    return r

# The f argument's like any other argument, i.e., a name for an object, here a function object 
# that we can call as we normally call function objects. An application of diff2 can read:

def g(t):
    return t**(-6)

# Behavior of Numerical Derivative as h -> 0. From mathematics we know that approximate formula
# becomes more accurate as h decreases. Let us try to demonstrate tjos expected feature by making
# table of 2nd-order derivative of g(t)=t**(-6) @ t=1 as h -> 0:

for k in range(1,15):
    h = 10**(-k)
    print 'h=%.0e: %.5f' % (h, diff2(g, 1, h))

"""
EXAMPLE OUTPUT:

bash-3.2$ python highprecision.py
h=1e-01: 44.61504
h=1e-02: 42.02521
h=1e-03: 42.00025
h=1e-04: 42.00000
h=1e-05: 42.00000
h=1e-06: 42.00000
h=1e-07: 42.00000
h=1e-08: 42.00000
h=1e-09: 42.00000
h=1e-10: 42.00000
h=1e-11: 42.00000
h=1e-12: 42.00000
h=1e-13: 20.00000
h=1e-14: 0.00000
-------
NOTE: With g(t)=t**(-6), exact answer is g"(1)=42... With 25 digits in x and h inside the diff2
function, get accurate results for h <= 10**(-13). However, for most practical applications, 
moderately smal h, say 10**(-3) <= h <= 10**(-4), gives sufficient accuracy and then round-off
errors from float calculations do not pose problems.
""" 
