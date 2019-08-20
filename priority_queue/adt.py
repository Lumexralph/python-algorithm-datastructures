"""Module containing the implementation"""


class PriorityQueueBase:
    """Abstract base class for a priority queue"""

    # using a composition design pattern to
    # group instances with same operations but
    # maintaining their individual states
    class _Item:
        """Lightweight composite to store priority queue elements"""
        __slots__ = '_key', '_value'         # helps for fast insertion and access and reduce memory space

        def __init__(self, k, v):
            self._key = k
            self._value = v

        # to achieve the a < b attribute for the key
        def __lt__(self, other):
            # compare items based on their keys
            return self._key < other._key

    def is_empty(self) -> bool:
        """Return True if the priority queue is empty."""
        return len(self) == 0
