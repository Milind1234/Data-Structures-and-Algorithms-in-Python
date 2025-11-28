class Graph:
    def __init__(self , graph_dict = None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict
    
    def addEdge(self , vertex , edge):
        self.graph_dict[vertex].append(edge)


Dict = { 
        "a" : ["b" , "c"],
        "b" : ["a" , "d" , "e"],
        "c" : ["a" , "e"],
        "d" : ["b" , "e" , "f"],
        "e" : ["d" , "f"],
        "f" : ["d" , "e"]
        }

graph = Graph(Dict)
print("Before Edit")
print(graph.graph_dict)
graph.addEdge("c", "d")
print()
print("After adding edge 'd' on vertex 'c' ")
print(graph.graph_dict)