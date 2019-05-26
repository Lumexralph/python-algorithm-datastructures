from array import array
from sys import getsizeof

primes = array('i', [5])

print(primes[0])

data = []

for k in range(10):
    a = len(data)                  # get number of elements
    b = getsizeof(data)            # get actual in bytes used to store the data list
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
