r"""
📘 Topic: Binary Search Tree (BST) — Insertion + PreOrder Traversal
==================================================================

🎯 Purpose
----------
To understand how a **Binary Search Tree (BST)** works, and how to:
1️⃣ Insert nodes into the BST  
2️⃣ Traverse the BST using **Preorder Traversal** (Root → Left → Right)

This note explains both the **concept** and the **code flow**.

==================================================================
🌳 What is a Binary Search Tree?
==================================================================
A BST is a special type of Binary Tree with rules:

1️⃣ **Left subtree** contains values **≤ parent**  
2️⃣ **Right subtree** contains values **> parent**

Example BST:

                     5
                  /      \
                4         6
              /          /  \
             2          7    8
              \
               3

This ordering makes:
✔ Searching fast  
✔ Insertion fast  
✔ Deletion structured  

==================================================================
🧠 Why BST Insertion is Fast (O(log N))?
==================================================================
At each comparison, the tree eliminates **half** of the remaining nodes.

Example:
Searching for 7 in the tree above:

5 → 6 → 7  
Only 3 steps (log₂7 ≈ 2.8)

Balanced BST height = **log N**  
→ Insert/Search/Delete = **O(log N)**

⚠ Worst case (skewed tree): O(N)

==================================================================
🏷️ INSERTION LOGIC — Step-by-Step
==================================================================

To insert a new value:

CASE 1 — Tree is empty  
--------------------------------
root.data is None → Insert value at root.

CASE 2 — Value ≤ root  
--------------------------------
Go to *left subtree*  
If leftchild is None → insert  
Else → recurse

CASE 3 — Value > root  
--------------------------------
Go to *right subtree*  
If rightchild is None → insert  
Else → recurse

This ensures the BST property remains valid.

==================================================================
📘 PreOrder Traversal: (Root → Left → Right)
==================================================================
Algorithm:
----------
1️⃣ Visit (print) current node  
2️⃣ Recursively traverse LEFT subtree  
3️⃣ Recursively traverse RIGHT subtree  

Example output for this tree:

    5
  /    \
 4      6
/      / \
2     7   8
 \
  3

Preorder Output:
→ 5, 4, 2, 3, 6, 7, 8

==================================================================
💻 Code (Your exact code – only comments added)
==================================================================
"""

# ============================================================
# 🏷️ BST Node Class
# ============================================================
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

    # CASE 2 — Insert into LEFT subtree (value <= root)
    elif node_value <= rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.leftchild, node_value)

    # CASE 3 — Insert into RIGHT subtree (value > root)
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.rightchild, node_value)

    return f"The Node {node_value} has been successfully Inserted "

# ============================================================
# 🏷️ PREORDER TRAVERSAL — Root → Left → Right
# ============================================================
def preOrderTraversal(rootnode):
    if not rootnode:
        return 
    print(rootnode.data)
    preOrderTraversal(rootnode.leftchild)
    preOrderTraversal(rootnode.rightchild)

# ============================================================
# 🏷️ DRIVER CODE — Insert + Display
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
print(newBST)     # __str__ prints inorder traversal

print("\n📘 PreOrder Traversal Output:")
preOrderTraversal(newBST)


r"""
==================================================================
⏱ Time & Space Complexity
==================================================================

Insertion
---------
Best Case (Balanced BST):    O(log N)  
Worst Case (Skewed BST):     O(N)  

Preorder Traversal:
---------
Time:  O(N)  
Space: O(N) (recursion stack)  

==================================================================
✅ Summary
==================================================================
✔ Built a BST using Linked List nodes  
✔ Inserted values by following BST rules  
✔ Performed Preorder Traversal  
✔ Explained O(log N) behavior of BST  

Next Steps:
-----------
➡ Implement Search in BST  
➡ Implement Delete operation (3 cases)  
➡ Traversals: Inorder, Postorder  
==================================================================
"""
