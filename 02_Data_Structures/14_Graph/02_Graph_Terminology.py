# =============================================================================
#                          📘 Graph_Terminology_Notes.py
# =============================================================================

"""
===============================================================================
                              GRAPH TERMINOLOGY
            (With simple explanations + ASCII diagrams + examples)
===============================================================================


1️⃣ VERTICES (VERTEX)
----------------------
Vertices are the **nodes** of a graph.

Example:

        (V1) —— (V3)
         |
        (V2)

Vertices here → V1, V2, V3

They represent entities such as:
    - cities
    - people
    - web pages
    - routers
    - states in a machine


2️⃣ EDGE
--------
An **edge** is the line that connects two vertices.

Example:

        V1 —— V3
        |
        V2

Edges present:
    • V1 — V2
    • V1 — V3

Edges represent:
    - flight connections
    - friendships
    - communication links


3️⃣ UNWEIGHTED GRAPH
---------------------
A graph where **no edge has a weight** (cost/time/distance).

Example:

        V1 —— V3
        |      \
        V2 —— V4 —— V5

No weights are shown → every edge has equal cost.


4️⃣ WEIGHTED GRAPH
-------------------
A graph where each edge has an associated **weight**.

Example:

        V1 ——(10)—— V3
         | \
       (8) (12)
         |     \
        V2 ——(5)— V4 ——(7)— V5

Meaning:
    • V1 → V2 cost = 8
    • V1 → V4 cost = 12
    • V3 → V5 cost = 7

Weights represent:
    - distance between cities
    - time
    - network bandwidth
    - money cost


5️⃣ UNDIRECTED GRAPH
----------------------
A graph where edges **do NOT have a direction**.
You can move both ways.

Example:

        V1 —— V3
        |      \
        V2 —— V4 —— V5

You can travel:
    V1 ↔ V3
    V3 ↔ V5
    V1 ↔ V2

Used in:
    • friendships (A ↔ B)
    • undirected roads


6️⃣ DIRECTED GRAPH (DIGRAPH)
-----------------------------
A graph where every edge has a **direction**.

Example:

        V1 → V3 → V5
         ↓      ↑
         V2 → V4

Meaning:
    • V1 → V2 allowed
    • V2 → V1 NOT allowed
    • V3 → V5 allowed
    • V5 → V3 NOT allowed

Used in:
    • one-way roads
    • Instagram following
    • task dependencies


7️⃣ CYCLIC GRAPH
----------------
A graph that contains **at least one loop** (cycle).

A cycle means:
    start at a vertex → follow edges → return to the same vertex through a different path.

Example cycle:

        V1
       /  \
      V2 — V4

Cycle:
    V1 → V2 → V4 → V1

Another cycle example:

        V1 → V3 → V5 → V4 → V1


8️⃣ ACYCLIC GRAPH
-----------------
A graph with **NO cycles**.

Example:

        V1 → V2
        |     \
        ↓      ↓
        V3 → V4 → V5

Here, there is **no way** to start from a vertex and come back via a different path.

Used in:
    • dependencies
    • course prerequisite order


9️⃣ TREE
---------
A **Tree = Directed Acyclic Graph (DAG) with special structure**

Properties:
    • It is directed
    • It has **no cycles**
    • There is exactly **one path** between any two nodes

Example Tree:

          V1
         /  \
       V2    V3
              \
               V5

This is a DAG **and** a tree.

Tree real-life use cases:
    • folder structure
    • class inheritance
    • organizational hierarchy


===============================================================================
### QUICK SUMMARY TABLE
===============================================================================

Term                Meaning
-------------------------------------------------------------------------------
Vertex              A node in a graph
Edge                A connection between two vertices
Unweighted Graph    Edges have no weights
Weighted Graph      Edges have weights (cost/time)
Undirected Graph    Edges have no direction (A ↔ B)
Directed Graph      Edges have direction (A → B)
Cyclic Graph        Contains at least one cycle
Acyclic Graph       Contains no cycles
Tree                Directed acyclic graph with hierarchical structure
===============================================================================

"""
