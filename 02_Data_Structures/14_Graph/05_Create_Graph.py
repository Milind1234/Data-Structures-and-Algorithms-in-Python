# =============================================================================
#                    📘 Create_Graph_In_Python_Notes.py
# =============================================================================
"""
In this chapter, we learn how to CREATE a graph in Python using:

    ✔ Dictionary  
    ✔ Adjacency List Representation  
    ✔ Custom Graph class  
    ✔ Method to add edges to vertices  

A graph in Python is most convenient to represent using a DICTIONARY:

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        ...
    }

The keys are **vertices** and the values are **lists of neighbor vertices**.

Below is the Python implementation explained in detail.
"""
# =============================================================================
#                          📌 GRAPH CLASS IMPLEMENTATION
# =============================================================================

class Graph:
    def __init__(self, graph_dict=None):
        """
        The constructor initializes the graph.

        graph_dict:
            - Should be a dictionary where:
                key   = vertex
                value = list of adjacent vertices
            - Example:
                { "A": ["B", "C"], "B": ["A"], ... }

        If graph_dict is NOT provided, we start with an empty dictionary.
        """
        if graph_dict is None:
            graph_dict = {}          # Create an empty graph dictionary
        self.graph_dict = graph_dict  # Store it inside the object

    def addEdge(self, vertex, edge):
        """
        This method adds an edge TO AN EXISTING vertex.

        Example:
            addEdge("C", "D")
            Meaning: Add D into adjacency list of C
                     So "C": ["A", "E"] becomes ["A", "E", "D"]

        NOTE:
            This function does NOT create a new vertex.
            The vertex MUST already exist in graph_dict.
        """
        self.graph_dict[vertex].append(edge)


# =============================================================================
#            📌 CUSTOM GRAPH WE WILL BUILD (BASED ON LECTURE DIAGRAM)
# =============================================================================
"""
Graph Diagram:

        A ----- B ----- D ----- F
        |       \       |       |
        |        \      |       |
        C -------- E ----       |
                   \------------

Adjacency representation:

    A → B, C
    B → A, D, E
    C → A, E
    D → B, E, F
    E → D, F
    F → D, E
"""

Dict = { 
    "a" : ["b", "c"],          # From A → B and C
    "b" : ["a", "d", "e"],     # From B → A, D, E
    "c" : ["a", "e"],          # From C → A and E
    "d" : ["b", "e", "f"],     # From D → B, E, F
    "e" : ["d", "f"],          # From E → D and F
    "f" : ["d", "e"]           # From F → D and E
}

# =============================================================================
#                      📌 CREATE GRAPH OBJECT FROM DICTIONARY
# =============================================================================

graph = Graph(Dict)

print("Before Edit:")
print(graph.graph_dict)   # Shows full adjacency list before modification


# =============================================================================
#               📌 NOW WE ADD A NEW EDGE USING addEdge() METHOD
# =============================================================================
"""
We add an edge:

    C → D

This means:
    - We insert "d" into list of neighbors under key "c"
    - Before: "c": ["a", "e"]
    - After:  "c": ["a", "e", "d"]

This demonstrates how we modify an existing graph.
"""
graph.addEdge("c", "d")

print()
print("After adding edge 'd' on vertex 'c':")
print(graph.graph_dict)


# =============================================================================
#                           📌 SUMMARY OF THIS SCRIPT
# =============================================================================
"""
✔ We created a GRAPH using Python Dictionary (Adjacency List)
✔ We defined Graph class with:
      - __init__()  → initializes graph
      - addEdge()   → adds an edge to an existing vertex

✔ We built a custom graph using your diagram
✔ We updated graph by adding a new edge (C → D)
✔ We printed before/after result to verify the modification

This is the foundation for upcoming chapters:
    → BFS (Breadth First Search)
    → DFS (Depth First Search)
    → Topological Sorting
    → Shortest Path Algorithms (Dijkstra, Bellman-Ford, BFS)
"""
# =============================================================================
#                               END OF NOTES
# =============================================================================
