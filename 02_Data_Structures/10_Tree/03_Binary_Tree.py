"""
📘 Topic: Binary Tree — Concept, Need & Types

------------------------------------------------------------
Purpose:
---------
To understand the concept of **Binary Tree**, its types, and how to
represent and implement it using **Linked List** and **Python List**.

In the previous notes, we created a General Tree (n-ary tree),
where each node could have unlimited children.

Now we move to the **Binary Tree**, where each node can have **at most two children**:
➡️ Left Child
➡️ Right Child
------------------------------------------------------------

📖 Definition:
---------------
A **Binary Tree** is a data structure in which each node has at most two children.
That means:
✅ A node can have 0, 1, or 2 children.
❌ A node cannot have more than two children.

Each node consists of:
- **Data** (the value stored in the node)
- **Left Child Pointer**
- **Right Child Pointer**

Example Diagram:
----------------
        N1
       /  \
     N2    N3
    / \     \
   N4   N5   N6
  / \
 N7  N8

------------------------------------------------------------
Why Binary Trees?
-----------------
1️⃣ Foundation for advanced trees like:
    - Binary Search Tree (BST)
    - AVL Tree
    - Red-Black Tree
    - Heap Tree
    - Syntax Tree

2️⃣ Efficient for certain problems:
    - Huffman Coding (Data Compression)
    - Heap Priority Queue Problems
    - Expression Parsing in Compilers

Hence, Binary Trees are **prerequisite** for mastering advanced tree algorithms.
------------------------------------------------------------

📗 Binary Tree Family:
----------------------
All these are *derived from the basic Binary Tree*:
    → BST (Binary Search Tree)
    → AVL Tree
    → Red-Black Tree
    → Heap Tree
    → Syntax Tree

All follow the same rule:
👉 A node can have at most 2 children.
------------------------------------------------------------

# ==========================================================
# TYPES OF BINARY TREE
# ==========================================================

# 1️⃣ FULL BINARY TREE
"""
"""
🧩 Definition:
--------------
If every node in a binary tree has either **0 or 2 children**, 
but not 1, then it is a **Full Binary Tree**.

📘 Key Point:
--------------
- No node should have only one child.

📊 Visualization:
-----------------
        N1
       /  \
     N2    N3
    / \
   N4  N5
  / \
 N7  N8

✅ Every node has either 2 or 0 children.
❌ No single-child nodes exist.

💡 Example in words:
Root (N1) → has 2 children
N2 → has 2 children (N4, N5)
N3 → has 0 children
N4 → has 2 children (N7, N8)
N5, N7, N8 → have 0 children
------------------------------------------------------------

# 2️⃣ PERFECT BINARY TREE
"""
"""
🧩 Definition:
--------------
A **Perfect Binary Tree** is a binary tree in which:
1️⃣ All non-leaf nodes have exactly two children.
2️⃣ All leaf nodes are at the same depth/level.

📊 Visualization:
-----------------
        N1
       /  \
     N2    N3
    / \    / \
   N4 N5  N6 N7

✅ All internal nodes have exactly two children.
✅ All leaves are at the same level (same depth).

🧮 Formula:
-----------
Number of Nodes (N) = (2^(h+1)) - 1
where h = height of tree

Example:
If height = 2 → N = (2^(2+1)) - 1 = 7 nodes
------------------------------------------------------------

# 3️⃣ COMPLETE BINARY TREE
"""
"""
🧩 Definition:
--------------
A **Complete Binary Tree** is a binary tree in which:
- All levels are completely filled **except possibly the last one**.
- The last level has all nodes **as left as possible**.

📊 Visualization:
-----------------
        N1
       /  \
     N2    N3
    / \    / \
   N4 N5  N6 N7
  / \
 N9 N10

✅ All upper levels are full.
✅ Last level is filled from **left to right**.

❌ If any node in the last level appears on the right side leaving left empty → Not complete.

📘 Example of Non-Complete Tree:
If N9 and N10 were under N5 instead of N4, it would not be a complete tree.
------------------------------------------------------------

# 4️⃣ BALANCED BINARY TREE
"""
"""
🧩 Definition:
--------------
A **Balanced Binary Tree** is a tree where:
- The height of the left and right subtrees of every node differ by at most **1**.
- Or equivalently: All leaf nodes are **not more than one level apart** in depth.

📊 Visualization:
-----------------
        N1
       /  \
     N2    N3
    / \      \
   N4 N5     N7

✅ All leaves (N4, N5, N7) are at depth 2.
✅ Height difference between subtrees ≤ 1.

🧮 Property:
------------
|height(left subtree) - height(right subtree)| ≤ 1 for every node.

📘 Balanced Trees are foundation for:
- AVL Tree
- Red-Black Tree
------------------------------------------------------------

# ==========================================================
# IMPLEMENTATION: REPRESENTING BINARY TREE
# ==========================================================

"""
"""
There are two main ways to represent a Binary Tree:

1️⃣ Using Linked List  
2️⃣ Using Python List (Array)
------------------------------------------------------------

# ==========================================================
# 🔹 1. Linked List Representation
# ==========================================================

📘 Concept:
-----------
A Binary Tree can be represented using a **Linked List**, 
where each node contains three components:

1️⃣ data — value of the node  
2️⃣ left pointer — address of the left child  
3️⃣ right pointer — address of the right child  

Each node holds references (or memory addresses) of its left and right children.

This is the most common way to represent binary trees in memory.

# ----------------------------------------------------------
# 📘 Example Node Definition
# ----------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ----------------------------------------------------------
# 📊 Visualization — Linked List Representation (Memory View)
# ----------------------------------------------------------

Visualization:
----------------------------------------

Each node is a block with three parts:
    [ Left_Address |  Data  | Right_Address ]

Here’s how our binary tree looks in linked-list representation:
                                111
                   ┌───────────────────────────────┐
                   │  222  |   Drinks   |   333    │
                   └───────────────────────────────┘
                    /                              \
                222                                  333
        ┌──────────────────────┐                ┌──────────────────────┐
        │  444  | Hot |  555   │                │  666  | Cold | 777   │
        └──────────────────────┘                └──────────────────────┘
            /            \                           /              \
         444              555                     666                777
   ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌───────────────┐
   │null |Tea| null │  │null|Coffee|null│  │null| Cola |null│  │null|Fanta|null│
   └────────────────┘  └────────────────┘  └────────────────┘  └───────────────┘


Explanation:
------------
🟦 Drinks node (111)
   - Left pointer → 222 (Hot)
   - Right pointer → 333 (Cold)

🟩 Hot node (222)
   - Left pointer → 444 (Tea)
   - Right pointer → 555 (Coffee)

🟧 Cold node (333)
   - Left pointer → 666 (Cola)
   - Right pointer → 777 (Fanta)

🟨 Leaf nodes (Tea, Coffee, Cola, Fanta)
   - Both Left and Right pointers are null
     → Left = None, Right = None

----------------------------------------------------------

🧠 Think of each box as a structure stored in memory:
   [left_address | data | right_address]

This is how real binary trees are implemented in programming languages like C, C++, or Python.
------------------------------------------------------------

# ----------------------------------------------------------
# 🧩 Python Example — Constructing the Same Tree
# ----------------------------------------------------------

drinks = Node("Drinks")
hot = Node("Hot")
cold = Node("Cold")
tea = Node("Tea")
coffee = Node("Coffee")
cola = Node("Cola")
fanta = Node("Fanta")

# Linking nodes (left and right pointers)
drinks.left = hot
drinks.right = cold
hot.left = tea
hot.right = coffee
cold.left = cola
cold.right = fanta

In-memory Simulation (addresses for clarity):
---------------------------------------------
Drinks → Left = 222 (Hot), Right = 333 (Cold)
Hot    → Left = 444 (Tea), Right = 555 (Coffee)
Cold   → Left = 666 (Cola), Right = 777 (Fanta)
Tea, Coffee, Cola, Fanta → Left = None, Right = None
----------------------------------------------------------
"""

# ----------------------------------------------------------
# 📘 Explanation Summary
# ----------------------------------------------------------

"""
🧩 Summary:
-----------
✅ Each node = (data + left_pointer + right_pointer)
✅ Left & Right pointers connect nodes (simulate memory addresses)
✅ Leaf nodes have both pointers set to None (or null)
✅ This structure enables dynamic trees (no fixed array size)

🧮 Complexity:
--------------
Access/Traversal: O(n)
Space: O(n)
Each node holds 3 fields (data + 2 pointers)

💡 Benefit:
-----------
- Flexible for insertion/deletion
- Direct child access through pointers
- Natural tree representation in linked memory
----------------------------------------------------------



# 🔹 2. Python List Representation

In list representation:
- Root node is stored at index 1 (index 0 left empty for simplicity).
- We use mathematical formulas to find left and right child locations.

📗 Formula:
-----------
Left child index  = 2 * X  
Right child index = 2 * X + 1  

Here, X = index of the current node.

📊 Example Binary Tree:
-----------------------
        Drinks
       /      \
     Hot       Cold
    /  \       /  \
  Tea Coffee  Non Alcoholic  Alcoholic


Python List Representation:
------------------------------------------------------------------------------------------------- 
|   Index: |  0  |   1    |    2   |    3    |   4    |    5    |      6         |     7        |
|----------|-----|--------|--------|---------|--------|---------|----------------|--------------|  
|   Value: |  X  | Drinks |   Hot  |   Cold  |   Tea  |  Coffee |  Non-Alcoholic |  Alcoholic.  |  
-------------------------------------------------------------------------------------------------

Detailed Explanation (Index-wise):
----------------------------------

1️⃣ Node at index 1 → "Drinks"
    - Left child  = 2 × 1 = 2  → "Hot"
    - Right child = 2 × 1 + 1 = 3  → "Cold"

2️⃣ Node at index 2 → "Hot"
    - Left child  = 2 × 2 = 4  → "Tea"
    - Right child = 2 × 2 + 1 = 5  → "Coffee"

3️⃣ Node at index 3 → "Cold"
    - Left child  = 2 × 3 = 6  → "Non-Alcoholic"
    - Right child = 2 × 3 + 1 = 7  → "Alcoholic"

4️⃣ Node at index 4 → "Tea"
    - Left child  = 2 × 4 = 8  → ❌ (No element at index 8)
    - Right child = 2 × 4 + 1 = 9  → ❌ (No element at index 9)

5️⃣ Node at index 5 → "Coffee"
    - Left child  = 2 × 5 = 10 → ❌
    - Right child = 2 × 5 + 1 = 11 → ❌

6️⃣ Node at index 6 → "Non-Alcoholic"
    - Left child  = 2 × 6 = 12 → ❌
    - Right child = 2 × 6 + 1 = 13 → ❌

7️⃣ Node at index 7 → "Alcoholic"
    - Left child  = 2 × 7 = 14 → ❌
    - Right child = 2 × 7 + 1 = 15 → ❌

📘 Summary Table:
--------------------------------------------------------------------
| Index  | Node Name      | Left Child (2x)   | Right Child (2x+1) |
|--------|----------------|-------------------|--------------------|
| 1      | Drinks         | 2 (Hot)           | 3 (Cold)           |
| 2      | Hot            | 4 (Tea)           | 5 (Coffee)         |
| 3      | Cold           | 6 (Non-Alcoholic) | 7 (Alcoholic)      |
| 4      | Tea            | None              | None               |
| 5      | Coffee         | None              | None               |
| 6      | Non-Alcoholic  | None              | None               |
| 7      | Alcoholic      | None              | None               |
--------------------------------------------------------------------
✅ Index 0 is unused to simplify the child index formula.
✅ Each node uses formulas `2x` and `2x+1` to locate children.
✅ Traversal and insertion become easy using index math.

------------------------------------------------------------
"""
"""
🧭 Summary of Binary Tree Types:
------------------------------------------------------------------------------------------
| Type                 | Description                                                     |
|----------------------|---------------------------------------------------------------- |
| Full Binary Tree     | Each node has 0 or 2 children                                   | 
| Perfect Binary Tree  | All internal nodes have 2 children, all leaves at same level    |
| Complete Binary Tree | All levels filled except last, which is filled from left        |
| Balanced Binary Tree | Left & right subtree heights differ by ≤ 1                      |
------------------------------------------------------------------------------------------

🧮 Formula Recap:
-----------------
For Perfect Binary Tree:
- Total Nodes = (2^(h+1)) - 1
- Total Leaf Nodes = 2^h

------------------------------------------------------------
⏱️ Time Complexity (for traversal or insertion):
------------------------------------------------------------
O(n) — Visiting every node once
💾 Space Complexity (for recursion):
O(h) — Height of the tree

------------------------------------------------------------
🎯 Key Takeaways:
-----------------
✅ Binary Tree allows max 2 children per node.
✅ Basis for advanced trees (BST, AVL, Heap, Red-Black).
✅ Can be represented using Linked List or Python List.
✅ Helps in solving problems like Huffman coding, Expression parsing, etc.

------------------------------------------------------------
"""

