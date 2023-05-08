import math

class Edge:
    def __init__(self, node1, node2, capacity):
        self.node1 = node1
        self.node2 = node2
        self.capacity = capacity
        self.flow = 0 

class Node:
    def __init__(self, name, value):
        self.name = name  #corresponde con el index en el array del grafo

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges


def BFS(s,t,adj): # s, t representan indices
    queue = []
    path = []
    d = []
    queue.append(s)
    path.append(-1)
    
    for i in range(len(adj)):
        d[i] = math.inf
    d[s] = 0
    
    while len(queue):
        u = queue.pop(0)
        for v in adj[u]:
            if d[v] == math.inf:
                d[v] = d[u]+1
                path[v] = u
                queue.append(v)    
        
    return path    