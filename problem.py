from regex import REVERSE
from generador import *

def BFS(s,adj): # s, t representan indices
    queue = []
    path = []
    d = []
    queue.append(s)
    
    for i in range(len(adj)):
        d.append(math.inf)
        path.append(None)
    d[s.name] = 0

    while len(queue):
        u = queue.pop(0)
        
        for v in adj[u.name]:
            if d[v.name] == math.inf:
                d[v.name] = d[u.name]+1
                path[v.name] = u
                queue.append(v)    
    return path    

        
def PATH_EK(s,t,adj): # Red residual, fuente, receptor
    path = BFS(s,adj)
    
    if path[t.name] is None :
        return None
    
    p=[]
    node_temp = t

    while not node_temp == None :
        p.append(node_temp)
        parent = path[node_temp.name]
        node_temp=parent
    
    return p    
        

def EDMONDS_KARP(G,s,t,adj):
    Gf = G.copy()
    p = PATH_EK(s,t,adj) #Devuelve el camino desde la fuente al receptor
    cp = math.inf
    edges_gf = []
        
    while p is not None:
        p.reverse()
        edges_gf.clear()
        #Busca la capacidad minima
        for i in range(0,len(p)-1):
            edge = Gf.find(p[i],p[i+1])
            if not edge == None:
                edges_gf.append(edge)
                r = edge.capacity - edge.flow #Si la arista esta saturada
                if r:
                    cp = min(cp,r)
                else:
                    cp = min(cp,edge.reverse)    
                    
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
        p = PATH_EK(s,t,adj)    
    
    road = []
    city = []
    road_name=[]
    # Obtiene las ciudades no saturadas
    for c in adj[t.name]:
        if adj[c.name].count(t):
            city.append(c)
    
    
    for r in G.edges:
        if r.node1.value:
            count = city.count(r.node2)
            if not count :
                if not road.count(r.node1) :
                    road.append(r.node1)
            elif road.count(r.node1):
                road.remove(r.node1)    
    
    for r in road:
        road_name.append(r.name)
                    
    return road_name
    
    
    
    
    



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
    e = 1
    for edge in graph.edges:
        #crear el nodo que representa la arista en el grafo
        node = Node(len(nodes), e)
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
        e = e+1

    receptor.name=len(nodes)

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

#------------------------------------------------------------------------------------------

node1 = Node(0, 9)
node2 = Node(1, 8)
# node3 = Node(2, 7)
# node4 = Node(3, 6)

# node5 = Node(4, 5)
# node6 = Node(5, 4)
# node7 = Node(6, 3)
# node8 = Node(7, 2)

# node9 = Node(8, 1)

edge1 = Edge(node1, node2, 20)
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
