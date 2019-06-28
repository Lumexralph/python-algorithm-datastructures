# create an appropriate class to raise an appropriate message
# for an empty stack as against the index error raised by List
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

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

        self._head = None
        self._tail = None
        self._size = 0                              # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""

        if self.is_empty():
            raise Empty('Queue is empty')
        
        return self._head.element                   # the node in the head is the element in the front

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        
        answer = self._head.element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None                       # removed head had been the tail

        return answer

    def enqueue(self, val):
        """Add an element to the back of queue."""

        newest_node = self._Node(val, None)         # node will be new tail node
        if self.is_empty():
            self._head = newest_node                # special case: previously empty queue
        else:
            self._tail._next = newest_node
        
        self._tail = newest_node                    # update reference to tail node
        self._size += 1

