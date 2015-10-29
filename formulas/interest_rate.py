"""
Compute the growth of money in a bank.

Let p be a bank's interest rate in percent per year. An initial amount
A has then grown to

A*(1+p/100)^n

after n years. Make a program for computing how much money 1000
euros have grown to after three years with 5% interest rate.

"""

p = 5       # Interest rate %
A = 1000    # Initial amount
years = 3   # Number of years to grow

# Formula for calculating sum: A(1 + p/100)^n
# To avoid integer division we convert p to float
sum = A * (1 + (float(p)/100))**years

print("After %g years with %g%% interest rate and an initial amount of %g we have %g." % (years, p, A, sum))

"""
Unix>python interest_rate.py 
After 3 years with 5% interest rate and an initial amount of 1000 we have 1157.63.
"""
