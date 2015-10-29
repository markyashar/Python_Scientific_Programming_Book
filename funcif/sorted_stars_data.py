# Exercise 3.32: Write a sort function for a list of 4-tuples

"""
This program gives list of nearest starrs & some of their properties. The list elements are 4-tuples containing
name of star, distance from sun in light years, apparent brightness, and luminosity. Apparent brightness is how 
bright the stars look in our sky compare to brightness of Siruis A. Luminosity, or true brightness, is how 
bright stars would look if all were @ same distance compared to Sun. The list data are found in file "stars.list".
Purpose of this exercise: sort this list wrt distance, apparent brightness, & luminosity.

To sort list data, can call sorted(data), which returns sorted list. However, in present case each element is a
4-tuple, & default sorting of such 4-tuples result in a list w/stars appearing in alphabetic order. Need to sort
wrt 2nd, 3rd, or 4th element of each 4-tuple. If a tailored sort mechanism is necessary, can provide our own sort
function as 2nd argument to 'sorted', as in 'sorted(data, mysort)'. Such a tailored sort function 'mysort' must 
take 2 arguments, say a & b, and returns -1 if a should come before b in the sorted sequence, 1 if b should come
before a, and 0 if they're equal. In present case, a & b are 4-tuples, so need to make the comparison between
the right elements in a & b, e.g., to sort wrt luminosity we write:

def mysort(a, b):
    if a[3] < b[3]:
        return -1
    elif a[3] > b[3]:
        return 1
    else: 
        return 0

Write complete program which initializes the data & writes out 3 sorted tables: star names vs. distance, star name vs.
apparent brightness, & star name vs. luminosity. 

"""

data = [
    ('Alpha Centauri A',    4.3,  0.26,      1.56),
    ('Alpha Centauri B',    4.3,  0.077,     0.45),
    ('Alpha Centauri C',    4.2,  0.00001,   0.00006),
    ("Barnard's Star",      6.0,  0.00004,   0.0005),
    ('Wolf 359',            7.7,  0.000001,  0.00002),
    ('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
    ('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
    ('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
    ('Sirius A',            8.6,  1.00,      23.6),
    ('Sirius B',            8.6,  0.001,     0.003),
    ('Ross 154',            9.4,  0.00002,   0.0005),
]


def print_table(data, mykey):
    print '-------------------------------------------------------------'
    print '%-19s %13s %13s %13s' % ('Star name', 'd_sun',
                                    'Brightness', 'Luminosity')
    print '-------------------------------------------------------------'
    for row in sorted(data, key=mykey):
        print '%-19s %13f %13f %13f' % row
    print '-------------------------------------------------------------\n'

print 'Sorted by star name'
print_table(data, lambda a: a[0])
print 'Sorted by distance to sun'
print_table(data, lambda a: a[1])

print 'Sorted by brightness'
print_table(data, lambda a: a[2])

print 'Sorted by luminosity'
print_table(data, lambda a: a[3])

"""
EXAMPLE OUTPUT:

bash-3.2$ python sorted_stars_data.py 
Sorted by star name
-------------------------------------------------------------
Star name                   d_sun    Brightness    Luminosity
-------------------------------------------------------------
Alpha Centauri A         4.300000      0.260000      1.560000
Alpha Centauri B         4.300000      0.077000      0.450000
Alpha Centauri C         4.200000      0.000010      0.000060
BD +36 degrees 2147      8.200000      0.000300      0.006000
Barnard's Star           6.000000      0.000040      0.000500
Luyten 726-8 A           8.400000      0.000003      0.000060
Luyten 726-8 B           8.400000      0.000002      0.000040
Ross 154                 9.400000      0.000020      0.000500
Sirius A                 8.600000      1.000000     23.600000
Sirius B                 8.600000      0.001000      0.003000
Wolf 359                 7.700000      0.000001      0.000020
-------------------------------------------------------------

Sorted by distance to sun
-------------------------------------------------------------
Star name                   d_sun    Brightness    Luminosity
-------------------------------------------------------------
Alpha Centauri C         4.200000      0.000010      0.000060
Alpha Centauri A         4.300000      0.260000      1.560000
Alpha Centauri B         4.300000      0.077000      0.450000
Barnard's Star           6.000000      0.000040      0.000500
Wolf 359                 7.700000      0.000001      0.000020
BD +36 degrees 2147      8.200000      0.000300      0.006000
Luyten 726-8 A           8.400000      0.000003      0.000060
Luyten 726-8 B           8.400000      0.000002      0.000040
Sirius A                 8.600000      1.000000     23.600000
Sirius B                 8.600000      0.001000      0.003000
Ross 154                 9.400000      0.000020      0.000500
-------------------------------------------------------------

Sorted by brightness
-------------------------------------------------------------
Star name                   d_sun    Brightness    Luminosity
-------------------------------------------------------------
Wolf 359                 7.700000      0.000001      0.000020
Luyten 726-8 B           8.400000      0.000002      0.000040
Luyten 726-8 A           8.400000      0.000003      0.000060
Alpha Centauri C         4.200000      0.000010      0.000060
Ross 154                 9.400000      0.000020      0.000500
Barnard's Star           6.000000      0.000040      0.000500
BD +36 degrees 2147      8.200000      0.000300      0.006000
Sirius B                 8.600000      0.001000      0.003000
Alpha Centauri B         4.300000      0.077000      0.450000
Alpha Centauri A         4.300000      0.260000      1.560000
Sirius A                 8.600000      1.000000     23.600000
-------------------------------------------------------------

Sorted by luminosity
-------------------------------------------------------------
Star name                   d_sun    Brightness    Luminosity
-------------------------------------------------------------
Wolf 359                 7.700000      0.000001      0.000020
Luyten 726-8 B           8.400000      0.000002      0.000040
Alpha Centauri C         4.200000      0.000010      0.000060
Luyten 726-8 A           8.400000      0.000003      0.000060
Barnard's Star           6.000000      0.000040      0.000500
Ross 154                 9.400000      0.000020      0.000500
Sirius B                 8.600000      0.001000      0.003000
BD +36 degrees 2147      8.200000      0.000300      0.006000
Alpha Centauri B         4.300000      0.077000      0.450000
Alpha Centauri A         4.300000      0.260000      1.560000
Sirius A                 8.600000      1.000000     23.600000
-------------------------------------------------------------
"""
