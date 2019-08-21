from adt import PriorityQueueBase, Empty
from linked_list.positional_list import PositionalList


class UnsortedPriorityQueue(PriorityQueueBase):
    """priority queue implemented with an unsorted list"""

    def _find_min(self):                    # non public entity
        """Return Position of item with minimum key"""
        if self.is_empty():                 # is_empty inherited from the base class
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)

        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair"""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove the element with the minimum key"""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


# ===============================================
# create an empty queue
priority_queue = UnsortedPriorityQueue()

# add elements to the queue
priority_queue.add(1, 'go to shop')
priority_queue.add(2, 'fetch water')
priority_queue.add(4, 'start chapter 5')
priority_queue.add(3, 'go get car document')
priority_queue.add(7, 'call mum')
priority_queue.add(6, 'prepare launch')

# get the minimun value
print(priority_queue.min())

# remove it and get the next minimum
print(priority_queue.remove_min())

# get the minimum value
print(priority_queue.min())
