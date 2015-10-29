"""
Derive and compute a formula

Can a newborn baby in Norway expect to live for one billion (10^9) seconds?
Name of program file: seconds2years.py

"""

time_in_seconds = 1.0E+9

# Quick solution
time_in_years = time_in_seconds/60/60/24/365.25
#print time_in_years

# More explanation
time_in_minutes = time_in_seconds/60
time_in_hours = time_in_minutes/60
time_in_days = time_in_hours/24
time_in_years = time_in_days/365.25
#print time_in_years

# Control no of decimals (0) in output
print 'Time in years: %.0f' % time_in_years

# Answer the yes/no question:
# Yes if time_in_years <= 80
if time_in_years <= 80:       # if test: chapter 3!
    print 'Yes!'
else:
    print 'No!'

"""
Terminal> python seconds2years.py
Time in years: 32
Yes!
"""
