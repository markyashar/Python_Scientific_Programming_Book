#M = 47       # small egg
M = 67      # large egg
rho = 1.038  # density
c = 3.7      # specific heat capacity
K = 5.4E-3   # thermal heat conduction
T_w = 100    # water temperature, Celsius
T_o = 4      # initial egg temperature
# T_o = 20
T_y = 70

from math import pi, log

t = ((M**(2/3.0)*c*rho**(1/3.0))/\
    (K*pi**2*(4*pi/3)**(2/3.0)))*\
    log(0.76*(float(T_o - T_w)/(T_y - T_w)))

print 'Recommended cooking time: %.2f min' % (t/60.)

"""
Terminal> python egg.py  # from fridge
Recommended cooking time: 6.61 min
Terminal> python egg.py  # room temperature
Recommended cooking time: 5.25 min

src/formulas> python egg.py &
[4] 17284
src/formulas> Recommended cooking time: 5.25 min


src/formulas> python egg.py &
[4] 18422
src/formulas> Recommended cooking time: 6.61 min


"""
