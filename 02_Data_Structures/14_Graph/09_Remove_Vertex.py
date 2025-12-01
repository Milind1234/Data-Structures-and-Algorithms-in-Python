class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self , vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex , ":" , self.adjacency_list[vertex])

    def add_edge(self , vertex1 , vertex2):
        if (vertex1 and vertex2) in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_Vertex(self , vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False


custom_graph = Graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_edge("A","B")
custom_graph.add_edge("A","C")
custom_graph.add_edge("A","D")
custom_graph.add_edge("C","D")
custom_graph.print_graph()
custom_graph.remove_Vertex("D")
print("After Remove..")
custom_graph.print_graph()