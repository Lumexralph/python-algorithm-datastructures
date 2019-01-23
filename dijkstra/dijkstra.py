"""Module for dijkstra's algorithm

breadth first search helps to know the path
with the fewer segments or nodes or hops
but if the time to travel through those points are
included we can't use the algorithm to get that
which brought about the need for dijkstra's algorithm
to help determine the faster path from one point to
to another point

steps:
1. Find the cheapest node(the node you can get to in
the least amount of time)

2. Check whether there’s a cheaper path to the neighbors
of this node. If so, update their costs

3. Repeat until you’ve done this for every node in the graph

4. Calculate the final path

NB: When you have a weighted graph, use dijkstra's algorithm but
when you have an unweighted graph, use breadth first search
dijkstra's algorithm only work for Directed Acyclic Graphs

In addition, it does not work with negative weight edges, the
algorithm to use for that is Bellman-Ford Algorithm

# converting a problem
# create the data structure (tables of nodes and their weights - how much
# to get to the node /the endpoint amidst different points)
# the nodes that hasn't been reached should have infinity initially

"""
# keep a list of nodes processed to avoid processing it twice
processed = []

def find_lowest_cost_node(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None

  # go through each node in the cost table
  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node

  return lowest_cost_node

def dijkstra():
  # create 3 hash tables
  # parents, costs, graph
  # update the cost and parents table as you proceed

  graph = {}
  graph["start"] = {}
  graph["start"]["a"] = 6
  graph["start"]["b"] = 2

  # add the neighbours of a and b
  graph["a"] = {}
  graph["a"]["fin"] = 1

  graph["b"] = {}
  graph["b"]["a"] = 3
  graph["b"]["fin"] = 5

  # the finish node doesn't have neighbours
  graph["fin"] = {}

  # create another hash table to store the costs of the nodes
  # if you don't know the cost yet, put infinity
  infinity = float("inf")

  costs = {}
  costs["a"] = 6
  costs["b"] = 2
  costs["fin"] = infinity

  # create a place to store parents
  parents = {}
  parents["a"] = "start"
  parents["b"] = "start"
  parents["fin"] = None

  node = find_lowest_cost_node(costs)

  while node is not None:
    cost = costs[node] # get the cost of the node
    neighbours = graph[node] # get the neighbours of that node

    for n in neighbours.keys(): # go through the costs of the neighbours
      new_cost = cost + neighbours[n] # add the cost of the node and that of the neighbour
      if costs[n] > new_cost: # if the calculated costs is less than than the initial cost
        costs[n] = new_cost
        parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)
