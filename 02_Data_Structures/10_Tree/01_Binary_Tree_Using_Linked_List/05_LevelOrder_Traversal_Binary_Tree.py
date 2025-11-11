r"""
📘 Topic: LevelOrder Traversal of Binary Tree (Linked List Representation)
========================================================================

🎯 Purpose:
------------
To understand how **LevelOrder Traversal** works in a Binary Tree
and how to implement it using a **Queue** (Breadth First Search approach).

In this traversal method, we visit:
-----------------------------------
1️⃣ Level 1 (Root)
2️⃣ Level 2 (Children of Root)
3️⃣ Level 3 (Grandchildren)
4️⃣ … and so on until all levels are visited.

This is the only traversal that visits nodes **level by level**, from top to bottom
and from **left to right** within each level.

=======================================================================
🌳 Tree Example:
=======================================================================

Let's consider this Binary Tree:

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7
                \
                 10

Traversal follows the pattern:
-------------------------------
Level 1 → 1  
Level 2 → 2, 3  
Level 3 → 4, 5, 6, 7  
Level 4 → 10  

Final LevelOrder Sequence:
---------------------------
👉 1 → 2 → 3 → 4 → 5 → 6 → 7 → 10

=======================================================================
📊 Visualization 
=======================================================================

LevelOrder Traversal (Breadth-First Search)
-------------------------------------------

                1
             /     \
           2         3
         /   \     /   \
        4     5   6     7
               \
                10

Level 1: 1  
Level 2: 2 → 3  
Level 3: 4 → 5 → 6 → 7  
Level 4: 10  

Traversal Order:
================
1 → 2 → 3 → 4 → 5 → 6 → 7 → 10

=======================================================================
💻 Python Implementation
=======================================================================
"""

# -----------------------------
# IMPORT QUEUE LINKED LIST
# -----------------------------
import QueueLinkedList as queue  # Queue implemented via Linked List (from previous section)

# -----------------------------
# CLASS DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        """
        📘 Constructor (__init__):
        -------------------------
        - Initializes a Binary Tree node with `data`, `leftchild`, and `rightchild`.
        - Each node can have at most two children.
        """
        self.data = data
        self.leftchild = None
        self.rightchild = None


# -----------------------------
# TREE CREATION
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

"""
At this point, the Binary Tree looks like:

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7
"""

# -----------------------------
# LEVEL ORDER TRAVERSAL FUNCTION
# -----------------------------
def levelOrderTraversal(rootnode):
    """
    📘 Function: levelOrderTraversal(rootnode)
    ------------------------------------------
    Traverses the Binary Tree **level by level** using a Queue.

    Logic:
    -------
    1️⃣ Create an empty queue.
    2️⃣ Enqueue the root node.
    3️⃣ While queue is not empty:
        - Dequeue a node and print its data.
        - Enqueue its left child (if exists).
        - Enqueue its right child (if exists).

    This ensures that nodes are visited **in order of their level**.
    """
    if not rootnode:
        return
    else:
        customQueue = queue.Queue()        # Create a custom queue
        customQueue.enqueue(rootnode)      # Enqueue the root node

        # Process nodes level by level
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)

            # Enqueue Left Child
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)

            # Enqueue Right Child
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)


# -----------------------------
# FUNCTION CALL
# -----------------------------
print("🧭 LevelOrder Traversal Output:\n")
levelOrderTraversal(newBT)

"""
Expected Output:
----------------
1
2
3
4
5
6
7

📘 Explanation:
---------------
Traversal Path (Level by Level):
--------------------------------
Level 1 → 1  
Level 2 → 2, 3  
Level 3 → 4, 5, 6, 7  

Traversal Sequence:
👉 1 → 2 → 3 → 4 → 5 → 6 → 7
"""

# -----------------------------
# TIME & SPACE COMPLEXITY ANALYSIS
# -----------------------------
"""
📈 Time Complexity: O(n)
------------------------
- Each node is visited exactly once.
- n = total number of nodes in the binary tree.

📊 Space Complexity: O(n)
-------------------------
- Due to use of queue to store all nodes level by level.
- In the worst case, queue will hold all nodes of the last level.

=======================================================================
🧩 Summary
=======================================================================
✅ LevelOrder Traversal = Breadth First Search (BFS)  
✅ Traverses all levels from top to bottom, left to right.  
✅ Time Complexity  → O(n)  
✅ Space Complexity → O(n)  
✅ Uses Queue as helper data structure (FIFO principle).

=======================================================================
📘 Next Steps:
--------------
Now we have learned all four binary tree traversal techniques:
1️⃣ PreOrder  → Root ➜ Left ➜ Right  
2️⃣ InOrder   → Left ➜ Root ➜ Right  
3️⃣ PostOrder → Left ➜ Right ➜ Root  
4️⃣ LevelOrder → Level-by-Level (using Queue)

➡️ Next, we will learn **Insertion** and **Deletion** in Binary Trees.
=======================================================================
"""
