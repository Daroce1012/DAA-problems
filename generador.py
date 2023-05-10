from tools import *
# class Edge:
#     def __init__(self, node1, node2, capacity):
#         self.node1 = node1
#         self.node2 = node2
#         self.capacity = capacity
#         self.flow = 0
#         self.reverse = 0
        
#     def equal(self,edge):
#         if self.node1.name == edge.node1.name and self.node2.name == edge.node2.name:
#             return True
#         if self.node1.name == edge.node2.name and self.node2.name == edge.node1.name:
#             return True
#         return False
             

# class Node:
#     def __init__(self, name, value):
#         self.name = name  #corresponde con el index en el array del grafo
#         self.value = value

# class Graph:
#     def __init__(self, nodes, edges):
#         self.nodes = nodes
#         self.edges = edges

#     def contain_edge(self, edge):
#         return edge in self.edges
    
#     def contain_node(self, node):
#         return node in self.nodes

#     def index(self, node):
#         for i in range(0, len(self.nodes)):
#             if node == self.nodes[i]:
#                 return i
#         return -1
    
#     def copy(self):
#         return copy.deepcopy(self)
    
#     def find(self, node1, node2):
#         for edge in self.edges:
#             if (edge.node1.name == node1.name and edge.node2.name == node2.name) or (edge.node2.name == node1.name and edge.node1.name == node2.name):
#                 return edge
#         return None

def tester_solution(grafo, edges_to_build, cities_to_build, pos):

    if pos == len(grafo.edges):
        presp = Obtener_presupuesto(grafo, edges_to_build, cities_to_build)
        return presp

    max_pres = 0

    for i in range(pos, len(grafo.edges)):

        visitado1= False
        visitado2 = False
        

        pres_1 = tester_solution(grafo, edges_to_build, cities_to_build, i+1)

        edges_to_build[i] = 1

        vert1 = grafo.edges[i].node1
        vert2 = grafo.edges[i].node2

        if not cities_to_build[vert1.name] == 1:
            visitado1 = True
            cities_to_build[vert1.name] = 1
        if not cities_to_build[vert2.name] == 1:
            visitado2 = True
            cities_to_build[vert2.name] = 1

        pres_2 = tester_solution(grafo, edges_to_build, cities_to_build, i+1)

        edges_to_build[i] = 0

        if visitado1:
            cities_to_build[vert1.name] = 0
        if visitado2:
            cities_to_build[vert2.name] = 0

        if max(pres_1, pres_2) > max_pres:
            max_pres = max(pres_1, pres_2)

    return max_pres



def Obtener_presupuesto(grafo, edges_to_build, cities_to_build):
    presup = 0
    for i in range(0, len(edges_to_build)):
        if edges_to_build[i] == 1:
            presup += grafo.edges[i].capacity
    for i in range(0, len(cities_to_build)):
        if cities_to_build[i] == 1:
            presup -= grafo.nodes[i].value
    return presup



# node1 = Node(0, 9)
# node2 = Node(1, 8)
# node3 = Node(2, 7)
# node4 = Node(3, 6)

# node5 = Node(4, 5)
# node6 = Node(5, 4)
# node7 = Node(6, 3)
# node8 = Node(7, 2)

# node9 = Node(8, 1)

# edge1 = Edge(node1, node2, 10)
# edge2 = Edge(node2, node3, 20)

# edge3 = Edge(node3, node4, 30)
# edge4 = Edge(node4, node5, 40)

# edge5 = Edge(node5, node6, 50)
# edge6 = Edge(node6, node7, 60)

# edge7 = Edge(node7, node8, 80)
# edge8 = Edge(node8, node9, 70)

# nodes = [node1, node2, node3, node4, node5, node6, node7, node8, node9]

# edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8]

# grafo = Graph(nodes, edges)

# array1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# array2 = [0, 0, 0, 0, 0, 0, 0, 0]

# print(tester_solution(grafo, array2, array1, 0))


