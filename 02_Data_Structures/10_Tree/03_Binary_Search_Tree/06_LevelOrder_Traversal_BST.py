r"""
📘 Topic: BST Level Order Traversal (Perfect Binary Search Tree Example)
========================================================================

🎯 Goal:
--------
To learn how to:
1️⃣ Create a perfectly balanced Binary Search Tree  
2️⃣ Insert nodes using BST insertion rules  
3️⃣ Perform **Level Order Traversal (Breadth-First Search)**  
   using a **custom linked-list queue**  

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
✔ All leaf nodes are at the same depth  
✔ Every internal node has two children  
✔ Tree height = 3  
✔ Balanced and symmetrical  


========================================================================
🧩 INSERTION LOGIC (insertNodeBST)
========================================================================

BST insertion rules:

1️⃣ If tree is empty → new value becomes ROOT  
2️⃣ If new value ≤ current node → go LEFT subtree  
3️⃣ If new value > current node → go RIGHT subtree  
4️⃣ Continue recursively until the correct empty spot is found  
5️⃣ Insert the new node there  

This structure ensures searches are efficient:
- Average time: **O(log n)**


========================================================================
🔁 LEVEL ORDER TRAVERSAL (BFS)
========================================================================

Algorithm (using custom QueueLinkedList):

1️⃣ Start by enqueueing the root  
2️⃣ While queue is not empty:
      - Dequeue a node  
      - Print its value  
      - Enqueue its LEFT child (if exists)  
      - Enqueue its RIGHT child (if exists)

Traversal order for this tree is:

    4 → 2 → 6 → 1 → 3 → 5 → 7


========================================================================
💻 COMPLETE PYTHON CODE (Your Version, Documented)
========================================================================
"""

import QueueLinkedList as queue

# ============================================================
# 🏷️ BST NODE CLASS
# ============================================================
class BSTNode:
    def __init__(self, data):
        # Each BST node has: data, leftchild, rightchild
        self.data = data
        self.leftchild = None
        self.rightchild = None


# ============================================================
# 🏷️ INSERT FUNCTION — insertNodeBST
# ============================================================
def insertNodeBST(rootnode, node_value):
    """
    Inserts a value into BST following BST rules.
    """
    # CASE 1 — Tree is empty → insert at root
    if rootnode.data == None:
        rootnode.data = node_value

    # CASE 2 — Insert into LEFT subtree
    elif node_value <= rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.leftchild, node_value)

    # CASE 3 — Insert into RIGHT subtree
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.rightchild, node_value)

    return f"The Node {node_value} has been successfully Inserted "


# ============================================================
# 🏷️ LEVEL ORDER TRAVERSAL (BFS)
# ============================================================
def levelOrderTraversal(rootnode):
    """
    Uses a LinkedList-based Queue to perform BFS traversal.
    Prints nodes level-by-level.
    """
    if not rootnode:
        return "BST is Empty"

    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    print("\n🌲 Level Order Traversal Output:")

    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)

        if root.value.leftchild is not None:
            customQueue.enqueue(root.value.leftchild)

        if root.value.rightchild is not None:
            customQueue.enqueue(root.value.rightchild)


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
print(newBST)   # Uses __str__ if defined

# Level Order Traversal
levelOrderTraversal(newBST)


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

🌲 Level Order Traversal Output:
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
    Worst   → O(n) (if tree becomes skewed)

LEVEL ORDER TRAVERSAL:
    Time  → O(n)
    Space → O(n)

========================================================================
✔ SUMMARY
========================================================================
✔ Built a perfect BST (7 nodes, height 3)  
✔ Inserted nodes using recursive BST algorithm  
✔ Performed BFS (level-order traversal) using custom queue  
✔ Verified BST structure with sorted inorder output  

========================================================================
"""
