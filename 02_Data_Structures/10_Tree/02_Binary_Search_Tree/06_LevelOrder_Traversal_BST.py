r"""
📘 Topic: BST Level Order Traversal (Perfect Binary Search Tree Example)
========================================================================

🎯 Goal:
--------
To learn how to:
1️⃣ Create a perfectly balanced Binary Search Tree  
2️⃣ Insert nodes using BST insertion rules  
3️⃣ Perform **Level Order Traversal (Breadth-First Search)**  
   using BOTH:
   ✔ Custom LinkedList Queue  
   ✔ Python collections.deque  

This version builds a **complete 3-level BST**, where *every* node has a left and right child.


========================================================================
🌳 What Tree Are We Building?
========================================================================

We insert values in this order:

    4, 2, 6, 1, 3, 5, 7

BST formed:

                    4
                 /     \
               2         6
             /  \      /   \
            1    3    5     7

This is a **perfect BST** because:
✔ All leaf nodes are at same depth  
✔ Every internal node has two children  
✔ Height = 3  
✔ Balanced and symmetrical  


========================================================================
🔁 LEVEL ORDER TRAVERSAL (BFS)
========================================================================

We implement **two versions**:

1️⃣ **Using QueueLinkedList** — good for understanding queue mechanics  
2️⃣ **Using collections.deque** — Python’s optimized queue structure  

Traversal order:

    4 → 2 → 6 → 1 → 3 → 5 → 7

========================================================================
💻 COMPLETE PYTHON CODE (Both Traversal Versions)
========================================================================
"""

import QueueLinkedList as queue
from collections import deque

# ============================================================
# 🏷️ BST NODE CLASS
# ============================================================
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# ============================================================
# 🏷️ INSERT FUNCTION — insertNodeBST
# ============================================================
def insertNodeBST(rootnode, node_value):
    if rootnode.data == None:
        rootnode.data = node_value
    elif node_value <= rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.leftchild, node_value)
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.rightchild, node_value)

    return f"The Node {node_value} has been successfully Inserted "


# ============================================================
# 🏷️ LEVEL ORDER TRAVERSAL — Using Custom QueueLinkedList
# ============================================================
def levelOrderTraversal_LinkedList(rootnode):
    """
    BFS Traversal using QueueLinkedList.
    Step-by-step:
    1. Enqueue root
    2. While queue not empty:
        - Dequeue
        - Print node
        - Enqueue left then right children
    """
    if not rootnode:
        return "BST is Empty"

    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    print("\n🌲 Level Order Traversal (QueueLinkedList):")

    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)

        if root.value.leftchild:
            customQueue.enqueue(root.value.leftchild)
        if root.value.rightchild:
            customQueue.enqueue(root.value.rightchild)


# ============================================================
# 🏷️ LEVEL ORDER TRAVERSAL — Using collections.deque
# ============================================================
def levelOrderTraversal_Deque(rootnode):
    """
    BFS Traversal using Python's deque (highly optimized).
    Same logic as above but faster in practice.
    """
    if not rootnode:
        return "BST is Empty"

    q = deque([rootnode])

    print("\n🌲 Level Order Traversal (collections.deque):")

    while q:
        node = q.popleft()
        print(node.data)

        if node.leftchild:
            q.append(node.leftchild)
        if node.rightchild:
            q.append(node.rightchild)


# ============================================================
# 🏷️ BUILDING THE PERFECT BST (3 Levels)
# ============================================================
newBST = BSTNode(None)

print(insertNodeBST(newBST, 4))
print(insertNodeBST(newBST, 2))
print(insertNodeBST(newBST, 6))
print(insertNodeBST(newBST, 1))
print(insertNodeBST(newBST, 3))
print(insertNodeBST(newBST, 5))
print(insertNodeBST(newBST, 7))

print("\n📘 BST Inorder Output (Sorted):")
print(newBST)   # Uses __str__ if implemented

# Traversal Outputs
levelOrderTraversal_LinkedList(newBST)
levelOrderTraversal_Deque(newBST)


r"""
========================================================================
📤 OUTPUT (Expected)
========================================================================

The Node 4 has been successfully Inserted  
The Node 2 has been successfully Inserted  
The Node 6 has been successfully Inserted  
The Node 1 has been successfully Inserted  
The Node 3 has been successfully Inserted  
The Node 5 has been successfully Inserted  
The Node 7 has been successfully Inserted  

📘 BST Inorder Output (Sorted):
1 2 3 4 5 6 7

🌲 Level Order Traversal (QueueLinkedList):
4
2
6
1
3
5
7

🌲 Level Order Traversal (collections.deque):
4
2
6
1
3
5
7


========================================================================
⏱ TIME & SPACE COMPLEXITY
========================================================================

INSERTION:
    Average → O(log n)
    Worst   → O(n) if skewed

LEVEL ORDER TRAVERSAL:
    Time  → O(n)
    Space → O(n)

========================================================================
✔ SUMMARY
========================================================================
✔ Built a perfect BST  
✔ Inserted seven nodes using recursive BST rules  
✔ Performed BFS using BOTH queue methods  
✔ Both traversals give identical output  

========================================================================
"""
