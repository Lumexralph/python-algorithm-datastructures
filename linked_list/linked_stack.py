# create an appropriate class to raise an appropriate message
# for an empty stack as against the index error raised by List
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""

        # slot is used because of 1. faster attribute access.
        # 2. space savings in memory.
        # ref: https://stackoverflow.com/questions/472000/usage-of-slots

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element                 # reference to user’s element
            self._next = next                       # reference to next node

    
    def __init__(self):
        """Create an empty stack."""
        self._head = None                           # reference to the head node
        self._size = 0                              # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)      # Create and link the node with the element
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty."""
        
        if  self.is_empty():
            raise Empty('Stack is empty')
        
        return self._head._element                  # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        
        Raise Empty exception if the stack is empty."""

        if self.is_empty():
            raise Empty('Stack is empty')

        value = self._head._element                 # store the element to be unlinked
        self._head = self._head._next               # link the head to the next element
        self._size -= 1                             # reduce the size of the list
        return value