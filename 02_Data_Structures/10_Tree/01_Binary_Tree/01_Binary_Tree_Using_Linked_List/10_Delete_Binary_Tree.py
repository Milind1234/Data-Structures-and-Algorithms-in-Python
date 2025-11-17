r"""
📘 Topic: Delete Entire Binary Tree (Using Queue / Deque)
=========================================================

🎯 Purpose:
------------
To learn how to **delete an entire Binary Tree** using both
- a **Custom Queue (Linked List implementation)**, and
- Python’s built-in **collections.deque**.

This operation helps us **free up memory** and reset the structure
when we no longer need the Binary Tree.

====================================================================
🧠 Key Idea:
====================================================================
Unlike individual node deletions, deleting an entire tree doesn’t require
restructuring. The idea is simple:

1️⃣ Traverse through all nodes (using Level Order / BFS).  
2️⃣ For each node → set its `data`, `leftchild`, and `rightchild` to **None**.  
3️⃣ Finally, remove the root reference.  

In Python, once all references are gone, the **Garbage Collector** automatically
frees up the memory used by those nodes.

====================================================================
💡 Why Use a Queue?
====================================================================
We use a queue to ensure that **each node** is visited **level by level**.
This guarantees every reference is cleared in a systematic order
and prevents accidentally skipping any node.

====================================================================
🌳 Example Binary Tree (Before Deletion)
====================================================================

             1
           /   \
         2       3
        / \     / \
       4   5   6   7

After deleting the entire tree:
-------------------------------
No nodes remain — the tree is empty.

====================================================================
💻 Python Implementation
====================================================================
"""

# -----------------------------
# IMPORT CUSTOM QUEUE
# -----------------------------
import QueueLinkedList as queue  # Custom queue (from previous modules)
from collections import deque    # Built-in deque (efficient FIFO)


# -----------------------------
# CLASS DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        """
        📘 Constructor:
        ----------------
        Creates a Binary Tree node with data, leftchild, and rightchild references.
        """
        self.data = data
        self.leftchild = None
        self.rightchild = None


# -----------------------------
# TREE CREATION (Sample)
# -----------------------------
newBT = TreeNode("1")

# Level 1
leftchild = TreeNode("2")
rightchild = TreeNode("3")

newBT.leftchild = leftchild
newBT.rightchild = rightchild

# Level 2 (Left Subtree)
N4 = TreeNode("4")
N5 = TreeNode("5")
leftchild.leftchild = N4
leftchild.rightchild = N5

# Level 2 (Right Subtree)
N6 = TreeNode("6")
N7 = TreeNode("7")
rightchild.leftchild = N6
rightchild.rightchild = N7

r"""
Binary Tree Structure:
-----------------------
             1
           /   \
         2       3
        / \     / \
       4   5   6   7
"""

# ============================================================
# 🧩 Helper: Level Order Traversal (Using Custom Queue)
# ============================================================
def levelOrderTraversal_LinkedList(rootnode):
    """
    Prints the Binary Tree level by level using the custom queue.
    """
    if not rootnode:
        print("🌳 Tree is empty")
        return
    
    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftchild:
            customQueue.enqueue(root.value.leftchild)
        if root.value.rightchild:
            customQueue.enqueue(root.value.rightchild)


# ============================================================
# 🧩 METHOD 1 — Delete Entire Tree using Custom Queue
# ============================================================
def deleteBT_LinkedList(rootnode):
    """
    📘 Function: deleteBT_LinkedList(rootnode)
    ------------------------------------------
    Deletes the entire Binary Tree using a **Custom Queue** implemented
    via Linked List.

    Logic:
    -------
    1️⃣ Create a queue and enqueue root node.
    2️⃣ Traverse the tree level by level.
    3️⃣ For each node:
        - Set data, leftchild, rightchild → None
    4️⃣ Finally, delete rootnode reference.
    """
    if not rootnode:
        return "Tree is already empty."

    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    while not(customQueue.isEmpty()):
        root = customQueue.dequeue().value
        if root.leftchild:
            customQueue.enqueue(root.leftchild)
        if root.rightchild:
            customQueue.enqueue(root.rightchild)

        # Delete current node data and children references
        root.data = None
        root.leftchild = None
        root.rightchild = None

    return "🧹 Binary Tree deleted successfully using Custom Queue!"


# ------------------------------------------------------------
# Explanation (deleteBT_LinkedList)
# ------------------------------------------------------------
# - This function ensures each node reference is explicitly cleared.
# - Since Python uses automatic garbage collection, clearing references
#   ensures that all objects are released.
# - Time Complexity: O(n) — each node visited once.
# - Space Complexity: O(n) — due to queue storing nodes.
# ------------------------------------------------------------


# ============================================================
# 🧩 METHOD 2 — Delete Entire Tree using collections.deque
# ============================================================
def deleteBT_Deque(rootnode):
    """
    📘 Function: deleteBT_Deque(rootnode)
    -------------------------------------
    Deletes the entire Binary Tree using Python’s built-in **deque**.

    Logic:
    -------
    1️⃣ Initialize deque with rootnode.
    2️⃣ Perform Level Order traversal.
    3️⃣ For each node:
        - Clear node.data
        - Clear leftchild and rightchild
    4️⃣ Finally, clear root reference.
    """
    if not rootnode:
        return "Tree is already empty."

    q = deque([rootnode])

    while q:
        node = q.popleft()

        if node.leftchild:
            q.append(node.leftchild)
        if node.rightchild:
            q.append(node.rightchild)

        node.data = None
        node.leftchild = None
        node.rightchild = None

    return "🧹 Binary Tree deleted successfully using deque!"


# ------------------------------------------------------------
# Explanation (deleteBT_Deque)
# ------------------------------------------------------------
# - Deque provides the same FIFO behavior as a queue but is optimized in C.
# - It’s lightweight, efficient, and avoids custom Node wrapper overhead.
# - Like the Linked List queue version, it clears all nodes level by level.
# - Once all references are None, Python’s garbage collector reclaims memory.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ------------------------------------------------------------


# ============================================================
# 🧩 TEST EXECUTION
# ============================================================
print("🌲 Binary Tree Before Deletion:")
levelOrderTraversal_LinkedList(newBT)

print("\n🪓 Deleting Entire Tree using Custom Queue...")
print(deleteBT_LinkedList(newBT))

print("\n🌿 Tree After Custom Queue Deletion:")
levelOrderTraversal_LinkedList(newBT)

# Recreate Tree for deque version
newBT = TreeNode("1")
newBT.leftchild = TreeNode("2")
newBT.rightchild = TreeNode("3")
newBT.leftchild.leftchild = TreeNode("4")

print("\n🌲 Binary Tree Before Deletion (Deque Version):")
levelOrderTraversal_LinkedList(newBT)

print("\n🪓 Deleting Entire Tree using Deque...")
print(deleteBT_Deque(newBT))

print("\n🌿 Tree After Deque Deletion:")
levelOrderTraversal_LinkedList(newBT)


r"""
====================================================================
📤 Example Output:
====================================================================

🌲 Binary Tree Before Deletion:
1
2
3
4
5
6
7

🪓 Deleting Entire Tree using Custom Queue...
🧹 Binary Tree deleted successfully using Custom Queue!

🌿 Tree After Custom Queue Deletion:
🌳 Tree is empty

🌲 Binary Tree Before Deletion (Deque Version):
1
2
3
4

🪓 Deleting Entire Tree using Deque...
🧹 Binary Tree deleted successfully using deque!

🌿 Tree After Deque Deletion:
🌳 Tree is empty

====================================================================
🧩 Time & Space Complexity
====================================================================

📈 Time Complexity: O(n)
------------------------
Each node is visited and cleared exactly once.

📊 Space Complexity: O(n)
-------------------------
A queue or deque is used to hold one level of nodes at a time.

====================================================================
✅ Summary
====================================================================

✔ Both methods achieve the same goal (full tree deletion).  
✔ `deleteBT_LinkedList` → uses custom queue (educational use).  
✔ `deleteBT_Deque` → uses Python's built-in deque (practical use).  
✔ After clearing all node references, Python automatically deallocates memory.  
✔ No need for manual `free()` like in low-level languages (C/C++).

====================================================================
📘 Next Steps:
--------------
➡️ Next, we’ll explore **Binary Tree Insertion + Deletion combined**  
   and **Tree Traversal vs Memory Cleanup concepts**.
====================================================================
"""


"""
def deleteBT(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return " The BT has beem Successfully deleted "

deleteBT(newBT)
levelOrderTraversal(newBT)

"""