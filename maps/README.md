# Maps and Dictionaries

Python’s dict class is arguably the most significant data structure in the language. It represents an abstraction known as a dictionary in which unique keys are mapped to associated values. Because of the relationship they express between keys and values, dictionaries are commonly known as associative arrays or maps.

## Hash Tables

One of the most practical data structures for implementing a map, and the one that is used by Python’s own implementation of the dict class. This structure is known as a hash table(bucket array).

## Hash Functions

The hash function is used to map each key to an integer in the range [0, N - 1], where N is the capacity of the bucket array for a hash table.

If there are two or more keys with the same hash value, then two different items will be mapped to the same bucket in the bucket array. Then this means a COLLISION has occurred.

We say that a hash function is “good” if it maps the keys in our map so as to sufficiently minimize collisions. For practical reasons, we also would like a hash function to be fast and easy to compute.
However, only immutable data types (int, float, str, tuple and frozenset) are deemed hashable in Python. This is to ensure that a particular object’s hash code remains constant during that object’s lifespan

hash function = hash code + compression function

A good compression function is the one that minimizes the number of collisions for a given set of distinct hash codes.
