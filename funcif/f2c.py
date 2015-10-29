# Exercise 3.1 -- Fahrenheit-Celsius conversion function. 
#
# The formula for converting Fahrenheit degrees to Celsius reads
# C = (5/9)*(F-32)
# Write a function C(F) that implements this formula. To verify the implementation of C(F), you can convert 
# Celsius temperature to Fahrenheit & then back to Celsius again using F(C) function & C(F) function, i.e.,
# you can check that boolean expression c == C(F(c)) is 'True' for any temp. c (should, however, be careful
# w/comparing real numbers with == ).

def C(F):
    C_val = (5. / 9) * (F - 32)
    F_val = (9.0 / 5) * C_val + 32
    return C_val if abs(F_val - F) < 1E-12 else 'Error'

print C(30)
print C(-32)
"""
Sample run:
python f2c.py
-1.11111111111
-35.5555555556
"""
