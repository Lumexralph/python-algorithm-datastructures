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
