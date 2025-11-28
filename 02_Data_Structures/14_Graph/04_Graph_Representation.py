# =============================================================================
#                       📘 Graph_Representation_Notes.py
# =============================================================================

"""
===============================================================================
                                GRAPH REPRESENTATION
===============================================================================

There are 3 main ways to represent a graph in code:

    1️⃣ Adjacency Matrix  
    2️⃣ Adjacency List  
    3️⃣ Dictionary of Lists (Pythonic adjacency list)

Below we explain each in detail with diagrams and examples.

===============================================================================
                       1️⃣ ADJACENCY MATRIX (2D ARRAY)
===============================================================================

Definition:
    • A **square matrix** (N x N) where N = number of vertices.
    • Each cell matrix[i][j] = 1 → edge exists.
    • matrix[i][j] = 0 → no edge.
    • Works for directed, undirected, weighted & unweighted graphs.

Example Graph (Undirected, Unweighted):

               A ----- B
              / \       \
             C --- D ---- E

Edges:
    A ↔ B
    A ↔ C
    A ↔ D
    B ↔ E
    C ↔ D
    D ↔ E

Assign vertex indexes:
    A=0, B=1, C=2, D=3, E=4

ASCII adjacency matrix:

          A B C D E
        -------------
    A |  0 1 1 1 0
    B |  1 0 0 0 1
    C |  1 0 0 1 0
    D |  1 0 1 0 1
    E |  0 1 0 1 0

Visualization (matrix view):

            0 1 1 1 0
            1 0 0 0 1
            1 0 0 1 0
            1 0 1 0 1
            0 1 0 1 0

Interpretation:
    matrix[A][B] = 1 → A is connected to B  
    matrix[D][E] = 1 → D is connected to E  
    matrix[C][C] = 0 → no self-loop  

Advantages:
    ✔ Easy to understand  
    ✔ Fast edge lookup: O(1)  
    ✔ Best for dense graphs (many edges)

Disadvantages:
    ✖ Uses O(N²) space  
    ✖ Inefficient for sparse graphs (few edges)

===============================================================================
                       2️⃣ ADJACENCY LIST (ARRAY + LINKED LIST)
===============================================================================

Definition:
    • An array of size N (one entry per vertex)
    • Each vertex stores a *linked list* of neighbors.
    • Efficient for sparse graphs.

Graph Example (same as above):

               A ----- B
              / \       \
             C --- D ---- E

Adjacency List (conceptual linked-list view):

    A → B → C → D
    B → A → E
    C → A → D
    D → A → C → E
    E → B → D

ASCII Visual:

    A : B → C → D
    B : A → E
    C : A → D
    D : A → C → E
    E : B → D

Advantages:
    ✔ Memory efficient for sparse graphs  
    ✔ Easy to add/remove edges  
    ✔ Perfect for BFS/DFS  

Disadvantages:
    ✖ Checking if edge exists is O(k) (k = neighbors of a vertex)  
    ✖ Harder to implement weighted matrix-like operations  

===============================================================================
                   3️⃣ PYTHON DICTIONARY ADJACENCY LIST
===============================================================================

Python uses **dictionary of lists** to store adjacency lists easily.

Same graph:

    {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E'],
        'C': ['A', 'D'],
        'D': ['A', 'C', 'E'],
        'E': ['B', 'D']
    }

ASCII Visual:

    A → [B, C, D]
    B → [A, E]
    C → [A, D]
    D → [A, C, E]
    E → [B, D]

Why Python dict is preferred?
    ✔ Easy to code  
    ✔ Dynamic (no fixed matrix size)  
    ✔ Natural representation of real-world graphs  
    ✔ BFS/DFS friendly  
    ✔ Great for sparse graphs  

===============================================================================
                     COMPARISON: MATRIX vs LIST
===============================================================================

1️⃣ When to use ADJACENCY MATRIX:
--------------------------------
✔ Graph is **dense** (many edges)  
✔ Need to check edges very fast (O(1))  
✔ Useful for algorithms like Floyd-Warshall  

Example:
    A complete graph with 10,000 nodes → matrix is ideal.

2️⃣ When to use ADJACENCY LIST:
-------------------------------
✔ Graph is **sparse** (few edges)  
✔ Need quick traversal (BFS/DFS)  
✔ Memory efficiency is important  

Example:
    Social network where each person has only few connections.

-------------------------------------------------------------------------------

ASCII Comparison:

Matrix Example (N = 5):
    Requires 5×5 = 25 cells  

List Example:
    Total neighbors = number of edges × 2 (undirected)

If edges = 6 → only 12 entries stored.

===============================================================================
            STEP-BY-STEP DEMO: BUILDING MATRIX & LIST FOR A GRAPH
===============================================================================

Graph:

               A ----- B
              / \       \
             C --- D ---- E

Step 1 → Create mapping:
    A=0, B=1, C=2, D=3, E=4

Step 2 → Start matrix of 5×5 with all zeros:
    00000
    00000
    00000
    00000
    00000

Step 3 → Insert edges:

A-B → (0,1) & (1,0)
A-C → (0,2) & (2,0)
A-D → (0,3) & (3,0)
B-E → (1,4) & (4,1)
C-D → (2,3) & (3,2)
D-E → (3,4) & (4,3)

Final Matrix:
    0 1 1 1 0
    1 0 0 0 1
    1 0 0 1 0
    1 0 1 0 1
    0 1 0 1 0

Step 4 → Build adjacency list:

    A → B, C, D
    B → A, E
    C → A, D
    D → A, C, E
    E → B, D

Step 5 → Represent using Python dict:

    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E'],
        'C': ['A', 'D'],
        'D': ['A', 'C', 'E'],
        'E': ['B', 'D']
    }

===============================================================================
END OF GRAPH REPRESENTATION NOTES
===============================================================================
"""
