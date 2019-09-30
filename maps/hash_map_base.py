from random import randrange

from map_base import MapBase
from unsorted_table_map import UnsortedTableMap


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression"""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map"""
        self._table = cap * [None]
        self._n = 0                         # number of entries in the map
        self._prime = p                     # prime for MAD compression
        self._scale = 1 + randrange(p - 1)  # scale from 1 to p-1 for MAD
        self._shift = randrange(p)          # scale from 0 to P-1 for MAD

    def _hash_function(self, k):
        return hash((k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)       # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)           #subroutine that maintains self._n
        if self._n > len(self._table) // 2:         # keep load factor <= 0.5 to reduce the chances of collision
            self._resize(2 * len(self._table) - 1)          # number 2^x - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1                    # reflect the decrease in the key value pairs/entries

    def _resize(self, c):               # resize the bucket to capacity c
        old = list(self.items())        # return a list of tuples of the key and values of old items
        self._table = c * [None]        # resize the table to the desired capacity
        self._n = 0                     # reset n to be recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v                 # reinsert the existing key-value pair into the new table


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]         # go to the hash table, get the bucket or entry relating to the hash
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:         # check if the entry  is new
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v

        if len(self._table) > oldsize:       # key is new entry to the table
            self._n += 1                      # increase in the overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))

        del bucket[k]

    def __iter__(self):
        # use a generator to return the value on demand
        for bucket in self._table:
            if bucket is not None:          # a non-empty slot
                for key in bucket:
                    yield key