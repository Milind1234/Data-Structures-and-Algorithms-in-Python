r"""
📘 Topic: BST Postorder Traversal + BST Insertion (Linked List Based)
====================================================================

🎯 Purpose:
-----------
To understand how a **Binary Search Tree (BST)** is created using linked nodes  
and how **Postorder Traversal** works on the BST.

This note includes:

✔ BST creation  
✔ BST insertion logic  
✔ Postorder traversal explanation (Left → Right → Root)  
✔ Example of a complete BST with 3 levels  


====================================================================
🌳 What is a Binary Search Tree (BST)?
====================================================================

A **BST** is a binary tree with special ordering rules:

1️⃣ Left subtree contains values **less than or equal** to the node  
2️⃣ Right subtree contains values **greater** than the node  

This ordering allows **fast searching, insertion, and deletion**  
in average **O(log n)** time.

--------------------------------------------------------------------
Example BST Used in This Code:
--------------------------------------------------------------------

                4
             /     \
           2         6
         /  \      /   \
        1    3    5     7



====================================================================
🔁 POSTORDER TRAVERSAL (Left → Right → Root)
====================================================================

In Postorder Traversal, we process nodes in this order:

    1. Traverse LEFT subtree  
    2. Traverse RIGHT subtree  
    3. Visit ROOT node  

This gives bottom-up traversal.

Useful for:
✔ Deleting a tree  
✔ Evaluating expression trees  
✔ Processing children before the parent  


Example Postorder Output for this BST:

Left subtree → Right subtree → Root  
1 3 2 5 7 6 4


====================================================================
💻 Python Code Implementation
====================================================================
"""

# ================================================================
# 🏷️ BST NODE CLASS
# ================================================================
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# ================================================================
# 🏷️ INSERT FUNCTION — insertNodeBST
# ================================================================
def insertNodeBST(rootnode, node_value):
    # CASE 1 — Tree is empty (root is None)
    if rootnode.data == None:
        rootnode.data = node_value

    # CASE 2 — Insert to LEFT subtree
    elif node_value <= rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.leftchild, node_value)

    # CASE 3 — Insert to RIGHT subtree
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.rightchild, node_value)

    return f"The Node {node_value} has been successfully Inserted "


# ================================================================
# 🏷️ POSTORDER TRAVERSAL — Left → Right → Root
# ================================================================
def postOrderTraversal(rootnode):
    """
    📘 Postorder Traversal:
    ------------------------
    Traverse LEFT subtree  
    Traverse RIGHT subtree  
    Visit ROOT (print data)

    This is a bottom-up traversal.
    """
    if not rootnode:
        return
    postOrderTraversal(rootnode.leftchild)
    postOrderTraversal(rootnode.rightchild)
    print(rootnode.data)


# ================================================================
# 🏷️ CREATE BST & INSERT VALUES
# ================================================================
newBST = BSTNode(None)
print(insertNodeBST(newBST, 4))
print(insertNodeBST(newBST, 2))
print(insertNodeBST(newBST, 6))
print(insertNodeBST(newBST, 1))
print(insertNodeBST(newBST, 3))
print(insertNodeBST(newBST, 5))
print(insertNodeBST(newBST, 7))

print("\n📘 BST Inorder Output (Sorted):")
print(newBST)   # Uses __str__ (if defined) — optional

print("\n📘 Postorder Traversal Output:")
postOrderTraversal(newBST)


r"""
====================================================================
📤 Final BST Structure:
====================================================================

                4
             /     \
           2         6
         /  \      /   \
        1    3    5     7

Postorder Output:
1 3 2 5 7 6 4

====================================================================
✔ End of Note
====================================================================
"""
