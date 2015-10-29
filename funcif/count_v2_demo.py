# Here we iterate directly over the string

def count_v2_demo(dna, base):
    print 'dna:', dna
    print 'base:', base
    i = 0 # counter
    for c in dna:
        print 'c:', c
        if c == base:
            print 'True if test'
            i += 1
    return i

dna = 'ATGCGGACCTAT'
base = 'C'

n = count_v2_demo('ATGCGGACCTAT', 'C')
print n

# printf-style formatting
print '%s appears %d times in %s' % (base, n, dna)

# or (new) format string syntax
print '{base} appears {n} times in {dna}'.format(base=base, n=n, dna=dna)

"""
OUTPUT

bash-3.2$ python count_v2_demo.py
dna: ATGCGGACCTAT
base: C
c: A
c: T
c: G
c: C
True if test
c: G
c: G
c: A
c: C
True if test
c: C
True if test
c: T
c: A
c: T
3
C appears 3 times in ATGCGGACCTAT
C appears 3 times in ATGCGGACCTAT

-------

Using Python Debugger: Use s (for step) to step through each statement, or n (next)
for proceeding to the next statement w/out stepping through a function that's called:

bash-3.2$ python -m pdb count_v2_demo.py
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(3)<module>()
-> def count_v2_demo(dna, base):
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(14)<module>()
-> dna = 'ATGCGGACCTAT'
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(15)<module>()
-> base = 'C'
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(17)<module>()
-> n = count_v2_demo('ATGCGGACCTAT', 'C')
(Pdb) s
--Call--
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(3)count_v2_demo()
-> def count_v2_demo(dna, base):
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(4)count_v2_demo()
-> print 'dna:', dna
(Pdb) s
dna: ATGCGGACCTAT
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(5)count_v2_demo()
-> print 'base:', base
(Pdb) s
base: C
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(6)count_v2_demo()
-> i = 0 # counter
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(7)count_v2_demo()
-> for c in dna:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(8)count_v2_demo()
-> print 'c:', c
(Pdb) s
c: A
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(9)count_v2_demo()
-> if c == base:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(7)count_v2_demo()
-> for c in dna:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(8)count_v2_demo()
-> print 'c:', c
(Pdb) s
c: T
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(9)count_v2_demo()
-> if c == base:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(7)count_v2_demo()
-> for c in dna:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(8)count_v2_demo()
-> print 'c:', c
(Pdb) s
c: G
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(9)count_v2_demo()
-> if c == base:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(7)count_v2_demo()
-> for c in dna:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(8)count_v2_demo()
-> print 'c:', c
(Pdb) s
c: C
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(9)count_v2_demo()
-> if c == base:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(10)count_v2_demo()
-> print 'True if test'
(Pdb) s
True if test
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(11)count_v2_demo()
-> i += 1
(Pdb) s
.
.
.
c: C
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(9)count_v2_demo()
-> if c == base:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(10)count_v2_demo()
-> print 'True if test'
(Pdb) s
True if test
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(11)count_v2_demo()
-> i += 1
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(7)count_v2_demo()
-> for c in dna:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(8)count_v2_demo()
-> print 'c:', c
(Pdb) s
c: T
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(9)count_v2_demo()
-> if c == base:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(7)count_v2_demo()
-> for c in dna:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(8)count_v2_demo()
-> print 'c:', c
(Pdb) s
c: A
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(9)count_v2_demo()
-> if c == base:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(7)count_v2_demo()
-> for c in dna:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(8)count_v2_demo()
-> print 'c:', c
(Pdb) s
c: T
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(9)count_v2_demo()
-> if c == base:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(7)count_v2_demo()
-> for c in dna:
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(12)count_v2_demo()
-> return i
(Pdb) s
--Return--
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(12)count_v2_demo()->3
-> return i
(Pdb) s
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(18)<module>()
-> print n
(Pdb) s
3
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(21)<module>()
-> print '%s appears %d times in %s' % (base, n, dna)
(Pdb) s
C appears 3 times in ATGCGGACCTAT
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(24)<module>()
-> print '{base} appears {n} times in {dna}'.format(base=base, n=n, dna=dna)
(Pdb) s
C appears 3 times in ATGCGGACCTAT
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(51)<module>()
(....
Pdb) s
--Return--
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(51)<module>()->None
-> .....
(Pdb) s
--Return--
> <string>(1)<module>()->None
(Pdb) s
The program finished and will be restarted
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(3)<module>()
.
.
.

---------

Observe the output of the print statements. One can also print a variable explicitly
inside the debugger:

--Call--
> /Users/markyashar/mytest_python/src/funcif/count_v2_demo.py(3)count_v2_demo()
-> def count_v2_demo(dna, base):
(Pdb) print base
C
(Pdb) 

---------

Misundertanding of program flow is one of most frequent sources of programming errors, so whenever in doubt about
any program flow, enter debugger to establish confidence.

"""

