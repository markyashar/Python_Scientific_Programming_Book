infile = open('data1.txt', 'r')
numbers = [float(w) for w in infile.read().split()]
mean = sum(numbers)/len(numbers)
print mean
infile.close()

"""
OUTPUT:

bash-3.2$ python mean3.py
20.95

"""
