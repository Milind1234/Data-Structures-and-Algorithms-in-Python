
# =============================================================================
#                          📘 Graph_Types_Notes.py
# =============================================================================

"""
===============================================================================
                             GRAPH TYPES (FULL NOTES)
              With explanations + multiple ASCII visualizations
===============================================================================

A graph can be broadly categorized based on:

1️⃣ Direction:      Directed / Undirected  
2️⃣ Weight:         Weighted / Unweighted  
3️⃣ Weight sign:    Positive / Negative  

This gives us SIX major graph categories used in interviews.

===============================================================================
                           OVERALL GRAPH TYPE TREE
===============================================================================

                                 GRAPH
                               /      \
                     Directed           Undirected
                   /         \        /           \
           Weighted      Unweighted  Weighted    Unweighted
           /     \                     /    \
      Positive  Negative        Positive   Negative

===============================================================================
                   1️⃣ UNWEIGHTED – UNDIRECTED GRAPH
===============================================================================

Definition:
    • No weights (all edges equal cost)
    • No directions (bidirectional edges)

ASCII Visualization:

            V1 ------- V3
            | \         \
            |  \         \
            V2 -- V4 ---- V5

Meaning:
    V1 ↔ V2  
    V2 ↔ V4  
    V4 ↔ V5  
    V3 ↔ V5  
    (all edges usable both ways)

Use cases:
    • Friendship network (A ↔ B)
    • Road where travel is allowed both ways

-------------------------------------------------------------------------------

Example 2 (another visualization):

            (A)
            / \
          (B)-(C)
            \  |
             (D)

All are undirected and equal cost.


===============================================================================
                   2️⃣ UNWEIGHTED – DIRECTED GRAPH
===============================================================================

Definition:
    • No weights
    • Edges show direction

ASCII Visualization:

       V1  →  V3  →  V5
        ↓        ↗
        V2  →  V4

Meaning:
    V1 → V2 allowed, V2 → V1 NOT allowed  
    V3 → V5 allowed, V5 → V3 NOT allowed

Use cases:
    • Instagram following (A → B only)
    • One-way traffic roads

-------------------------------------------------------------------------------

Example 2 (more complex):

       A → B → D
       ↑      ↓
       C ←----


===============================================================================
           3️⃣ POSITIVE – WEIGHTED – UNDIRECTED GRAPH
===============================================================================

Definition:
    • All weights are positive  
    • All edges bidirectional  

ASCII Visualization (matches your slide):

          (3)
     V1 -------- V3
     | \         \
   (4) (5)        (2)
     |     \       \
     V2 ---- V4 ---- V5
          (3)

Meaning:
    • Cost V1 → V2 = 4  
    • Cost V3 → V5 = 2  
    • Travel both ways  

Use cases:
    • Road distances  
    • Network latency (undirected links)


===============================================================================
               4️⃣ POSITIVE – WEIGHTED – DIRECTED GRAPH
===============================================================================

Definition:
    • Positive weights  
    • Direction matters  

ASCII Visualization:

     V1 --3--> V3 --2--> V5
      ↑          \
      |5          \
      V4 <--3-- V2

Meaning:
    • V1 → V3 cost 3  
    • V3 → V5 cost 2  
    • V5 → V3 NOT ALLOWED  
    • V2 → V4 cost 3  

Use cases:
    • Travel routes with one-way edges
    • Data flow in systems
    • Task dependency graph


===============================================================================
              5️⃣ NEGATIVE – WEIGHTED – UNDIRECTED GRAPH
===============================================================================

Definition:
    • At least one edge has negative weight  
    • Bidirectional edges  

ASCII Visualization:

           -3
     V1 -------- V3
     | \         \
   (4) (-5)       (2)
     |     \       \
     V2 ---- V4 ---- V5
          (3)

Meaning:
    • V1 ↔ V4 = -5  
    • V1 ↔ V3 = -3  
    • V3 ↔ V5 = 2  

Why negative?
    • Profit (gain) edges  
    • Reduction cost paths  

Used in:
    • Bellman–Ford shortest path algorithm


===============================================================================
                6️⃣ NEGATIVE – WEIGHTED – DIRECTED GRAPH
===============================================================================

Definition:
    • At least one negative weight  
    • Directional edges  

ASCII Visualization:

     V1 --(-3)--> V3 --2--> V5
      ↑             \
     -5              \
      V4 <--3-- V2 ----

Meaning:
    • V1 → V3 = -3  
    • V1 → V4 = -5  
    • V4 → V2 = 3  
    • V5 → V3 NOT allowed  

Danger:
    • May contain *negative cycles*
    • Dijkstra CANNOT be used
    • Bellman-Ford is required

-------------------------------------------------------------------------------

Example 2:

     A → B (-2)
     ↑     ↓
     D ← C (-5)


===============================================================================
                       QUICK SUMMARY TABLE (INTERVIEW GOLD)
===============================================================================

Type                                | Weight | Direction | Notes
-------------------------------------------------------------------------------------------
Unweighted – Undirected             |   ✖️    |   ↔       | Simple, BFS works
Unweighted – Directed               |   ✖️    |   →       | In-deg/out-deg important
Positive Weighted – Undirected      |  +     |   ↔       | Dijkstra works
Positive Weighted – Directed        |  +     |   →       | Dijkstra works
Negative Weighted – Undirected      |  -     |   ↔       | Use Bellman-Ford
Negative Weighted – Directed        |  -     |   →       | Use Bellman-Ford, watch cycles

===============================================================================
END OF NOTES
===============================================================================
"""
