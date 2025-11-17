r"""
📘 Topic: Deleting a Node from a Binary Search Tree (BST)
=========================================================

🎯 Goal:
--------
Understand how to **delete a node from a BST** using:
- In-order successor (minimum node from right subtree)
- Recursive deletion logic
- Level-order traversal for verification  

This code also demonstrates building a **perfect 3-level BST** and deleting a value from it.

=========================================================
🌳 BST Structure Before Deletion
=========================================================

We insert the values:

        4, 2, 6, 1, 3, 5, 7

BST formed:

                    4
                 /     \
               2         6
             /  \      /   \
            1    3    5     7

This tree is:
✔ Perfect  
✔ Balanced  
✔ Height = 3  

=========================================================
🗑️ BST Deletion — 3 Possible Cases
=========================================================

1️⃣ **Node has NO children (leaf)**  
   → Directly delete the node  

2️⃣ **Node has ONE child**  
   → Replace node with its child  

3️⃣ **Node has TWO children**  
   → Find in-order successor  
   → Copy successor's value  
   → Delete successor node  

=========================================================

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
# 🏷️ UTILITY — Find In-order Successor (Minimum Right Node)
# ============================================================
def minValueNode(bstnode):
    current = bstnode
    while (current.leftchild is not None):
        current = current.leftchild
    return current


# ============================================================
# 🏷️ DELETE FUNCTION — deleteNode()
# ============================================================
def deleteNode(rootnode , nodevalue):
    r"""
    📘 deleteNode(rootnode, nodevalue)
    ==================================

    🎯 Purpose:
    Delete a node from BST while maintaining BST properties.

    ------------------------------------------------------------
    🧩 HOW THE ALGORITHM WORKS (STEP-BY-STEP)
    ------------------------------------------------------------

    ➤ Step 1: **Search for the node recursively**
        - If nodevalue < root → go left
        - If nodevalue > root → go right
        - If equal → we found the node to delete

    ➤ Step 2: **Perform deletion depending on the case**

    ------------------------------------------------------------
    CASE 1 — Node has NO left child  
    ------------------------------------------------------------
        Just return its right child.
        This effectively removes the current node.

        Example:
                6
                 \
                  7
        Delete 6 → return 7

    ------------------------------------------------------------
    CASE 2 — Node has NO right child  
    ------------------------------------------------------------
        Just return its left child.

        Example:
                6
               /
              5
        Delete 6 → return 5

    ------------------------------------------------------------
    CASE 3 — Node has TWO children  
    ------------------------------------------------------------
        This is the MOST important case.

        Steps:
        1️⃣ Find **in-order successor**  
              → smallest value in RIGHT subtree  
              minValueNode(rootnode.rightchild)

        2️⃣ Replace current node’s data with successor’s data  
              rootnode.data = temp.data

        3️⃣ Recursively delete the successor  
              rootnode.rightchild = deleteNode(...)

        This ensures BST properties remain valid.

    ------------------------------------------------------------
    ⏱ TIME COMPLEXITY
    ------------------------------------------------------------
        Average: O(log n)
        Worst:   O(n) (skewed BST)

    ------------------------------------------------------------
    """

    # STEP 1: Search recursively
    if rootnode is None:
        return rootnode
    
    if nodevalue < rootnode.data:
        rootnode.leftchild = deleteNode(rootnode.leftchild , nodevalue)

    elif nodevalue > rootnode.data:
        rootnode.rightchild = deleteNode(rootnode.rightchild , nodevalue)

    # STEP 2: Node found → Apply the correct deletion case
    else:
        # CASE 1 — Node has NO left child
        if rootnode.leftchild is None:
            temp = rootnode.rightchild 
            rootnode = None
            return temp
        
        # CASE 2 — Node has NO right child
        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        
        # CASE 3 — TWO children → find in-order successor
        temp = minValueNode(rootnode.rightchild)
        rootnode.data = temp.data   # Copy successor value
        rootnode.rightchild = deleteNode(rootnode.rightchild , temp.data)

    return rootnode



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

# DELETE ANY VALUE
print("After Deleting node 4 : ")
deleteNode(newBST , 4)

# Traversal Output
levelOrderTraversal_LinkedList(newBST)


r"""
=========================================================
📤 EXAMPLE OUTPUT (After Deleting 4)
=========================================================

In-order successor of 4 = 5  
Replace → 4 → 5  
Delete original 5  

Tree becomes:

                    5
                 /     \
               2         6
             /  \          \
            1    3          7

Level Order Output:

    5
    2
    6
    1
    3
    7

=========================================================
✔ SUMMARY
=========================================================
✔ Perfect BST created  
✔ Node deleted using full BST deletion algorithm  
✔ Explained all three deletion cases  
✔ Verified using Level Order Traversal  

=========================================================

def deleteNode(rootnode, value):

    # Delete `value` from BST rooted at `rootnode`.
    # Returns the new root of this subtree (useful if the root gets deleted).
    
    if rootnode is None:
        return None

    # 1) Search down the tree
    if value < rootnode.data:
        rootnode.leftchild = deleteNode(rootnode.leftchild, value)
        return rootnode
    if value > rootnode.data:
        rootnode.rightchild = deleteNode(rootnode.rightchild, value)
        return rootnode

    # 2) Found the node to delete (rootnode.data == value)

    # Case A: No left child -> replace node with right child (may be None)
    if rootnode.leftchild is None:
        return rootnode.rightchild

    # Case B: No right child -> replace node with left child
    if rootnode.rightchild is None:
        return rootnode.leftchild

    # Case C: Two children -> find inorder successor (smallest in right subtree)
    succ = rootnode.rightchild
    while succ.leftchild:
        succ = succ.leftchild

    # Copy successor's value into current node, then delete successor node
    rootnode.data = succ.data
    rootnode.rightchild = deleteNode(rootnode.rightchild, succ.data)
    return rootnode
"""


