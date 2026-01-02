# =============================================================================
#         📘 Create_Graph_Remove_Edge_Notes.py — REMOVE EDGE (ADJACENCY LIST)
# =============================================================================
"""
This note explains how to REMOVE EDGES from a graph implemented using
an adjacency-list (Python dictionary).

Covers:
    ✔ What "remove edge" means (visual)
    ✔ Implementation details and corrected code
    ✔ Edge cases and error handling (try/except)
    ✔ Example usage / demo
    ✔ Time & space complexity

This continues the Graph lectures (add_vertex, add_edge); we assume an
undirected graph (edges stored both ways).
"""

# =============================================================================
# 1) Concept: What is "remove edge"?
# =============================================================================
"""
Given an undirected graph:

    A ----- B
    |       |
   ( )     ( )

Adjacency lists before removal:
    A : ['B', 'C']
    B : ['A']
    C : ['A']

If we remove the edge A — B, adjacency lists become:
    A : ['C']
    B : []
    C : ['A']

So removing an edge between vertex1 and vertex2 means:
    - Remove vertex2 from vertex1's neighbor list
    - Remove vertex1 from vertex2's neighbor list
"""

# =============================================================================
# 2) Visual step-by-step
# =============================================================================
"""
Before:
    A : ['B', 'C']
    B : ['A']
    C : ['A']

Call:
    remove_edge('A', 'B')

After:
    A : ['C']
    B : []
    C : ['A']
"""

# =============================================================================
# 3) Graph class (add_vertex, add_edge, remove_edge, print_graph)
# =============================================================================

class Graph:
    def __init__(self):
        """
        Initialize an empty adjacency list dictionary.

        Time: O(1)
        Space: O(1)
        """
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        """
        Add a vertex with an empty neighbor list if it does not already exist.

        Returns True if added, False if already present.

        Time: O(1)
        Space: O(1) (per new vertex)
        """
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        """
        Print adjacency list in readable form.

        Time: O(V + E) to iterate and print everything
        Space: O(1) extra
        """
        print("\n📌 GRAPH STRUCTURE:")
        print("-" * 35)
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
        print("-" * 35)

    def add_edge(self, vertex1, vertex2):
        """
        Add an undirected edge between vertex1 and vertex2.

        Behavior:
            - Both vertices must exist; otherwise return False.
            - Appends vertex2 into vertex1 list and vertex1 into vertex2 list.

        Time: O(1) average for dict lookup + O(1) append
        Space: O(1) per added edge
        """
        # Correct membership check (both must exist)
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            # Avoid duplicate entries if desired (optional, uncomment to enforce)
            if vertex2 not in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].append(vertex2)
            if vertex1 not in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].append(vertex1)

            # # Simple append (matches original lecture behavior)
            # self.adjacency_list[vertex1].append(vertex2)
            # self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        """
        Remove an undirected edge between vertex1 and vertex2.

        Steps:
            1. Check both vertices exist in adjacency_list keys.
            2. Try to remove vertex2 from vertex1's neighbor list and vice versa.
               Use try/except to avoid ValueError when the neighbor is not present.
            3. Return True if the operation was executed (even if edge wasn't present).
               Return False if one or both vertices are missing.

        Why try/except?
            list.remove(x) raises ValueError if x is not in the list.
            In lecture we avoid showing a traceback to users, so we catch ValueError.

        Returns:
            True  → operation attempted (vertices existed)
            False → one or both vertices do not exist (no operation)

        Time Complexity:
            - Dictionary membership checks: O(1)
            - list.remove(x) is O(k) where k is degree(vertex) (search for the element)
            → Overall: O(k1 + k2) where k1 = deg(vertex1), k2 = deg(vertex2)

        Space Complexity:
            - O(1) extra (in-place removal)
        """
        # Correct membership check (both vertices must exist)
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                # Attempt to remove vertex2 from vertex1's neighbor list
                self.adjacency_list[vertex1].remove(vertex2)
            except ValueError:
                # vertex2 was not in vertex1's neighbor list — ignore
                pass

            try:
                # Attempt to remove vertex1 from vertex2's neighbor list
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                # vertex1 was not in vertex2's neighbor list — ignore
                pass

            return True
        
        # One or both vertices do not exist in the graph
        return False


# =============================================================================
# 4) Demo / Example usage (exactly follows lecture steps)
# =============================================================================

if __name__ == "__main__":
    # Create the graph and add vertices
    custom_graph = Graph()
    custom_graph.add_vertex("A")
    custom_graph.add_vertex("B")
    custom_graph.add_vertex("C")
    custom_graph.add_vertex("D")   # D has no edges initially

    # Add edges (undirected)
    custom_graph.add_edge("A", "B")
    custom_graph.add_edge("A", "C")
    custom_graph.add_edge("B", "C")

    print("Before removing edge:")
    custom_graph.print_graph()

    # Remove an existing edge A - C
    custom_graph.remove_edge("A", "C")
    print("After removing edge between A & C:")
    custom_graph.print_graph()

    # Attempt to remove a non-existent edge (A - D): no traceback thanks to try/except
    removed = custom_graph.remove_edge("A", "D")
    print("Tried removing edge A - D (non-existent). Operation returned:", removed)
    custom_graph.print_graph()

    # Attempt to remove edge with a missing vertex (X - Y): returns False
    removed_missing = custom_graph.remove_edge("X", "Y")
    print("Tried removing edge X - Y (vertices missing). Operation returned:", removed_missing)

# =============================================================================
# 5) Complexity summary
# =============================================================================
"""
| Method         | Time Complexity     | Space Complexity | Notes
| -------------- | ------------------- | ---------------- | -----------------------------------------------
| __init__()     | O(1)                | O(1)             | Create empty dict
| add_vertex()   | O(1)                | O(1) per vertex  | dict insertion
| add_edge()     | O(1) average        | O(1) per edge    | dict lookups + append (lists). Duplicate checks cost O(k)
| remove_edge()  | O(k1 + k2)          | O(1)             | k1=deg(v1), k2=deg(v2) (cost of list.remove searches)
| print_graph()  | O(V + E)            | O(1)             | iterate all vertices & neighbors

Notes:
- If you expect many membership checks (to avoid duplicates) consider using sets
  for neighbor storage (neighbors as set ⇒ O(1) membership & removal), but sets
  do not preserve insertion order and have slightly higher memory overhead.
- remove_edge returns False only when one or both vertices do not exist.
  It returns True when the operation was attempted (even if the specific edge
  wasn't present). This mirrors the lecture behavior and avoids tracebacks.
"""
# =============================================================================
#                                  END
# =============================================================================
