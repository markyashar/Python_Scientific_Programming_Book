Cdegrees = []
n = 21
C_min = -10
C_max = 40
dC = (C_max - C_min)/float(n-1)  # increment in C

Cdegrees = [0]*n
for i in range(len(Cdegrees)):
     Cdegrees[i] = -10 + i*dC

Fdegrees = [0]*n
for i in range(len(Cdegrees)):
    Fdegrees[i] = (9.0/5)*Cdegrees[i] + 32

for i in range(len(Cdegrees)):
    print '%5.1f %5.1f' % (Cdegrees[i], Fdegrees[i])

for C, F in zip(Cdegrees, Fdegrees):
    print '%5d %5.1f' % (C, F)

for c in Cdegrees:
    c += 5
print Cdegrees

for i in range(len(Cdegrees)):
    Cdegrees[i] += 5
print Cdegrees

Cdegrees = range(-20, 41, 5)   # -20, -15, ..., 35, 40
Fdegrees = [(9.0/5)*C + 32 for C in Cdegrees]

table = [Cdegrees, Fdegrees]
import pprint
pprint.pprint(table)

table = []
for C, F in zip(Cdegrees, Fdegrees):
    table.append([C, F])
pprint.pprint(table)

table = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
pprint.pprint(table)
