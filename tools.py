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
            if (edge.node1 == node1 and edge.node2 == node2) or (edge.node2 == node1 and edge.node1 == node2):
                return edge
        return None


def BFS(s,adj): # s, t representan indices
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


def PATH_EK(Gf,s,t): # Red residual, fuente, receptor
    path = BFS(Gf,s)
    p=[]
    
    if len(path)< 0 :
        return None
    
    node_temp = t
    while node_temp :
        parent = path[node_temp]
        p.append(parent)
        node_temp=parent
    
    return p    
        

def EDMONDS_KARP(G,s,t):
    edges  = G.edges
    nodes = G.nodes
    Gf = G
    p = PATH_EK(Gf,s,t)
    while p!= None:
        for
        c_p = min()
    
