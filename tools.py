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


def BFS(s,adj): # s, t representan indices
    queue = []
    path = []
    d = []
    queue.append(s)
    
    for i in range(len(adj)):
        d.append(math.inf)
        path.append(-1)
    d[s.name] = 0

    
    while len(queue):
        u = queue.pop(0)

        print("u")
        print(u.name)

        for v in adj[u.name]:
            if d[v.name] == math.inf:
                d[v.name] = d[u.name]+1
                path[v.name] = u
                queue.append(v)    
        

    return path    

        
def PATH_EK(Gf,s,t,adj): # Red residual, fuente, receptor
    path = BFS(s,adj)
    p=[]
    
    if len(path) < 0 :
        return None
    
    node_temp = t


    while not node_temp == -1 :

        parent = path[node_temp.name]
        p.append(parent)
        node_temp=parent
    
    return p    
        

def EDMONDS_KARP(G,s,t,adj):
    
    edges  = G.edges
    nodes = G.nodes
    Gf = G.copy()
    p = PATH_EK(Gf,s,t,adj)
    
    while not (len(p) == 1 and p[0] == -1):
        
        node1=None
        node2= t 
        
        cp = math.inf
        edges_gf = []
        for i in range(0,len(p)):
            if (i+1)%2 == 0:
                edge = Gf.find(node1,node2)

                
                if not edge == None:

                    print("edge")
                    print(edge.capacity)

                    edges_gf.append(edge)
                    r = edge.capacity - edge.flow #Si la arista esta saturada
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
                if e.capacity - e.flow <=0:
                    i = e.node1.name
                    j = e.node2
                    remove_node(ady[i], j)
                
            else: #si es la arista inversa
                e.flow = e.flow - cp
                e.reverse = e.reverse - cp
                if e.reverse <=0:
                    i = e.node2.name
                    j = e.node1
                    remove_node(ady[i], j)
                if e.capacity - e.flow > 0:
                    i = e.node1.name
                    j = e.node2
                    adj[i].append(j)
        p = PATH_EK(Gf,s,t,adj)
    
    solucion = []
    carreteras = []
    mark_nodes = []

    for i in range(0, len(ady[0])):
        carreteras.append(ady[0][i])
        mark_nodes.append(0)

    for item in ady[t.name]:
        for carretera in ady[item.name]:
            carr = [i for i in range(0, len(carreteras)) if carreteras[i].name == carretera.name]
            if not len(carr) == 0:
                mark_nodes[carr[0]] = 1

    for i in range(0, len(carreteras)):
        if mark_nodes[i] == 0:
            solucion.append(carreteras[i])
    return solucion



def remove_node(ady, node):
    ady_copy = ady
    for item in ady_copy:
        if item.name == node.name:
            ady.remove(item)
            return
    
    
                

def convert_to_flow(graph):
    fuente = Node(0, 0)
    receptor = Node("receptor", 0)
    nodes = [fuente]
    edges = []

    for edge in graph.edges:
        #crear el nodo que representa la arista en el grafo
        node = Node(len(nodes), 0)
        nodes.append(node)
        #crear la arista entre la fuente y el nodo creado
        edges.append(Edge(nodes[0], node, edge.capacity))

        #crear los 2 nodos de la arista
        node1 = Node(len(nodes), 0)
        nodes.append(node1)
        node2 = Node(len(nodes), 0)
        nodes.append(node2)
        
        edges.append(Edge(node, node1, math.inf))

        edges.append(Edge(node, node2, math.inf))

        edges.append(Edge(node1, receptor, edge.node1.value))
        edges.append(Edge(node2, receptor, edge.node2.value))

    receptor.name=len(nodes)

    print("receptor.name")
    print(receptor.name)

    nodes.append(receptor)

    return Graph(nodes, edges)

def ady_list(graph):
    ady = []
    for node in graph.nodes:
        l = []
        # print("Node")
        # print(node.name)
        for edge in graph.edges:
            if edge.node1 == node:
                l.append(edge.node2)
                # print("Vecino")
                # print(edge.node2.name)
            elif edge.node2 == node:
                l.append(edge.node1)
                # print("Vecino")
                # print(edge.node1.name)
        ady.append(l)
    return ady

node1 = Node(0, 9)
node2 = Node(1, 8)
# node3 = Node(2, 7)
# node4 = Node(3, 6)

# node5 = Node(4, 5)
# node6 = Node(5, 4)
# node7 = Node(6, 3)
# node8 = Node(7, 2)

# node9 = Node(8, 1)

edge1 = Edge(node1, node2, 10)
# edge2 = Edge(node2, node3, 20)

# edge3 = Edge(node3, node4, 30)
# edge4 = Edge(node4, node5, 40)

# edge5 = Edge(node5, node6, 50)
# edge6 = Edge(node6, node7, 60)

# edge7 = Edge(node7, node8, 80)
# edge8 = Edge(node8, node9, 70)

# nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9]

# edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8]

nodes = [node1, node2]

edges = [edge1]

grafo = Graph(nodes, edges)


# for l in ady_list(grafo):
#     print(l)

red_flujo = convert_to_flow(grafo)

ady = ady_list(red_flujo)

print(EDMONDS_KARP(red_flujo,red_flujo.nodes[0],red_flujo.nodes[len(red_flujo.nodes)-1],ady))

# for node in red_flujo.nodes:
#     print("Nodo")
#     print(node.name)
# for edge in red_flujo.edges:
#     print("Arista")
#     print(edge.capacity)
#     print(edge.node1.name)
#     print(edge.node2.name)
