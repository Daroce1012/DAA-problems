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
    G = Graph()
    
    edges  = G.edges
    nodes = G.nodes
    Gf = G.copy()
    Gf = Graph()
    p = PATH_EK(Gf,s,t)
    
    while p!= None:
        
        node1=None
        node2= t
        
        cp = math.inf
        edges_gf = []
        for i in range(1,len(p)):
            if i%2 == 0:
                edge = Edge(Gf.find(node1,node2))
                edges_gf.append(edge)
                r = edge.capacity-edge.flow #Si la arista esta saturada
                if r:
                    cp = min(cp,r)
                else:
                    cp = min(cp,edge.reverse)    
                node2 = p[i]
            else: node1 = p[i]
        
        for e in edges_gf:
            if Gf.contain_edge(e):
                e.flow = e.flow+cp
                e.reverse = e.reverse + cp
                
            else: 
                e.flow = e.flow - cp
                e.reverse = e.reverse - cp
            #update (𝑢,𝑣) and (𝑣,𝑢) in 𝐺_𝑓

