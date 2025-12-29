# =============================================================================
#                        📘 Graph_Introduction_Notes.py
# =============================================================================

"""
===============================================================================
                                1️⃣ WHAT IS A GRAPH?
===============================================================================

A *Graph* is a **non-linear data structure** consisting of:

    • Vertices  → also called Nodes
    • Edges     → connections/links between nodes

Formal definition:
    A Graph = (V, E)
        V = finite set of vertices
        E = finite set of edges connecting pairs of vertices

Graphs allow us to represent complex relationships between data items.

===============================================================================
                       2️⃣ GRAPH VISUAL (ASCII REPRESENTATION)
===============================================================================

Example Graph:

                    A
                  / | \
                 /  |  \
                B   |   D
               /    |    \
              E --- K ---- J

    - Circles represent NODES: A, B, D, K, J, E
    - Lines represent EDGES (connections)

===============================================================================
                           3️⃣ WHY DO WE NEED GRAPHS?
===============================================================================

Graphs are used to represent **networks**, such as:

    ✔ Transportation networks (roads, flights, railways)
    ✔ Social networks (Facebook, LinkedIn)
    ✔ Communication networks (telephone lines, internet)
    ✔ Electrical circuits
    ✔ Map systems (Google Maps pathfinding)

Graphs help solve problems like:
    • Shortest path between cities
    • Detecting cycles
    • Network flow
    • Connectivity checks
    • Recommendations in social media

===============================================================================
               4️⃣ REAL-LIFE EXAMPLE — FLIGHT CONNECTION GRAPH
===============================================================================

Imagine cities connected with flight routes:

           London
        /     |      \
       /      |       \
    Paris   Berlin    Kyiv
       \       \        \
       Rome    Moscow    Baku

Possible routes to reach **Baku from London**:
    1. London → Moscow → Baku
    2. London → Kyiv   → Baku
    3. London → Istanbul → Baku

Notice:  
    These paths form **cycles** and **multiple routes**,  
    which cannot be represented using a tree (because tree has NO cycles).

Therefore, the correct structure is **Graph**.

===============================================================================
                          5️⃣ WHY NOT USE A TREE?
===============================================================================

Trees have:
    ✔ Nodes  
    ✔ Edges  
    ❌ BUT NO cycles  
    ❌ Only one path between two nodes  

Real-world networks often contain:
    ✔ multiple paths  
    ✔ cycles  
    ✔ complex relationships  

→ That’s why **Tree ≠ suitable**  
→ **Graph = perfect** for these situations

===============================================================================
                                SUMMARY
===============================================================================

Graphs:
    • consist of vertices and edges
    • model real-world relationships
    • support multiple paths + cycles
    • are used in routing, networks, and shortest path problems

Next topics (as per lecture):
    ✓ Graph Terminology
    ✓ Types of Graphs
    ✓ Graph Representation in Code
    ✓ BFS & DFS Traversals
    ✓ Topological Sorting
    ✓ Shortest Path Algorithms (BFS, Dijkstra, Bellman-Ford)
    ✓ Minimum Spanning Tree (Prim & Kruskal)

===============================================================================
"""
