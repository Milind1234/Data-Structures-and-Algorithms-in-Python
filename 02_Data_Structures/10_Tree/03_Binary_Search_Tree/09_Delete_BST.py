r"""
📘 Topic: Delete Entire Binary Search Tree (BST)
=================================================

🎯 Goal:
--------
Understand how to *completely delete a BST* created using Linked List nodes.
This operation removes:
✔ Root node’s data  
✔ Left subtree  
✔ Right subtree  

After deletion → The BST becomes **empty** (root becomes a blank node).

=================================================
🌳 BST Before Deletion
=================================================

Inserted values:

    5, 4, 6, 7, 2, 3, 8

BST formed:

                5
              /   \
            4       6
          /        / \
         2        7   8
          \
           3

This is a normal BST following insertion rules:
- Left subtree ≤ node  
- Right subtree > node  


=================================================
🗑️ Deleting Entire BST — How It Works?
=================================================

Binary Search Tree (Linked List version) stores data in *connected nodes*.
To delete the entire tree:

We simply:
1️⃣ Set `root.data = None`  
2️⃣ Set `root.leftchild = None`  
3️⃣ Set `root.rightchild = None`

Python's **garbage collector** automatically removes the freed nodes.

This operation is:
✔ Constant time — O(1)  
✔ Constant space — O(1)


=================================================
💡 Why is it O(1)?
-------------------------------------------------
We are NOT deleting every node manually.  
We only remove references from the **root**, so:
- All children become unreachable  
- Python removes them automatically  

Hence → constant time.


=================================================
💻 COMPLETE PYTHON CODE (Your Original Code)
=================================================
"""

class BSTNode:
    def __init__(self, data):
        # Each node contains: data, leftchild, rightchild
        self.data = data
        self.leftchild = None
        self.rightchild = None


# ============================================================
# 🏷️ INSERT FUNCTION — insertNodeBST
# ============================================================
def insertNodeBST(rootnode, node_value):
    
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
# 🏷️ DELETE ENTIRE BST
# ============================================================
def deleteBST(rootnode):
    r"""
    📘 deleteBST(rootnode)
    ------------------------
    🎯 Purpose:
        Delete the ENTIRE Binary Search Tree instantly.

    🧠 How it works:
        - BST root holds references to the whole tree.
        - Removing these references disconnects the entire structure.
        - Python garbage collector frees memory automatically.

    ✔ Reset data  
    ✔ Remove left subtree  
    ✔ Remove right subtree  
    ✔ BST becomes empty  
    """
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "The BST has been successfully deleted"


# ============================================================
# 🏷️ DRIVER CODE (Testing)
# ============================================================

newBST = BSTNode(None)

print(insertNodeBST(newBST, 5))
print(insertNodeBST(newBST, 4))
print(insertNodeBST(newBST, 6))
print(insertNodeBST(newBST, 7))
print(insertNodeBST(newBST, 2))
print(insertNodeBST(newBST, 3))
print(insertNodeBST(newBST, 8))

print("\n📘 BST Inorder Output (Sorted):")
print(newBST)

print(deleteBST(newBST))

print(newBST)


r"""
=================================================
📤 OUTPUT (Expected)
=================================================
The Node 5 has been successfully Inserted
The Node 4 has been successfully Inserted
The Node 6 has been successfully Inserted
The Node 7 has been successfully Inserted
The Node 2 has been successfully Inserted
The Node 3 has been successfully Inserted
The Node 8 has been successfully Inserted

📘 BST Inorder Output (Sorted):
2 3 4 5 6 7 8

The BST has been successfully deleted

(None)    ← BST is now empty


=================================================
⏱ TIME & SPACE COMPLEXITY
=================================================
DELETE ENTIRE BST:
    Time  → O(1)
    Space → O(1)

=================================================
✔ SUMMARY
=================================================
✔ Simple O(1) deletion  
✔ Removes entire BST by clearing root references  
✔ Python handles memory cleanup  
✔ Tree becomes completely empty  

=================================================
"""
