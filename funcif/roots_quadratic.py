# Exercise 3.3: Write a function for solving a*x**2 + b*x + c = 0
"""
Given a quadratic equation a*x**2 + b*x + c = 0, write a function 'roots(a, b, c)' that returns the 2 roots of
the equation. The returned roots should be 'float' objects when the roots are real, otherwise the roots should
be 'complex' objects. Construct 2 test cases w/known solutions, one w/real roots & other w/complex roots, to
check that function returns correct value and correct type of objects. I threw in a 3rd test case just for fun. 
"""

def roots(a, b, c):
    from cmath import sqrt
    q = sqrt(b * b - 4 * a * c)
    x1 = (-b + q) / (2 * a)
    x2 = (-b - q) / (2 * a)
    return x1, x2

print roots(1, 3, 2)
print roots(1, -2, 3)
print roots (1, -1, 1)

"""
Sample run:
python roots_quadratic.py
((-1+0j), (-2+0j))
((1+1.4142135623730951j), (1-1.4142135623730951j))
((0.5+0.8660254037844386j), (0.5-0.8660254037844386j))
"""
