"""
======================================================
INSERTION IN SINGLY LINKED LIST (Concept + Memory View)
======================================================

📌 Insertion can happen in **3 places**:
1️⃣ At the **beginning**
2️⃣ In the **middle** (after a given node)
3️⃣ At the **end**

======================================================
1) INSERTION AT BEGINNING
======================================================
📝 **Steps**:
1) Create a new node (allocate memory for it in heap).
2) Set new_node.next → head (previous first node).
3) Update head → new_node.

📊 **Visualization** (Before → After)
Before:
head → [1 | next] → [2 | next] → [4 | next] → None

Insert(0 at beginning):
new_node(0).next = head
head = new_node

After:
head → [0 | next] → [1 | next] → [2 | next] → [4 | next] → None

======================================================
2) INSERTION IN MIDDLE (after given node)
======================================================
📝 **Steps**:
1) Traverse from head to the node after which you want to insert.
2) Create a new node.
3) Set new_node.next → current.next (next node reference).
4) Set current.next → new_node.

📊 **Visualization** (Insert 3 after node 2)
Before:
head → [1 | next] → [2 | next] → [4 | next] → None

After:
head → [1 | next] → [2 | next] → [3 | next] → [4 | next] → None

======================================================
3) INSERTION AT END
======================================================
📝 **Steps**:
1) Traverse to last node (or directly access tail if available).
2) Create new node.
3) Set last_node.next → new_node.
4) Update tail → new_node.

📊 **Visualization** (Insert 5 at end)
Before:
head → [1 | next] → [2 | next] → [4 | next] → None

After:
head → [1 | next] → [2 | next] → [4 | next] → [5 | next] → None

======================================================
COMPLEXITY
======================================================
- **Insert at Beginning** → O(1)
- **Insert at Middle (given node)** → O(1) (if node already known) else O(n) to find it
- **Insert at End**
    - O(1) (if tail pointer available)
    - O(n) (if no tail pointer)

======================================================
INTERVIEW POINTS 🎯
======================================================
1) Insertion at head → O(1) always.
2) Maintaining tail reference reduces insertion at end from O(n) → O(1).
3) Insertion in middle requires traversal unless node reference is given.
4) Memory allocated dynamically (non-contiguous).
5) Updating pointers is crucial; one wrong assignment breaks the chain.
"""
