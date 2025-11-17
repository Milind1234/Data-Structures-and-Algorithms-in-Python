r"""
📘 Topic: Searching in Binary Tree (Level Order / BFS Approach)
==============================================================

🎯 Purpose:
------------
To understand how to **search for a node** in a Binary Tree using **Level Order Traversal (Breadth First Search)**.

Level Order Search checks each node **level by level**, from **top to bottom** and **left to right**.

=======================================================================
🧠 Concept:
=======================================================================
Unlike Binary Search Trees (BST), a **regular binary tree** has no ordering between nodes.
Hence, we cannot perform binary search directly — we must visit **every node** until we find the match.

So, we use **Level Order Traversal (BFS)** — visiting nodes level by level using a **Queue**.

=======================================================================
🌳 Example Binary Tree:
=======================================================================

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7

If we search for `5`, the search path will be:
👉 1 → 2 → 3 → 4 → 5

✅ When 5 is found → we stop immediately.

=======================================================================
💡 Algorithm Logic:
=======================================================================

1️⃣ Start from the **root node**.  
2️⃣ Enqueue the root node into the queue.  
3️⃣ While the queue is not empty:
    - Dequeue one node at a time.
    - If its data matches the target → ✅ Found.
    - Otherwise enqueue its left and right children (if any).
4️⃣ If the queue becomes empty and we still didn’t find the node → ❌ Not Found.

=======================================================================
💻 Python Implementation
=======================================================================
"""

# -----------------------------
# IMPORT CUSTOM QUEUE
# -----------------------------
import QueueLinkedList as queue  # Custom queue (from previous module)

# -----------------------------
# CLASS DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        """
        📘 Constructor (__init__):
        -------------------------
        Creates a new Binary Tree Node.

        Attributes:
        -----------
        data       : Node value
        leftchild  : Pointer to left node
        rightchild : Pointer to right node
        """
        self.data = data
        self.leftchild = None
        self.rightchild = None


# -----------------------------
# TREE CREATION
# -----------------------------
newBT = TreeNode("1")
leftchild = TreeNode("2")
rightchild = TreeNode("3")

newBT.leftchild = leftchild
newBT.rightchild = rightchild

N4 = TreeNode("4")
N5 = TreeNode("5")
leftchild.leftchild = N4
leftchild.rightchild = N5

N6 = TreeNode("6")
N7 = TreeNode("7")
rightchild.leftchild = N6
rightchild.rightchild = N7

"""
Tree Visualization:
-------------------
                 1
               /   \
             2       3
            / \     / \
           4   5   6   7
"""

# =============================================================
# 🧩 METHOD 1 — Search Using Custom Queue (Linked List Queue)
# =============================================================
def searchBT(rootnode, nodeValue):
    """
    📘 Function: searchBT(rootnode, nodeValue)
    ------------------------------------------
    Searches for a node in a Binary Tree using a **Custom Queue (Linked List)**.

    🧠 Intuition:
    -------------
    - A normal binary tree has **no sorting order** (unlike BST),
      so we must look through every node until we find the target.
    - The best way to do that is by **Level Order Traversal (Breadth-First Search)**,
      which visits nodes level by level using a **Queue (FIFO)** structure.

    ⚙️ Working Logic:
    -----------------
    1️⃣ If tree is empty → return message immediately.

    2️⃣ Create an empty custom queue (`QueueLinkedList` object).
        - This queue stores nodes to visit later.
        - We start by enqueueing the root node.

    3️⃣ While the queue is not empty:
        - Dequeue the front node → current node to process.
        - Check if its data matches the target (`nodeValue`).
            • If yes → return success immediately.
        - If not, enqueue its left and right children (if they exist).
          They will be processed next, maintaining level order.

    4️⃣ If the queue becomes empty and node not found → return "Not Found".

    -------------------------------------------------------------------
    Visualization of Queue Flow (for searching '5'):
    -------------------------------------------------------------------
    Initial queue: [1]
    Step 1 → Dequeue 1, enqueue 2 & 3 → queue = [2, 3]
    Step 2 → Dequeue 2, enqueue 4 & 5 → queue = [3, 4, 5]
    Step 3 → Dequeue 3 (no children) → queue = [4, 5]
    Step 4 → Dequeue 4 (no children) → queue = [5]
    Step 5 → Dequeue 5 → ✅ Match → return “Found”
    -------------------------------------------------------------------

    Parameters:
    -----------
    rootnode : TreeNode
        Root of the binary tree.
    nodeValue : str/int
        Value to search for.

    Returns:
    --------
    str
        Message stating whether the node was found.
    """

    # 1️⃣ Handle Empty Tree
    if not rootnode:
        return "Tree is empty"

    # 2️⃣ Create a queue and enqueue the root node
    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    # 3️⃣ Process nodes level by level
    while not(customQueue.isEmpty()):

        # Dequeue the front node
        root = customQueue.dequeue()    # returns a queue node; actual tree node in root.value

        # 4️⃣ Check current node
        if root.value.data == nodeValue:
            return f"✅ Node '{nodeValue}' Found"

        # 5️⃣ Enqueue left child if it exists
        if root.value.leftchild is not None:
            customQueue.enqueue(root.value.leftchild)

        # 6️⃣ Enqueue right child if it exists
        if root.value.rightchild is not None:
            customQueue.enqueue(root.value.rightchild)

    # 7️⃣ If queue becomes empty and we didn’t find the node
    return f"❌ Node '{nodeValue}' Not Found"

# =============================================================
# 🧩 METHOD 2 — Search Using Python collections.deque
# =============================================================
from collections import deque

def searchBT_Deque(rootnode, nodeValue):
    """
    📘 Function: searchBT_Deque(rootnode, nodeValue)
    ------------------------------------------------
    Searches for a node using Python's built-in **deque** (efficient FIFO queue).

    Logic:
    -------
    1️⃣ Use deque to store nodes level-by-level.
    2️⃣ Dequeue each node, check for target value.
    3️⃣ Enqueue its children for next level.
    4️⃣ Stop immediately when found.
    """
    if not rootnode:
        return "Tree is empty"
    
    queue = deque([rootnode])  # Initialize deque with root node
    
    while queue:
        current = queue.popleft()  # Dequeue front element
        
        if current.data == nodeValue:
            return f"✅ Node '{nodeValue}' Found"
        
        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)
    
    return f"❌ Node '{nodeValue}' Not Found"


# =============================================================
# 🧭 FUNCTION CALLS
# =============================================================
print("\n🧭 Searching Node Using Custom Queue:\n")
print(searchBT(newBT, "5"))

print("\n🧭 Searching Node Using deque:\n")
print(searchBT_Deque(newBT, "2"))

"""
=======================================================================
📤 Example Output:
=======================================================================

🧭 Searching Node Using Custom Queue:
✅ Node '5' Found

🧭 Searching Node Using deque:
✅ Node '2' Found

=======================================================================
⚙️ Working of BFS Search:
=======================================================================

If we search for 5:
-------------------
Queue flow →
[1] → [2, 3] → [3, 4, 5] → [4, 5] → [5] → FOUND ✅

Order of visit:
1 → 2 → 3 → 4 → 5

=======================================================================
🧩 Time & Space Complexity
=======================================================================

📈 Time Complexity: O(n)
------------------------
- Each node is visited once until found (or end of tree).
- In the worst case (node not found), all n nodes are scanned.

📊 Space Complexity: O(n)
-------------------------
- Because a queue can hold up to all nodes of the largest level.

=======================================================================
✅ Summary
=======================================================================

✔ Search uses **Level Order Traversal (Breadth-First Search)**  
✔ Works for all kinds of binary trees (not just BST)  
✔ Stops early when the node is found  
✔ Time Complexity  → O(n)  
✔ Space Complexity → O(n)  

=======================================================================
📘 Next Steps:
--------------
➡️ Next we will learn how to **insert a new node** into the Binary Tree.
=======================================================================
"""
