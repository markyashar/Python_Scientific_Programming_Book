# Exercise 3.2: Defind a Python function sum_1_div_k(M) tgat reurns the sum s as defined in a previous
# exercise. Print out the result of calling s(3) & check that the answer is correct.
def sum_1_div_k(M):
# def sum_1_div_k(M=100):  # (gives the same answer)  
    s = 0
    k = 1
    while k <= M:
        s += 1. / k
        k += 1
    print s

sum_1_div_k(3)

"""
Sample run:
python sum_func.py
1.83333333333
"""
