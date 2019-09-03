from priority_queue.heap_priority_queue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a
    binary heap.
    """

    # -------------- nested Locator class --------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue.
        """
        __slots__ = '_index'            # add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    # ----------- nonpublic behaviours ----------------
    # override the swap to record new indices
    def _swap(self, i, j):
        super()._swap(i, j)             # perform the swap
        self._data[i]._index = i        # reset the locator index
        self._data[j] = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._bubble_upheap(j)
        else:
            self._bubble_downheap(j)

    # ---------- public behaviours -------------------
    def add(self, key, value):
        """Add a key-value pair"""
        # initialise the locator index
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._bubble_upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newvalue):
        """Update the key and value for the entry
        identified by Locator loc.
        """
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')

        loc._key = newkey
        loc._value = newvalue
        self._bubble(j)

    def remove(self, loc):
        """Remove and return the (k,v) pair identified by
        Locator loc.
        """
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')

        if j == len(self) - 1:                  # item at last position
            self._data.pop()                    # remove it
        else:
            self._swap(j, len(self) - 1)        # swap item to the last position
            self._data.pop()                    # remove it from the list
            self._bubble(j)                     # fix the item displaced by the swap

        return (loc._key,)
