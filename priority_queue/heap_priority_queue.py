from priority_queue.adt import PriorityQueueBase, Empty


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""

    # ---------- nonpublic behaviours -----------

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2
    
    def _has_left(self, j):
        # if the index is beyond the end of the list
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        # if the index is beyond the end of the list
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at the indices i, j of the array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _bubble_upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            # check if the value is less than the parent
            self._swap(j, parent)

            # recur at postion of parent
            self._bubble_upheap(parent)

    def _bubble_downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left

            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)

                # recur at the small_child's position till end of the tree
                self._bubble_downheap(small_child)

    def _heapify(self):
        # start at PARENT of last leaf, index of parent
        start = self._parent(len(self) - 1)

        # loop through the tree to the and include the tree
        # start from the end of the tree, the deepest level
        for j in range(start, -1, -1):
            # bubble down the heap as the case applies
            self._bubble_downheap(j)


    # ----------- public behaviours or operations --------

    def __init__(self, contents=()):
        """Create a new empty Priority Queue.

        By default, queue will be empty. If contents is given, it should be as an
        iterable sequence of (k,v) tuples specifying the initial contents. This optional implementation is
        needed because we might want to start with some initial entries
        """
        # empty by default
        self._data = [self._Item(k, v) for k, v in contents]

        if len(self._data) > 1:
            # Needed to create the heap to attain the heap-sort
            # order property
            self._heapify()

    def __len__data(self):
        """Return the number of items in the priority queue."""

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))

        # upheap the newly added element at the last postion
        self._bubble_upheap(len(self._data) - 1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty')

        # the minimum item will always be at the root
        item = self._data[0]

        return (item._key, item._value)

    def remove_min(self):
        """Return and remove (k,v) tuple with minimum key.

        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        
        # put the item at the end of the queue to the
        # minimum value's position and vice-versa
        self._swap(0, len(self._data) - 1)

        # remove the minimum value from the list
        item = self._data.pop()

        # rearrange the heap due to the position change
        # fix the new root
        self._bubble_downheap(0)
        return (item._key, item._value)
