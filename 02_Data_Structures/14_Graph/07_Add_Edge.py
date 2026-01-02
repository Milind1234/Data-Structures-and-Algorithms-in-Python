# =============================================================================
#         📘 Create_Graph_Add_Edge_Notes.py — GRAPH USING ADJACENCY LIST
# =============================================================================
"""
This note explains how to ADD EDGES to a graph using Python:

        ✔ Adjacency List Representation
        ✔ Dictionary-based Graph class
        ✔ add_edge() method
        ✔ print_graph() helper
        ✔ Time & Space Complexity

This lectur'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number 

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]

    start_time=time.time()

    ##create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)

    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
e continues from the previous "Add Vertex" lecture.
"""

# =============================================================================
# 📌 1. What does add_edge() do?
# =============================================================================
"""
If we have two vertices:

        A : []
        B : []

And we want to connect them, we add edges BOTH WAYS (because graph is undirected):

        A : [B]
        B : [A]

This creates a link between the two vertices.

The adjacency list dictionary becomes:

{
    "A": ["B"],
    "B": ["A"]
}

This means:
    ✔ A is connected to B
    ✔ B is connected to A

This is the fundamental idea behind adjacency list–based graph representation.
"""

# =============================================================================
# 📌 2. Visual Representation
# =============================================================================
"""
Before adding edge:

    A    B
    |    |
   []   []

After add_edge("A", "B"):

    A ------ B
    |        |
   [B]      [A]

Adjacency list:

    A : [B]
    B : [A]
"""

# =============================================================================
# 📌 3. Python Class with add_edge() (UNDIRECTED)
# =============================================================================

class Graph:
    def __init__(self):
        """
        Initializes an empty adjacency list.
        """
        self.adjacency_list = {}
    
    # ---------------------------------------------------------------------

    def add_vertex(self, vertex):
        """
        Adds a new vertex if it does not exist.

        Example:
            add_vertex("A") → {"A": []}

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    # ---------------------------------------------------------------------

    def print_graph(self):
        """
        Prints adjacency list in readable form.

        Format:
            A : ['B', 'C']
            B : ['A']

        Time Complexity: O(V + E)
        Space Complexity: O(1)
        """
        print("\n📌 GRAPH STRUCTURE:")
        print("-" * 35)
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
        print("-" * 35)

    # ---------------------------------------------------------------------

    def add_edge(self, vertex1, vertex2):
        """
        Adds an UNDIRECTED edge between vertex1 and vertex2.

        Steps:
            1. Check if both vertices exist in the graph.
            2. Append vertex2 into vertex1's list.
            3. Append vertex1 into vertex2's list.
            4. Return True if successfully added.

        Example:
            add_edge("A", "B")

            Before:
                A : []
                B : []

            After:
                A : ['B']
                B : ['A']

        NOTE:
            This graph is UNDIRECTED → edges go BOTH ways.

        Edge Case:
            If either vertex is missing → return False

        Time Complexity:
            ✔ O(1) average (append operations)
            ✔ But membership check inside dict is O(1)

        Space Complexity:
            ✔ O(1) per edge
        """

        
        # Edge Case:
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            
            # Add edge to vertex1's list
            self.adjacency_list[vertex1].append(vertex2)

            # Add edge to vertex2's list (undirected graph)
            self.adjacency_list[vertex2].append(vertex1)

            return True
        
        return False


# =============================================================================
# 📌 4. DEMO / HOW THE METHOD WORKS
# =============================================================================

custom_graph = Graph()

# Step 1 — Add vertices
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")

# Step 2 — Add edges
custom_graph.add_edge("A", "B")   # A-B connected both ways
custom_graph.add_edge("A", "C")   # A-C connected both ways

# Step 3 — Print graph structure
custom_graph.print_graph()

"""
EXPECTED OUTPUT:

📌 GRAPH STRUCTURE:
-----------------------------------
A : ['B', 'C']
B : ['A']
C : ['A']
-----------------------------------

Which means:
    ✔ A connected to B and C
    ✔ B connected to A
    ✔ C connected to A
"""

# =============================================================================
# 📌 5. Time & Space Complexity Summary
# =============================================================================
"""
| Method          | Time Complexity | Space Complexity | Explanation                             |
| --------------- | --------------- | ---------------- | --------------------------------------- |
| `__init__()`    | O(1)            | O(1)             | Creates empty dictionary                |
| `add_vertex()`  | O(1)            | O(1)             | Inserts a new key                       |
| `add_edge()`    | O(1)            | O(1)             | Appends in adjacency lists              |
| `print_graph()` | O(V + E)        | O(1)             | Visits every vertex & edge              |

V = number of vertices  
E = number of edges
"""

# =============================================================================
#                                  END
# =============================================================================
