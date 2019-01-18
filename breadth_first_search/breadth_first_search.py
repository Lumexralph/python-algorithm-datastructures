"""Module for breadth first search algorithm"""

"""this is an double ended queue"""
from collections import deque

# implement the graph
graph = {}
graph["olu"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def breadth_first_search(name):

  # create a new queue
  search_queue = deque()
  searched = []

  # add all olu's neighbour in the queue
  search_queue += graph[name]

  while search_queue:
    # while the queue is not empty
    # take the first person off the queue
    person = search_queue.popleft()

    # if the person/node is not among searched node
    if not person in searched:
      if person_is_seller(person):
        print(f"{person} is a mango seller!")
        return True
      else:
        # if we didn't get the seller,
        # add the friends of this person to the queue
        search_queue += graph[person]
        # mark the person as searched, to avoid searching same node twice
        searched.append(person)

  return False


def person_is_seller(name):
  return name[-1] == 'm'


print(breadth_first_search("olu"))
