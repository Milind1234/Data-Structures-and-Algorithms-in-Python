# =============================================================================
#         📘 Create_Graph_Add_Vertex_Notes.py — GRAPH USING ADJACENCY LIST
# =============================================================================
"""
This note explains how to CREATE A GRAPH in Python using:

        ✔ Adjacency List Representation
        ✔ Dictionary Implementation
        ✔ Graph class
        ✔ add_vertex() method
        ✔ print_graph() helper method

This lecture is part of course remastering, focusing on clearer explanations.

───────────────────────────────────────────────────────────────────────────────
📌 1. What is an Adjacency List?
───────────────────────────────────────────────────────────────────────────────
We represent a graph using a dictionary:

        adjacency_list = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            ...
        }

✔ Keys      → Vertices  
✔ Values    → List of neighbors (edges)

If a vertex has no edges yet, its list remains empty:

Example:
    A : []
(meaning A exists but has NO connections yet)

───────────────────────────────────────────────────────────────────────────────
📌 2. Visual Representation of Adjacency List
───────────────────────────────────────────────────────────────────────────────

Graph: (only vertices, no edges yet)

        A    B    C    D
        |    |    |    |
       []   []   []   []

As a dictionary:

        {
            "A": [],
            "B": [],
            "C": [],
            "D": []
        }

───────────────────────────────────────────────────────────────────────────────
📌 3. Python Class Implementation
───────────────────────────────────────────────────────────────────────────────
We create:

    → Graph class
    → adjacency_list dictionary
    → add_vertex() method
    → print_graph() method
"""

# =============================================================================
#                              📌 GRAPH CLASS
# =============================================================================

class Graph:
    def __init__(self):
        """
        Constructor initializes the adjacency list.

        adjacency_list:
            A dictionary where:
                key   = vertex
                value = list of neighbors (edges)

        When graph is newly created → it is EMPTY:
            {}
        ────────────────────────────────────────────────────────
        ⏳ Time Complexity: O(1)
            Reason: Just initializes an empty dictionary.

        💾 Space Complexity: O(1)
            No vertices or edges stored yet.
        ────────────────────────────────────────────────────────
        
        """
        self.adjacency_list = {}

    # -------------------------------------------------------------------------

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Steps:
            1. Check if vertex already exists
            2. If not → create a key with empty list
            3. Return True if added, False if duplicate

        Example:
            add_vertex("A")

            Before:
                {}
            After:
                {"A": []}

        Visualization:

            A : []

        ────────────────────────────────────────────────────────
        ⏳ Time Complexity: O(1)
            - Checking existence in dictionary is O(1).
            - Adding a new key is also O(1).

        💾 Space Complexity: O(1)
            - Each new vertex stores an empty list.
        ────────────────────────────────────────────────────────

        """
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []   # Create empty edge list
            return True
        return False

    # -------------------------------------------------------------------------

    def print_graph(self):
        """
        Prints the graph in readable form.

        Format:
            A : ['B', 'C']
            B : ['A']
            C : []

        Useful for debugging and visualizing structure.
        ────────────────────────────────────────────────────────
        ⏳ Time Complexity: O(V + E)
            - You iterate over every vertex → O(V)
            - Printing the neighbor list contributes → O(E)

        💾 Space Complexity: O(1)
            - Output only. No extra memory stored.
        ────────────────────────────────────────────────────────
        """
        print("\n📌 GRAPH STRUCTURE:")
        print("-" * 35)
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
        print("-" * 35)


# =============================================================================
#                    📌 USING THE GRAPH (DEMO)
# =============================================================================
"""
We now create a graph object and add a single vertex "A".
"""

custom_graph = Graph()

print("Adding vertex 'A'...")
custom_graph.add_vertex("A")

# Print graph state to verify
custom_graph.print_graph()

"""
Expected Output:

📌 GRAPH STRUCTURE:
-----------------------------------
A : []
-----------------------------------

This means:
    → Vertex "A" exists
    → It currently has NO edges
"""

# =============================================================================
#                                  END
# =============================================================================

"""

| Method          | Time Complexity | Space Complexity | Explanation                             |
| --------------- | --------------- | ---------------- | --------------------------------------- |
| `__init__()`    | **O(1)**        | **O(1)**         | Only creates an empty dictionary        |
| `add_vertex()`  | **O(1)**        | **O(1)**         | Dictionary insertion + membership check |
| `print_graph()` | **O(V + E)**    | **O(1)**         | Prints all vertices and adjacency lists |

"""