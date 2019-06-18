"""Using the adapter pattern - a design pattern that
consists of modifying the methods of an existing class
to match the methods of a similar class or interface

This pattern is used with the List class to create a stack
and implement the behaviours of the stack using the methods
of the List class
"""

# create an appropriate class to raise an appropriate message
# for an empty stack as against the index error raised by List
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


# the stack
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self: bool) -> bool:
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, val):
        """Add element val to the top of the stack."""
        self._data.append(val)
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('stack is empty')
        
        return self._data[-1]           # return the last element in the stack/list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('stack is empty')
        
        return self._data.pop()