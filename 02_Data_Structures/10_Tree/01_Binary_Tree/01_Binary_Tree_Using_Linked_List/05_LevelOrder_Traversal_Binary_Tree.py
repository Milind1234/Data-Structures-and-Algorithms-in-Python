r"""
📘 Topic: LevelOrder Traversal of Binary Tree (Linked List & Deque Implementation)
=================================================================================

🎯 Purpose:
------------
To understand how **LevelOrder Traversal (Breadth-First Search)** works in a Binary Tree
and to implement it in two ways:
1️⃣ Using a **custom Queue (Linked List)**  
2️⃣ Using Python’s **collections.deque**

=======================================================================
📖 Definition
=======================================================================
In **LevelOrder Traversal**, we visit all nodes of a binary tree **level by level** —
starting from the root (Level 1), then Level 2, and so on, until the last level.

Order of traversal:
--------------------
Root ➜ Children ➜ Grandchildren ➜ ...

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

Traversal Levels:
-----------------
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

# =============================================================
# 🧩 METHOD 1 — Using Custom Queue (Linked List-based)
# =============================================================

import QueueLinkedList as queue  # Import custom queue class (from previous module)

# -----------------------------
# CLASS DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        """
        📘 Constructor (__init__):
        -------------------------
        Initializes a Binary Tree node with:
          - data (value)
          - leftchild
          - rightchild
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

r"""
At this point, the Binary Tree looks like:

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7
"""

# -----------------------------
# LEVEL ORDER TRAVERSAL (Custom Queue)
# -----------------------------
def levelOrderTraversal_LinkedList(rootnode):
    """
    📘 Function: levelOrderTraversal_LinkedList(rootnode)
    -----------------------------------------------------
    Traverses the Binary Tree level-by-level using a Queue implemented via Linked List.

    Steps:
    -------
    1️⃣ Create an empty queue.
    2️⃣ Enqueue the root node.
    3️⃣ While the queue is not empty:
         - Dequeue a node.
         - Print its data.
         - Enqueue its left and right children (if they exist).
    """
    if not rootnode:
        return
    else:
        customQueue = queue.Queue()          # Create a custom queue object
        customQueue.enqueue(rootnode)        # Enqueue the root node

        while not(customQueue.isEmpty()):    # Continue until queue is empty
            root = customQueue.dequeue()     # Dequeue the front node
            print(root.value.data)           # Visit current node

            # Enqueue Left Child
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)

            # Enqueue Right Child
            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)


# =============================================================
# 🧩 METHOD 2 — Using Python collections.deque (Efficient Built-in)
# =============================================================
from collections import deque

def levelOrderTraversal_Deque(root):
    """
    📘 Function: levelOrderTraversal_Deque(root)
    --------------------------------------------
    Traverses the Binary Tree using Python's deque for efficient FIFO queue behavior.

    Logic:
    -------
    - Initialize a deque with the root node.
    - Pop nodes from the left.
    - Append left and right children to the right.
    - Continue until deque is empty.

    ✅ Time Complexity → O(n)
    ✅ Space Complexity → O(n)
    """
    if not root:
        return

    queue = deque([root])  # Initialize deque with root node

    while queue:
        node = queue.popleft()      # Pop leftmost node
        print(node.data, end=" --> ")   # Visit current node

        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)


# -----------------------------
# FUNCTION CALLS
# -----------------------------
print("🧭 LevelOrder Traversal using Custom Queue:\n")
levelOrderTraversal_LinkedList(newBT)

print("\n\n🧭 LevelOrder Traversal using Python deque:\n")
levelOrderTraversal_Deque(newBT)

"""
Expected Output:
----------------
🧭 LevelOrder Traversal using Custom Queue:
1
2
3
4
5
6
7

🧭 LevelOrder Traversal using Python deque:
1 2 3 4 5 6 7

📘 Explanation:
---------------
Both functions follow the same traversal sequence:
Root → Level 2 → Level 3 → ...

Traversal Path:
---------------
1 → 2 → 3 → 4 → 5 → 6 → 7

=======================================================================
⚖️ COMPARISON: LinkedList Queue vs Python deque
=======================================================================
| Feature                    | LinkedList Queue        | collections.deque       |
|-----------------------------|-------------------------|-------------------------|
| Implementation              | Manual (custom)         | Built-in (optimized C)  |
| Performance                 | O(1) enqueue/dequeue    | O(1) append/popleft     |
| Educational Value           | Excellent for DSA demo  | Best for production use |
| Code Simplicity             | Medium                  | Very Simple             |
| Use Case                    | Teaching data structure | Real-world applications  |

=======================================================================
🧩 Complexity Analysis
=======================================================================
📈 Time Complexity: O(n)
------------------------
- Every node is enqueued and dequeued exactly once.

📊 Space Complexity: O(n)
-------------------------
- Queue stores all nodes at the current level.
- In the worst case (last level full), queue holds n/2 nodes.

=======================================================================
✅ Summary
=======================================================================
✔ LevelOrder Traversal = Breadth First Search (BFS)  
✔ Traverses tree level by level (top to bottom, left to right)  
✔ Time Complexity  → O(n)  
✔ Space Complexity → O(n)  
✔ Uses a queue (FIFO) as the helper data structure  
✔ Last traversal type in Binary Tree traversal family 🌳

=======================================================================
📘 Next Steps:
--------------
Now that we have learned all four binary tree traversal techniques:
1️⃣ PreOrder  → Root ➜ Left ➜ Right  
2️⃣ InOrder   → Left ➜ Root ➜ Right  
3️⃣ PostOrder → Left ➜ Right ➜ Root  
4️⃣ LevelOrder → Level-by-Level (BFS)

➡️ Next Topic: **Insertion and Deletion in Binary Tree**
=======================================================================
"""
