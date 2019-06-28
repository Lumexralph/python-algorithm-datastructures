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


"""
An insertion sort implementation that operates on a PositionalList,
relying on the same high-level algorithm in which each
element is placed relative to a growing collection of
previously sorted elements.
"""
def insertion_sort(p_list):
    """Sort PositionalList of comparable elements into ascending order."""
    if len(p_list) > 1:                             # list of length 0 or 1 is sorted
        marker = p_list.first()
        while marker != p_list.last():
            pivot = p_list.after(marker)            # next item to place
            value = pivot.element()
            if value > marker.element():            # pivot is already sorted
                marker = pivot                      # pivot becomes new marker
            else:                                   # must relocate pivot to be before marker
                walk = marker                       # find leftmost item greater than value
                while (walk != p_list.first() and
                        p_list.before(walk).element() > value):
                    walk = p_list.before(walk)
                p_list.delete(pivot)
                p_list.add_before(walk, value)       # reinsert value before walk
            

"""
Implement a favorites list by making use of a PositionalList for storage.

If elements of the positional list were simply elements of the favorites list,
we would be challenged to maintain access counts and to keep the proper count
with the associated element as the contents of the list are reordered.
We use a general object-oriented design pattern, the composition pattern,
in which we define a single object that is composed of two or more other objects.
"""
class FavouritesList:
    """List of elements ordered from most frequently accessed to least."""
    
    class _Item:
         # slot is used because of
         # 1. faster attribute access.
         # 2. space savings in memory.
         # ref: https://stackoverflow.com/questions/472000/usage-of-slots
        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e                             # the user s element
            self._count = 0                             # access count is initially zero
        
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p == self._data.first():
            count = p.element()._count
            walk = self._data.before(p)
            if count > walk.element()._count:                              # must shift forward
                while (walk != self._data.first() and
                        count > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)

                self._data.add_before(walk, self._data.delete(p))           # delete/reinsert
    
    def __init__(self):
        """Create an empty list of favorites."""
        self._data = PositionalList()                                       # list of Item instances

    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self._data)
    
    def is_empty(self):
        """Return True if list is empty."""
        return len(self._data) == 0
    
    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)                                          # try to locate existing element
        if p is None:
            new_item = self._Item(e)
            p = self._data.add_last(new_item)                               # if new, place at end of the list
        p.element()._count += 1                                             # always increment count
        self._move_up(p)                                                    # consider moving forward

    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e)                                          # try to locate existing element
        if p is not None:
            self._data.delete(p)                                            # delete if found
    
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()                                           # element of list is Item
            yield item._value                                               # using the customized __iter__ method
            walk = self._data.after(walk)

        
"""
The previous implementation of a favorites list performs the access(e) method 
in time proportional to the index of e in the favorites list. 
That is, if e is the kth most popular element in the favorites list,
then accessing it takes O(k) time. In many real-life access sequences (e.g., Web pages visited by a user),
once an element is accessed it is more likely to be accessed again in the near future. 
Such scenarios are said to possess locality of reference.
A heuristic, or rule of thumb, that attempts to take advantage of the locality of reference
 that is present in an access sequence is the move-to-front heuristic. To apply this heuristic, 
 each time we access an element we move it all the way to the front of the list. Our hope, of course, 
 is that this element will be accessed again in the near future. Consider, for example, 
 
 a scenario in which we have n elements and the following series of n2 accesses:
• element 1 is accessed n times • element 2 is accessed n times
• element n is accessed n times.
If we store the elements sorted by their access counts, inserting each element the first time it is accessed, then
• each access to element 1 runs in O(1) time
• each access to element 2 runs in O(2) time
• each access to element n runs in O(n) time.
Thus, the total time for performing the series of accesses is proportional to
n+2n+3n+···+n·n = n(1+2+3+···+n) = n· n(n+1), 2
which is O(n3).

On the other hand, if we use the move-to-front heuristic, inserting each element
the first time it is accessed, then
• each subsequent access to element 1 takes O(1) time
• each subsequent access to element 2 takes O(1) time
• each subsequent access to element n runs in O(1) time.
So the running time for performing all the accesses in this case is O(n2). 
Thus, the move-to-front implementation has faster access times for this scenario. 
Still, the move-to-front approach is just a heuristic, for there are access sequences 
where using the move-to-front approach is slower than simply keeping the favorites list ordered by access counts.

MTF : Move To Front
"""
class FavouritesListMTF(FavouritesList):
    """List of elements ordered with move-to-front heuristic."""
    # override move up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))              # remove or delete it from initial place and reinsert in new position

    # override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        
        # making a copy of the original list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        # repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # found the element with highest count
            yield highPos.element()._value                          # report element to user
            temp.delete(highPos)
