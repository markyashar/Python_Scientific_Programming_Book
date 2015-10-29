"""
Generate equally spaced coordinates
between 1 and 2. Space should be 0.01

We want to generate x coordinates between 1 & 2 w/spacing 0.01. The coordinates
are given by the formula x_i = 1 + ih, where h = 0.01 and i runs over integers
0, 1,...,100. Compute the x_i values and store them in a list (use a 'for' loop,
and append each new x_i value to a list, which is empty initially).

"""
x = 1
h = 0.01
xcoor = []

for i in range(0, 101):     # 101 to get to 2.00
    xi = i*h
    xcoor.append(x + xi)
print xcoor

"""
Running program
Unix>python 2.9-coor1.py &

src/looplist> [1.0, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.1400000000000001, 1.15, 1.16, 1.17, 1.18, 1.19, 1.2, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.29, 1.3, 1.31, 1.32, 1.33, 1.34, 1.35, 1.3599999999999999, 1.37, 1.38, 1.3900000000000001, 1.4, 1.4100000000000001, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49, 1.5, 1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.5899999999999999, 1.6, 1.6099999999999999, 1.62, 1.63, 1.6400000000000001, 1.65, 1.6600000000000001, 1.67, 1.6800000000000002, 1.69, 1.7000000000000002, 1.71, 1.72, 1.73, 1.74, 1.75, 1.76, 1.77, 1.78, 1.79, 1.8, 1.81, 1.82, 1.83, 1.8399999999999999, 1.85, 1.8599999999999999, 1.87, 1.88, 1.8900000000000001, 1.9, 1.9100000000000001, 1.92, 1.9300000000000002, 1.94, 1.9500000000000002, 1.96, 1.97, 1.98, 1.99, 2.0]

"""
