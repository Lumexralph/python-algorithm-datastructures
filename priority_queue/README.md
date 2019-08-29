# Priority Queue

## Reasons

There are many applications in which a queue-like structure is used to manage objects that must be processed in some way, but for which the first-in, first-out policy does not suffice. Consider, for example, an air-traffic control center that has to decide which flight to clear for landing from among many approaching the airport. This choice may be influenced by factors such as each plane’s distance from the runway, time spent waiting in a holding pattern, or amount of remaining fuel. It is unlikely that the landing decisions are based purely on a FIFO policy.
There are other situations in which a “first come, first serve” policy might seem reasonable, yet for which other priorities come into play. To use another airline analogy, suppose a certain flight is fully booked an hour prior to departure. Be- cause of the possibility of cancellations, the airline maintains a queue of standby passengers hoping to get a seat. Although the priority of a standby passenger is influenced by the check-in time of that passenger, other considerations include the fare paid and frequent-flyer status. So it may be that an available seat is given to a passenger who has arrived later than another, if such a passenger is assigned a better priority by the airline agent.

## What is a Priority Queue

This is a collection of prioritized elements that allows arbitrary element insertion, and allows the removal of the element that has first priority. When an element is added to a priority queue, the user designates its priority by providing an associated key.

![Operations in a priority Queue - Python](p_queue.png)

## Implementation

- Using  unsorted list
- Using sorted list
- Using Binary Heap

### Binary Heap

It is a binary tree that stores collection of items at its positions and satisfies two additional properties:
a relational property defined in terms of the way keys are stored in T and a structural property defined in terms of the shape of T itself

![Example of a heap storing 13 entries with integer keys. The last position
is the one storing entry (13,W )](binary_heap.png)
Example of a heap storing 13 entries with integer keys. The last position
is the one storing entry (13,W )
