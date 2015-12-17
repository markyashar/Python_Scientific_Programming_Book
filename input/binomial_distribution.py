# Exercise 4.24: Compute the binomail distribution
# Author: Noah Waterfield Price

"""
Consider uncertain event where there are 2 outcomes only, typically success or faiure. Example: flipping
a coin -- outcome is uncertain & of 2 types, either head (can be considered as success) or tail (failure). 
Throwing a die can be another example, if (e.g.) geting a 6 is considered success & all other outcomes represent
failure. Let probability of success be p & that of failure 1-p. If we perform n experiments, where outcome of
each experiment does not depend on outcome of previous experiments, probability of getting success x times
(& failure n-x times) is given by

B(x,n,p) = [n!*p^x*(1-p)^(n-x)]/[x!*(n-x)!]  

p = probability of success ; n = number of experiments performed.
x = number of times we get a success.

This formula's called binomial distribution. Expression x! is factorial of x. Implement binomial distribution
expression in a function 'binomial(x, n, p)'. Make a module containing this 'binomial' function. Include a test
block @ end of module file.
"""
import sys


def fact(n):
    ans = 1
    if n == 0 or n == 1:
        return ans
    else:
        while n > 0:
            ans *= n
            n -= 1
    return ans


def binomial(x, n, p):
    B = float(fact(n)) / (fact(x) * fact(n - x)) * p ** x * (1 - p) ** (n - x)
    return B

if __name__ == "__main__":

    """
Python allows a special construction to let a file act both as a module w/function definitions only and
as an ordinary program that we can run, i.e., w/statements that apply the functions & possibly write output.
This 2-fold 'magic' consists of putting the application part after an 'if' test of the form of what is above
& below these comment lines. The '__name__' variable is automatically defined in any module & equals the module
name if module file is imported in another program, or '__name__' equals the string '__main__' if the module
file is run as a program. This implies that the block of statements after ' if __name__ == '__main__': ' is 
executed if and only if we run the module file as a program. Such block of statements is referred to as the
test block of a module.
    """
    try:
        x = int(sys.argv[1])
        n = int(sys.argv[2])
        p = float(sys.argv[3])
    except IndexError:
        print 'x, n and p must be supplied on the command line'
        sys.exit(1)
    except ValueError:
        print 'x and n must be real integers'
        sys.exit(1)

    print binomial(x, n, p)

"""
Sample run:
python binomial_distribution.py 3 3 0.5
0.125
python binomial_distribution.py 2 5 0.5
0.3125
bash-3.2$ python binomial_distribution.py 3 3 0.5
0.125
bash-3.2$ python binomial_distribution.py 7 13 0.3
0.0441523990908
bash-3.2$ python binomial_distribution.py 6 63 0.8
2.56690920825e-33
bash-3.2$ python binomial_distribution.py 9 13 0.3
0.0033790101345
bash-3.2$ python binomial_distribution.py 2 13 0.3
0.138808337359

"""
