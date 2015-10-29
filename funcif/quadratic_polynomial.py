# Here is an example of a function for polynomials of 2nd degree:

# function definition:
def quadratic_polynomial(x, a, b, c):
    value = a*x*x + b*x + c
    derivative = 2*a*x + b
    return value, derivative

# function call:
x = 1
p, dp = quadratic_polynomial(x, 2, 0.5, 1)
print p, dp
p, dp = quadratic_polynomial(x=x, a=-4, b=0.5, c=0)
print p, dp
# The sequence of the arguments is important, unless all arguments are given as 'name=value'

"""
OUTPUT:

bash-3.2$ python quadratic_polynomial.py
3.5 4.5
-3.5 -7.5

"""
