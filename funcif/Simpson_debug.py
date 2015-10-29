def Simpson(f, a, b, n=500):
    """
    Return the approximation of the integral of f
    from a to b using Simpson's rule with n intervals.
    """
    if a > b:                                 # Here we test if b > a
        print 'Error: a=%g > b=%g' % (a, b)
        return None

    # Check that n is even                               # Here we test if n is an even integer by making use of mod function:
    if n % 2 != 0:                                       # mod(n,d) gives the remainder when n is divided by d (both n and d 
        print 'Error: n=%d is not an even integer!' % n  # are integers). In Python, percentage sign is used for the mod function.
        n = n+1  # make n even                           # To test if n is an odd integer, can see if it can be divided by 2 & yield
                                                         # an integer w/out any reminder (n % 2 ==0). 
    h = (b - a)/float(n)  
    sum1 = 0
    for i in range(1, n/2 + 1):     # We code the summation w/aid of 'for loop' over i & accumulation variable sum1 for 
        sum1 += f(a + (2*i-1)*h)    # building up the sum, one term @ a time.

    sum2 = 0
    for i in range(1, n/2):
        sum2 += f(a + 2*i*h)

    integral = (b-a)/(3*n)*(f(a) + f(b) + 4*sum1 + 2*sum2)
    return integral

def h(x):                      # Note: 'Simpson' can integrate any Python function f of 1 variable.
    return (3./2)*sin(x)**3

from math import sin, pi

def application():                               # We put these statements inside a function here called 'application',
    print 'Integral of 1.5*sin^3 from 0 to pi:'  # mainly to group them, & not because 'application' will be called several
    for n in 2, 6, 12, 100, 500:                 # times or w/different arguments.
        approx = Simpson(h, 0, pi, n)
        print 'n=%3d, approx=%18.15f, error=%9.2E' % \
              (n, approx, 2-approx)

def verify():                                                        # A better way of verifying the implementation is to look for
    """Check that 2nd-degree polynomials are integrated exactly."""  # test cases where the numerical approx. formula is exact. Since
    a = 1.5                                                          # it's stated that the formula is exact for polynomials up to 2nd
    b = 2.0                                                          # degree, we just test it on such an "arbitrary" parabola ...
    n = 8
    g = lambda x: 3*x**2 - 7*x + 2.5       # test integrand      # We can make 'verify' function more compact by utilizing lambda 
    G = lambda x: x**3 - 3.5*x**2 + 2.5*x  # integral of g       # functions for g and G.
    exact = G(b) - G(a)
    approx = Simpson(g, a, b, n)
    if abs(exact - approx) > 1E-14:   # never use == for floats!  # In 'if test' here, we avoid testing 'exact == approx' because
        print "Error: Simpson's rule should integrate g exactly"  # there may be round-off errors in these 'float' objects so that == fails.
                                                                  # Testing that the 2 variables are very close (distance less that 10^(-14))
def experiments():                                                # is better.   
    """Some other tests with known answers."""               
    from math import sin, pi, exp, log
    n = 200
    print 'sin from 0 to pi:', Simpson(sin, 0, pi, n)
    print 'exp from 0 to log(3):', Simpson(exp, 0, log(3), n)

verify()
application()
experiments()

"""
OUTPUT

bash-3.2$ python Simpson.py
Integral of 1.5*sin^3 from 0 to pi:
n=  2, approx= 3.141592653589793, error=-1.14E+00
n=  6, approx= 1.989171700583579, error= 1.08E-02
n= 12, approx= 1.999489233010781, error= 5.11E-04
n=100, approx= 1.999999902476350, error= 9.75E-08
n=500, approx= 1.999999999844138, error= 1.56E-10
sin from 0 to pi: 2.00000000068
exp from 0 to log(3): 2.00000000001

Note that running the call application() leads to the output

Integral of 1.5*sin^3 from 0 to pi:                                                                                                                  
n=  2, approx= 3.141592653589793, error=-1.14E+00                                                                                                    
n=  6, approx= 1.989171700583579, error= 1.08E-02                                                                                                    
n= 12, approx= 1.999489233010781, error= 5.11E-04                                                                                                    
n=100, approx= 1.999999902476350, error= 9.75E-08                                                                                                    
n=500, approx= 1.999999999844138, error= 1.56E-10  

Clearly see that approx. improves as n increases. However, every computation will give an answer that deviates from 
the exact value 2. We can't from this test alone know if the errors above are those implied by the approx. only, or if
there are additional programmable mistakes. Better way of verifying the implementation is therefore to look for test
cases where the numerical approx. formula is exact. This is why we also write and implement the 'experiments' function,
where we test an "arbitrary" parabola.

----------

A good exercise is to simulate the program flow by hand, starting w/call to 'application' function. A debugger
is a convenient tool for controlling that your thinking is correct.

W/debugger, can stop execution @ any perscribed line number, print out variables, continue execution, stop again, execute
statements one by one, & repeat such actions until you track down abnormal behavior & find bugs.

** 1. Start IPython

bash-3.2$ ipython
Python 2.7.1 (r271:86832, Jul 31 2011, 19:30:53) 
Type "copyright", "credits" or "license" for more information.

IPython 3.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

** 2. Run the program Simpson.py w/debugger on (-d):

In [1]: run -d Simpson.py
Breakpoint 1 at /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py:1
NOTE: Enter 'c' at the ipdb>  prompt to continue execution.
> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(1)<module>()
1---> 1 def Simpson(f, a, b, n=500):
      2     ...
      3     Return the approximation of the integral of f

** 3. Type 'continue' or just 'c' to go to first line of file. Now you can see printout of where we are in program. Each program line
      is numbered & arrow points to next line to be executed. This is called 'current line'.  

ipdb> c
Integral of 1.5*sin^3 from 0 to pi:
n=  2, approx= 3.141592653589793, error=-1.14E+00
n=  6, approx= 1.989171700583579, error= 1.08E-02
n= 12, approx= 1.999489233010781, error= 5.11E-04
n=100, approx= 1.999999902476350, error= 9.75E-08
n=500, approx= 1.999999999844138, error= 1.56E-10
sin from 0 to pi: 2.00000000068
exp from 0 to log(3): 2.00000000001

In [2]: run -d Simpson.py
Breakpoint 1 at /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py:1
NOTE: Enter 'c' at the ipdb>  prompt to continue execution.
> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(1)<module>()
1---> 1 def Simpson(f, a, b, n=500):
      2     ...
      3     Return the approximation of the integral of f

** 4. Can set a 'break point' where you want the program stop so that can examine variables and perhaps follow the execturion
      closely. Start by setting a break point in 'application' function:
    
ipdb> break application
Breakpoint 2 at /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py:32

** Can also say break X, where X is line number in file.

** 5. Continue exectution until the break point by writing 'continue' or 'c'. Now program stops at line 33 in 'application'
      function:

ipdb> c
> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(33)application()
2    32 def application():                               # We put these statements inside a function here called 'application',
---> 33     print 'Integral of 1.5*sin^3 from 0 to pi:'  # mainly to group them, & not because 'application' will be called several
     34     for n in 2, 6, 12, 100, 500:                 # times or w/different arguments.

** 6. Typiing 'step' or just 's' executes one statement @ a time. Let's test this feature:

ipdb> s
Integral of 1.5*sin^3 from 0 to pi:
> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(34)application()
     33     print 'Integral of 1.5*sin^3 from 0 to pi:'  # mainly to group them, & not because 'application' will be called several
---> 34     for n in 2, 6, 12, 100, 500:                 # times or w/different arguments.
     35         approx = Simpson(h, 0, pi, n)

ipdb> s
> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(35)application()
     34     for n in 2, 6, 12, 100, 500:                 # times or w/different arguments.
---> 35         approx = Simpson(h, 0, pi, n)
     36         print 'n=%3d, approx=%18.15f, error=%9.2E' % \

** Typing another 's' reaches the call to 'Simpson', and a new 's' steps into the function 'Simpson':

ipdb> s
--Call--
> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(1)Simpson()
1---> 1 def Simpson(f, a, b, n=500):
      2     ...
      3     Return the approximation of the integral of f

** Type a few more 's' to step ahead of the 'if' steps.

ipdb> s
> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(6)Simpson()
      5     ...
----> 6     if a > b:                                 # Here we test if b > a
      7         print 'Error: a=%g > b=%g' % (a, b)
	ipdb> s
	> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(11)Simpson()
	     10     # Check that n is even                               # Here we test if n is an even integer by making use of mod function:
	---> 11     if n % 2 != 0:                                       # mod(n,d) gives the remainder when n is divided by d (both n and d
	     12         print 'Error: n=%d is not an even integer!' % n  # are integers). In Python, percentage sign is used for the mod function.

	ipdb> s
	> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(15)Simpson()
	     14                                                          # an integer w/out any reminder (n % 2 ==0).
	---> 15     h = (b - a)/float(n)
	     16     sum1 = 0
** 7. Examining the contents of variables is easy w/'print' (or 'p') command:

	ipdb> print f, a, b, n
	<function h at 0x106565cf8> 0 3.14159265359 2

** Can also check the type of objects

	ipdb> whatis f
	Function h
	ipdb> hatis a
	*** SyntaxError: invalid syntax (<stdin>, line 1)
	ipdb> whatis a
	<type 'int'>
	ipdb> whatis b 
	<type 'float'>
	ipdb> whatis n
	<type 'int'>

** 8. Set a new break point in 'application' function so that can jump directly there w/out having to go manually through all the
      statements in the 'Simpson' function. To see line numbers & corresponding statements around some line w/numbers X, type
      'list X', For example,

	ipdb> list 32
	     27 def h(x):                      # Note: 'Simpson' can integrate any Python function f of 1 variable.
	     28     return (3./2)*sin(x)**3
	     29 
	     30 from math import sin, pi
	     31 
	2    32 def application():                               # We put these statements inside a function here called 'application',
	     33     print 'Integral of 1.5*sin^3 from 0 to pi:'  # mainly to group them, & not because 'application' will be called several
	     34     for n in 2, 6, 12, 100, 500:                 # times or w/different arguments.
	     35         approx = Simpson(h, 0, pi, n)
	     36         print 'n=%3d, approx=%18.15f, error=%9.2E' % \
	     37               (n, approx, 2-approx)

** Set line break @ line 35:

	ipdb> break 35
	Breakpoint 3 at /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py:35
	ipdb> n
	> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(16)Simpson()
	     15     h = (b - a)/float(n)
	---> 16     sum1 = 0
	     17     for i in range(1, n/2 + 1):     # We code the summation w/aid of 'for loop' over i & accumulation variable sum1 for

** Typing 'c' continues execution up to next break point, line 35.

	ipdb> c
	n=  2, approx= 3.141592653589793, error=-1.14E+00
	> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(35)application()
	     34     for n in 2, 6, 12, 100, 500:                 # times or w/different arguments.
	3--> 35         approx = Simpson(h, 0, pi, n)
	     36         print 'n=%3d, approx=%18.15f, error=%9.2E' % \

** 9. The command 'next' or 'n' is like 'step' or 's' in that current line is exectured, but the execution does not step into
      functions, instead the function calls are just performed & program stops @ next line:

	ipdb> n
	> /Users/markyashar/python_data_analysis/mytest_python/src/funcif/Simpson.py(36)application()
	3    35         approx = Simpson(h, 0, pi, n)
	---> 36         print 'n=%3d, approx=%18.15f, error=%9.2E' % \
	     37               (n, approx, 2-approx)

	ipdb> print approx, n
	1.98917170058 6

** 10. The command 'disable X Y Z' disables break points w/numbers X, Y, and Z & so on. To remove our 3 break points & continue
       execution until program naturally stops, we write

	ipdb> disable 1 2 3
	ipdb> c
	n=  6, approx= 1.989171700583579, error= 1.08E-02
	n= 12, approx= 1.999489233010781, error= 5.11E-04
	n=100, approx= 1.999999902476350, error= 9.75E-08
	n=500, approx= 1.999999999844138, error= 1.56E-10
	sin from 0 to pi: 2.00000000068
	exp from 0 to log(3): 2.00000000001

	In [3]:

"""
