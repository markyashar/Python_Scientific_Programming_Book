"""
We want to access density data in 'densities.dat' file. A dictionary w/name of substance as key &
corresponding density as value seems well-suited for sorting the data.

Solution: Can read 'densities.dat' file line by line, split each line into words, use float conversion
of last word as density value, & remaining one or two words as key in dictionary.
"""

import pprint

def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densities[substance] = density
    infile.close()
    return densities

densities = read_densities('densities.dat')
# from scitools.pprint2 import pprint
pp = pprint.PrettyPrinter(indent=4)
pprint.pprint(densities)
pp.pprint(densities)

"""
OUTPUT:

bash-3.2$ python density.py
{'Earth core': 13.0,
 'Earth mean': 5.52,
 'Moon': 3.3,
 'Sun core': 160.0,
 'Sun mean': 1.4,
 'air': 0.0012,
 'gasoline': 0.67,
 'gold': 18.9,
 'granite': 2.7,
 'human body': 1.03,
 'ice': 0.9,
 'iron': 7.8,
 'limestone': 2.6,
 'mercury': 13.6,
 'platinium': 21.4,
 'proton': 280000000000000.0,
 'pure water': 1.0,
 'seawater': 1.025,
 'silver': 10.5}
{   'Earth core': 13.0,
    'Earth mean': 5.52,
    'Moon': 3.3,
    'Sun core': 160.0,
    'Sun mean': 1.4,
    'air': 0.0012,
    'gasoline': 0.67,
    'gold': 18.9,
    'granite': 2.7,
    'human body': 1.03,
    'ice': 0.9,
    'iron': 7.8,
    'limestone': 2.6,
    'mercury': 13.6,
    'platinium': 21.4,
    'proton': 280000000000000.0,
    'pure water': 1.0,
    'seawater': 1.025,
    'silver': 10.5}

"""
