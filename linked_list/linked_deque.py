"""implementation of a LinkedDeque class """

# create an appropriate class to raise an appropriate message
# for an empty stack as against the index error raised by List
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""

         # slot is used because of 1. faster attribute access.
        # 2. space savings in memory.
        # ref: https://stackoverflow.com/questions/472000/usage-of-slots

        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element                 # reference to user’s element
            self._prev = prev                       # reference to previous node
            self._next = next                       # reference to next node


    def __init__(self):
        """Create an empty list"""

        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                  # trailer is the next node after header
        self._trailer._prev = self._header                  # header is the node before trailer
        self._size = 0                                      # keep track of the number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, val, predecessor, successor):
        """Add element val between two existing nodes and return new node."""
        newest = self._Node(val, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

        return newest

    def _delete_node(self, node):
        """Delete nonsentinel/non-guard node from the list and return its element.

        Although the deleted node will be ignored by the rest of the list, setting its
        fields to None is advantageous as it may help Python’s garbage collection,
        since unnecessary links to the other nodes and the stored element are eliminated.
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor                       # unlink from the node and link the predecessor and successors
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record the deleted element
        node._prev = node.next = node._element = None       # clean uo the node to be deleted and leave for garbage collection

        return element


class LinkedDeque(_DoublyLinkedBase):
    """inherits from the DoublyLinkedBase class.

    We do not provide an explicit "init method" for the LinkedDeque class,
    as the inherited version of that method suffices to initialize a new instance.
    """

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')

        return self._header._next._element                                  # real item just after the header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')

        return self._trailer._prev._element                                 # real item just before trailer

    def insert_first(self, val):
        """Add an element to the front of the deque."""
        self._insert_between(val, self._header, self._header._next)         # after header
    
    def insert_last(self, val):
        """Add an element to the back of the deque."""
        self._insert_between(val, self._trailer._prev, self._trailer)       # insert before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')

        return self._delete_node(self._header._next)                        # use the inherited method

    def delete_last(self):
        """Remove and return the element from the end of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')

        return self._delete_node(self._trailer._prev)                        # use the inherited method

