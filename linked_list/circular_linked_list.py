# create an appropriate class to raise an appropriate message
# for an empty stack as against the index error raised by List
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

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
        """Create an empty queue."""

        self._tail = None                           # represent tail of queue
        self._size = 0                              # number of elements in the queue

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')

        oldhead = self._tail._next
        if self._size == 1:                         # removing only element
            self._tail = None                       # queue becomes empty
        else:
            self._tail._next = oldhead._next        # bypass the old head and create a new link
        
        self._size -= 1
        return oldhead._element

    def enqueue(self, val):
        """Add an element to the back of queue."""

        newest_node = self._Node(val, None)         # node will be new tail node
        if self.is_empty():
            newest_node._next = newest_node         # initialize circularly
        else:
            newest_node._next = self._tail._next    # new node points to head
            self._tail._next = newest_node          # old tail points to new node

        self._tail = newest_node
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""

        if self._size > 0:
            self._tail = self._tail._next           # old head becomes new tail


