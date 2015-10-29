
"""
Compute the mass of various substances

The density of a substance is defined as rho = m/V, where m is the mass of a Volume V.
Compute and print out the mass of one liter of each of the following substances whose
densities in g/cm^3 are found in the file src/files/densities.dat: iron, air, gasoline,
ice, the human body, silver, and platinum: 21.4. Name of program file: 1iter.py.

"""

# q = m/V for density
# m = q * V for mass
# Densities for various substances in g/cm3
iron        = 7.8
air         = 0.0012
gasoline    = 0.67
ice         = 0.9
body        = 1.03
silver      = 10.5
platinum    = 21.4

v = 1000 #  Liter in grams (volume)

print("""From %g liter the mass of 
iron        is %g grams
air         is %g grams
gasoline    is %g grams
ice         is %g grams
human body  is %g grams
silver      is %g grams
platinum    is %g grams """ % (v, v * iron, v * air, v * gasoline, v * ice, v * body, v* silver, v * platinum))

"""
Running program
Unix>python 1liter.py 
From 1000 liter the mass of 
iron        is 7800 grams
air         is 1.2 grams
gasoline    is 670 grams
ice         is 900 grams
human body  is 1030 grams
silver      is 10500 grams
platinum    is 21400 grams
"""
