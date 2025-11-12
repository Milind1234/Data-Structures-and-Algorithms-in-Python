r"""
📘 Topic: Insertion in Binary Tree (Level Order / BFS Approach)
==============================================================

🎯 Purpose:
------------
To learn how to **insert a new node** into a Binary Tree using **Level Order Traversal (Breadth First Search)**.

Unlike Binary Search Trees (BST), a **normal Binary Tree** does not have any ordering rule,
so insertion happens at the **first available empty position** (left-to-right, level-by-level).

=======================================================================
🧠 Concept:
=======================================================================
We perform insertion **level by level**, using a **queue** (BFS approach).

➡️ Start from the root node.
➡️ Traverse each level:
    - If a node has a missing left child → insert there.
    - Else if a node has a missing right child → insert there.
    - Else → enqueue its children and continue.

This ensures the tree remains as **complete as possible** — filled from top to bottom, left to right.

=======================================================================
🌳 Example Binary Tree:
=======================================================================

Before Insertion:
-----------------
             1
           /   \
         2       3
        / \     /
       4   5   6

Insert 7 → it will go as RIGHT child of node '3'.

After Insertion:
----------------
             1
           /   \
         2       3
        / \     / \
       4   5   6   7

=======================================================================
💡 Algorithm Logic:
=======================================================================

1️⃣ If the tree is empty:
      → Make the new node as root.

2️⃣ Otherwise:
      → Create a queue and enqueue the root node.

3️⃣ While queue is not empty:
      - Dequeue the front node.
      - If its left child is None → insert new node there.
      - Else enqueue the left child.
      - If its right child is None → insert new node there.
      - Else enqueue the right child.

4️⃣ Stop after inserting (first vacant spot found).

=======================================================================
💻 Python Implementation
=======================================================================
"""

# -----------------------------
# IMPORT CUSTOM QUEUE
# -----------------------------
import QueueLinkedList as queue  # Custom Queue implemented using Linked List

# -----------------------------
# CLASS DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        """
        📘 Constructor (__init__):
        -------------------------
        Initializes a Binary Tree node.

        Attributes:
        -----------
        data       : Value stored in the node.
        leftchild  : Reference to left child.
        rightchild : Reference to right child.
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

four = TreeNode("4")
five = TreeNode("5")
leftchild.leftchild = four
leftchild.rightchild = five

six = TreeNode("6")
rightchild.leftchild = six

r"""
Tree Visualization (Before Insertion):
-------------------------------------
             1
           /   \
         2       3
        / \     /
       4   5   6
"""

# =============================================================
# 🧩 METHOD 1 — Insertion Using Custom Queue (Linked List Queue)
# =============================================================
def insertNodeBT(rootNode, newNode):
    """
    📘 Function: insertNodeBT(rootNode, newNode)
    --------------------------------------------
    Inserts a node in a Binary Tree using **Level Order Traversal**
    with a **custom Queue (Linked List)**.

    ⚙️ Logic Flow:
    --------------
    1️⃣ If the tree is empty → newNode becomes the root.
    2️⃣ Otherwise, perform BFS:
        - Enqueue root node.
        - Dequeue one node at a time.
        - If a missing left child is found → insert there.
        - If not, enqueue left child.
        - Repeat the same for the right child.
    3️⃣ Stop once the node is inserted.

    🧠 Why Level Order?
    -------------------
    Because it ensures nodes are filled top-to-bottom, left-to-right
    → maintaining a **Complete Binary Tree** structure.
    """
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            # Check left child
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild = newNode
                return f"🎆 Value '{newNode.data}' inserted successfully on LEFT of '{root.value.data}'"
            
            # Check right child
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild = newNode
                return f"🎆 Value '{newNode.data}' inserted successfully on RIGHT of '{root.value.data}'"


# =============================================================
# 🧩 METHOD 2 — Insertion Using Python deque
# =============================================================
from collections import deque

def insertNodeBT_Deque(rootNode, newNode):
    """
    📘 Function: insertNodeBT_Deque(rootNode, newNode)
    --------------------------------------------------
    Inserts a node in a Binary Tree using a **deque-based queue**.

    ⚙️ Logic Flow:
    --------------
    1️⃣ If root is None → create new root.
    2️⃣ Initialize deque with root node.
    3️⃣ While queue not empty:
        - Dequeue one node.
        - Check if left child is empty → insert and stop.
        - Else enqueue left child.
        - Check if right child is empty → insert and stop.
        - Else enqueue right child.
    """
    if not rootNode:
        rootNode = newNode
        return "🌱 Root node created successfully."
    
    queue = deque([rootNode])

    while queue:
        current = queue.popleft()

        # Check left
        if current.leftchild is None:
            current.leftchild = newNode
            return f"🎆 Value '{newNode.data}' inserted successfully on LEFT of '{current.data}'"
        else:
            queue.append(current.leftchild)

        # Check right
        if current.rightchild is None:
            current.rightchild = newNode
            return f"🎆 Value '{newNode.data}' inserted successfully on RIGHT of '{current.data}'"
        else:
            queue.append(current.rightchild)


# =============================================================
# 📊 LEVEL ORDER TRAVERSAL (for Visualization)
# =============================================================
def levelOrderTraversal_LinkedList(rootnode):
    """
    Prints the Binary Tree nodes level by level using custom queue.
    """
    if not rootnode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)


# =============================================================
# 🧭 FUNCTION CALLS (Demonstration)
# =============================================================
newNode = TreeNode("7")
print(insertNodeBT(newBT, newNode))

print("\n🧭 Level Order Traversal After First Insertion:")
levelOrderTraversal_LinkedList(newBT)

newNode = TreeNode("8")
print("\n" + insertNodeBT_Deque(newBT, newNode))

print("\n🧭 Level Order Traversal After Second Insertion:")
levelOrderTraversal_LinkedList(newBT)


"""
=======================================================================
📤 Example Output:
=======================================================================

🎆 Value '7' inserted successfully on RIGHT of '3'

🧭 Level Order Traversal After First Insertion:
1
2
3
4
5
6
7

🎆 Value '8' inserted successfully on LEFT of '4'

🧭 Level Order Traversal After Second Insertion:
1
2
3
4
5
6
7
8

=======================================================================
⚙️ Step-by-Step Logic Flow (Deque Example):
=======================================================================

Initial Queue: [1]
1️⃣ Dequeue 1 → has both children → enqueue [2, 3]
2️⃣ Dequeue 2 → has both children → enqueue [3, 4, 5]
3️⃣ Dequeue 3 → missing RIGHT → insert new node (7)

✅ Node '7' inserted at first available position.

=======================================================================
🧩 Time & Space Complexity
=======================================================================

📈 Time Complexity: O(n)
------------------------
- Each node is visited once until the vacant spot is found.
- n = number of nodes.

📊 Space Complexity: O(n)
-------------------------
- Queue may store up to all nodes at the current level.

=======================================================================
✅ Summary
=======================================================================

✔ Insertion uses **Level Order Traversal (BFS)**  
✔ Fills tree from **top to bottom, left to right**  
✔ Works for both **custom queue** and **Python deque**  
✔ Maintains **Complete Binary Tree structure**  
✔ Time Complexity  → O(n)  
✔ Space Complexity → O(n)

=======================================================================
📘 Next Steps:
--------------
➡️ Next, we will learn **Deletion in Binary Tree** —  
   how to remove a node while maintaining tree structure.
=======================================================================
"""
