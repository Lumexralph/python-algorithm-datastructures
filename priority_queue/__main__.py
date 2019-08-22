from .unsorted_priority_queue import UnsortedPriorityQueue

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
