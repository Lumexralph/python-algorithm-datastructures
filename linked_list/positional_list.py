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


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Postion"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not(self == other)

    def _validate(self, p):
        """Return position s node, or raise appropriate error if invalid."""

        if not isinstance(p, self.Position):
            raise TypeError('position p must be a proper Position type')
        
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None                                     # at the boundary of the list
        else:
            return self.Position(self, node)

    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
        
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)              # the inherited method

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p
        """
        original = self._validate(p)
        old_value = original._element                   # temporarily store old element
        original._element = e                           # replace with new element

        return old_value

