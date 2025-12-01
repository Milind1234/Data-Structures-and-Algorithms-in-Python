# =============================================================================
#        📘 Create_Graph_Remove_Vertex_Notes.py — REMOVE VERTEX FROM GRAPH
# =============================================================================
r"""
This note explains how to REMOVE A VERTEX from a graph that uses:

        ✔ Adjacency List Representation (dictionary)
        ✔ Undirected graph structure
        ✔ remove_vertex() method logic
        ✔ Edge cleanup (very important)
        ✔ Visual diagrams
        ✔ Time & Space Complexity

This is the continuation of previous lectures:
    → Add Vertex
    → Add Edge
    → Remove Edge
"""

# =============================================================================
# 📌 1. What does "remove a vertex" mean?
# =============================================================================
r"""
If our graph looks like this:

        A ----- C
         \     /
           \  /
             D
             |
             B

Adjacency List:
    A : ['B', 'C', 'D']
    B : ['A', 'D']
    C : ['A', 'D']
    D : ['A', 'B', 'C']

If we remove vertex D, the final graph must remove:
    ✔ The vertex D itself
    ✔ Every edge pointing to D in A, B, C

After removal:
    A : ['B', 'C']
    B : ['A']
    C : ['A']
"""

# =============================================================================
# 📌 2. Visual Flow (step-by-step deleting D)
# =============================================================================
"""
Edges connected to D:  A, B, C

1. Remove D from A's list:
       A : ['B', 'C']

2. Remove D from B's list:
       B : ['A']

3. Remove D from C's list:
       C : ['A']

4. Delete vertex D entirely from dictionary.

This process ensures the graph remains consistent.
"""

# =============================================================================
# 📌 3. The Graph Class With remove_vertex()
# =============================================================================

class Graph:
    def __init__(self):
        """
        Initialize empty adjacency list.
        """
        self.adjacency_list = {}
    
    # -------------------------------------------------------------------------
    def add_vertex(self, vertex):
        """
        Adds a new vertex with no edges.
        """
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    # -------------------------------------------------------------------------
    def print_graph(self):
        """
        Print adjacency list in readable form.
        """
        print("\n📌 GRAPH STRUCTURE:")
        print("-" * 35)
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
        print("-" * 35)

    # -------------------------------------------------------------------------
    def add_edge(self, vertex1, vertex2):
        """
        Adds an undirected edge (vertex1 <-> vertex2)
        """
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    # -------------------------------------------------------------------------
    def remove_Vertex(self, vertex):
        """
        Removes a vertex AND all its connected edges.

        Steps:

            1. Confirm vertex exists.
            2. Loop through all neighbors of the vertex.
            3. Remove 'vertex' from each neighbor's adjacency list.
            4. Delete the vertex itself from adjacency_list.
            5. Return True if successful.

        Example:
            Before removing D:
                D : ['A', 'C']

            Remove D:
                - Remove D from A
                - Remove D from C
                - Delete D entirely

        Time Complexity:
            ----------------------------------------
            O(V + E_vertex)
            - Looping neighbors: O(E_vertex)
            - Removing from neighbor lists: O(V)
            ----------------------------------------
        Space Complexity:
            O(1)
        """
        if vertex in self.adjacency_list.keys():

            # Step 1: Delete 'vertex' from all its neighbor lists
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)

            # Step 2: Delete the vertex from the graph
            del self.adjacency_list[vertex]
            return True
        
        return False


# =============================================================================
# 📌 4. DEMO — Removing Vertex from Graph
# =============================================================================

custom_graph = Graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")

# Adding edges
custom_graph.add_edge("A", "B")
custom_graph.add_edge("A", "C")
custom_graph.add_edge("A", "D")
custom_graph.add_edge("B", "C")
custom_graph.add_edge("C", "D")

print("Before removing vertex D")
custom_graph.print_graph()

# Remove vertex D
custom_graph.remove_Vertex("D")
print("After Removing Vertex D")
custom_graph.print_graph()

"""
Expected Output:

Before removing:
    A : ['B', 'C', 'D']
    B : ['A', 'C']
    C : ['A', 'B', 'D']
    D : ['A', 'C']

After removing D:
    A : ['B', 'C']
    B : ['A', 'C']
    C : ['A', 'B']
"""

# =============================================================================
# 📌 5. Complexity Summary
# =============================================================================
"""
| Method            | Time Complexity     | Space Complexity | Notes                                   |
| ----------------- | ------------------- | ---------------- | ---------------------------------------- |
| add_vertex()      | O(1)                | O(1)             | Add key with empty list                  |
| add_edge()        | O(1)                | O(1)             | Append to lists                          |
| remove_Vertex()   | O(V + E_vertex)     | O(1)             | Remove from neighbors + delete key       |
| print_graph()     | O(V + E)            | O(1)             | Iterate over all vertices & edges        |

Where:
    V = number of vertices
    E = total number of edges
    E_vertex = number of neighbors of the vertex being removed
"""

# =============================================================================
#                                    END
# =============================================================================
