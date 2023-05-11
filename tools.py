import math
import copy

class Edge:
    def __init__(self, node1, node2, capacity):
        self.node1 = node1
        self.node2 = node2
        self.capacity = capacity
        self.flow = 0
        self.reverse = 0
        
    def equal(self,edge):
        if self.node1.name == edge.node1.name and self.node2.name == edge.node2.name:
            return True
        if self.node1.name == edge.node2.name and self.node2.name == edge.node1.name:
            return True
        return False
             

class Node:
    def __init__(self, name, value):
        self.name = name  #corresponde con el index en el array del grafo
        self.value = value

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def contain_edge(self, edge):
        return edge in self.edges
    
    def contain_node(self, node):
        return node in self.nodes

    def index(self, node):
        for i in range(0, len(self.nodes)):
            if node == self.nodes[i]:
                return i
        return -1
    
    def copy(self):
        return copy.deepcopy(self)
    
    def find(self, node1, node2):
        for edge in self.edges:
            if (edge.node1.name == node1.name and edge.node2.name == node2.name) or (edge.node2.name == node1.name and edge.node1.name == node2.name):
                return edge
        return None


    