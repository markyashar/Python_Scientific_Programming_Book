def C2F(C):
    """Convert Celsius degrees (C) to Fahrenheit."""
    return (9.0/5)*C + 32
print C2F.__doc__

def line(x0, y0, x1, y1):
    """
    Compute the coefficients a and b in the mathematical
    expression for a straight line y = a*x + b that goes
    through two points (x0, y0) and (x1, y1).

    x0, y0: a point on the line (floats).
    x1, y1: another point on the line (floats).
    return: coefficients a, b (floats) for the line (y=a*x+b).
    
    Example:
    >>>> a, b = line(1, -1, 4, 3)
    >>>> a
    1.3333333333333333
    >>>> b
    -2.333333333333333
    """
    
    a = (y1 - y0)/float(x1 - x0)
    b = y0 - a*x0
    return a, b

print line.__doc__
print "Fahrenheit degrees = ",C2F(10)
print "(a,b) = ",line(5.4,6.3,7.5,8.2)

"""
EXAMPLE OUTPUT:

bash-3.2$ python c2f_line_doc_strings.py
Convert Celsius degrees (C) to Fahrenheit.

    Compute the coefficients a and b in the mathematical
    expression for a straight line y = a*x + b that goes
    through two points (x0, y0) and (x1, y1).

    x0, y0: a point on the line (floats).
    x1, y1: another point on the line (floats).
    return: coefficients a, b (floats) for the line (y=a*x+b).
    
Fahrenheit degrees =  50.0
(a,b) =  (0.9047619047619047, 1.4142857142857146)


python c2f_line_doc_strings.py
Convert Celsius degrees (C) to Fahrenheit.

    Compute the coefficients a and b in the mathematical
    expression for a straight line y = a*x + b that goes
    through two points (x0, y0) and (x1, y1).

    x0, y0: a point on the line (floats).
    x1, y1: another point on the line (floats).
    return: coefficients a, b (floats) for the line (y=a*x+b).
    
    Example:
    >>>> a, b = line(1, -1, 4, 3)
    >>>> a
    1.3333333333333333
    >>>> b
    -2.333333333333333
    
Fahrenheit degrees =  50.0
(a,b) =  (0.9047619047619047, 1.4142857142857146)
"""
