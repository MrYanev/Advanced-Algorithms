from re import S
import re


class Vertex:
    def __init__(self, n):
        self.name = n

class Graph:
    vertices = {}
    edges = []  #Two dimentional array of the edges
    edge_indices = {}

    def add_vertex(self, vertex): #Function to add new vertices
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:  #Check if the vertex already exists 
            self.vertices[vertex.name] = vertex #If its not this line is adding it to the list
            for row in self.edges: #A for loop to add a new row of 0
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1)) #Appending 0s equal to the lenght of the list
            self.edge_indices[vertex.name] = len(self.edge_indices)  #Assigning indexes to the dictionary
            return True
        else:
            return False

    def add_edge(self, u, v, weight= 1): #Function to add new edges
        if u in self.vertices and v in self.vertices: #Check if the verices are in the dictionary 
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight #Adding the weigh in both u, v
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight #And adding the weight in v,u as the graph is symetrical
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end= '')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')



g = Graph()
a = Vertex('1')
g.add_vertex(a)
g.add_vertex(Vertex('2'))
for i in range(ord('1'), ord('7')):
    g.add_vertex(Vertex(chr(i)))

edges = ['12', '13', '21', '23', '31', '32', '34', '43']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()