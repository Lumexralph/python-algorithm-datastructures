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
  graph["start"]["a"] = 5
  graph["start"]["b"] = 2

  # add neighbours to the edges
  graph["a"] = {}
  graph["a"]["c"] = 4
  graph["a"]["d"] = 2

  graph["b"] = {}
  graph["b"]["a"] = 8
  graph["b"]["d"] = 7

  graph["c"] = {}
  graph["c"]["d"] = 6
  graph["c"]["fin"] = 3

  graph["d"] = {}
  graph["d"]["fin"] = 1

  # the finish node doesn't have neighbours
  graph["fin"] = {}

  # create another hash table to store the costs of the nodes
  # if you don't know the cost yet, put infinity
  infinity = float("inf")

  costs = {}
  costs["a"] = 5
  costs["b"] = 2
  costs["c"] = infinity
  costs["d"] = infinity
  costs["fin"] = infinity

  # create a place to store parents
  parents = {}
  parents["a"] = "start"
  parents["b"] = "start"
  parents["c"] = "a"
  parents["d"] = "b"
  parents["d"] = "a"
  parents["d"] = "c"
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

  print("The graph of the edges", graph)
  print("The costs of the edges", costs)
  print("The parents of the edges", parents)


dijkstra()