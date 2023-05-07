class Edge:
    def __init__(self, node1, node2, cost):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
