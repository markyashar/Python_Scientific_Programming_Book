"""
Convert from meters to British length units

Make a program where you set a length given in meters and then compute and 
write out the corresponding length measure in inches, in feet, in yards, and in
miles. Use 1 inch = 2.54 cm, 1 foot = 12 inches, one yard = 3 feet, 1 British
mile = 1760 yards. As a verification, 640 meters = (25196.85 inches) = (2099.74 
feet) =  (699.91 yards) = (0.3977 miles). 
Name of program file: length_conversion.py

""" 

inch = 0.0254   # m!
foot = 12*inch
yard = 3*foot
mile = 1760*yard

length = 640  # length in meters
length_inches = length/inch
length_feet = length/foot
length_yards = length/yard
length_miles = length/mile

print """
A length of %.0f m corresponds to
%.2f inches
%.2f feet
%.2f yards
%.4f miles
""" % (length, length_inches, length_feet,
       length_yards, length_miles)

"""
Terminal> python length_conversion.py

A length of 640 m corresponds to
25196.85 inches
2099.74 feet
699.91 yards
0.3977 miles
"""
