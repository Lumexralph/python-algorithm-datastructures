"""Although the Python list class provides a highly optimized implementation
of dynamic arrays,it is instructive to see how such a class might be implemented.
"""

# The key is to provide means to grow the array
# that stores the elements of a list

import ctypes                             # provides low level array


class DynamicArray(object):
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        # Create an empty array
        self._n = 0                                 # count actual elements
        self._capacity = 1                          # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array


    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k.
        either a positive or negative
        """
        if (0 > k > self._n):
            raise IndexError('invalid index')
        return self._A[k]                           # get the element from the array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:               # means the array is filled up and no room for new element
            self._resize(2 * self._capacity)        # double the capacity
        self._A[self._n] = obj                      # add the new object as the last element in the array
        self._n += 1                                # increase the length

    def _resize(self, c):                           # nonpublic utility
        """Resize internal array to capacity c"""
        B = self._make_array(c)                     # create a new bigger array

        for k in range(self._n):                    # perform the operation of copying over values to new array
            B[k] = self._A[k]
        self._A = B                                 # rewire ti the new array
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c"""

        return (c * ctypes.py_object)()

    def insert(self, index, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= index <= n in this version)

        if self._n == self._capacity:               # Means it is filled up and no enough room
            self._resize(2 * self._capacity)        # Double the size
        for j in range(self._n, index, -1):         # shift the right most
            self._A[j] = self._A[j - 1]
        self._A[index] = value
        self._n += 1                                # Update for addition of a new element

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        # we should shrink the array as the size changes

        for k in range(self._n):
            if self._A[k] == value:                 # Found a match
                for j in range(k, self._n - 1):     # shift others to fill the gap on the right
                    self._A[j] = self._A[j + 1]     # overwrite the value with the reamining elements
                self._A[self._n - 1] = None         # Since we are one element short and shifted, help garbage collection
                self._n -= 1                        # We have one less item
                return
        raise ValueError('value not found')         # when the value is not present

