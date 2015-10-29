import time
e0 = time.time()   # elapsed time since the epoch
c0 = time.clock()  # total CPU time spend in program so far
print "Hello there python followers. This script compares elapsed time with cpu_time!!!"
elapsed_time = time.time() - e0
cpu_time = time.clock() - c0

print "elapsed time = ", elapsed_time
print "cpu_time = ", cpu_time 
print "cpu_time/elapsed_time = ", cpu_time/elapsed_time
"""
ADDITIONAL NOTES:
Epoch: initial time (time.time() would return 0), which is 00:00:00 January 1, 1970.
'time' module also has numerous functions for nice formatting of dates and time, 
& more recent 'datetime' module has more functionality & improved interface.
Although timing has finer resolution than seconds, one should construct test cases
that last some seconds to obtain reliable results.


EXAMPLE OUTPUT:
bash-3.2$ python time_module_test.py
Hello there python followers. This script compares elapsed time with cpu_time!!!
elapsed time =  2.09808349609e-05
cpu_time =  2.1e-05

bash-3.2$ python time_module_test.py
Hello there python followers. This script compares elapsed time with cpu_time!!!
elapsed time =  6.38961791992e-05
cpu_time =  6.4e-05
cpu_time/elapsed_time =  1.00162483582
"""
