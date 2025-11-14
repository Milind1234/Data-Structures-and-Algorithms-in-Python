r"""
📘 Topic: Binary Search Tree (BST) — Insertion + InOrder Traversal
==================================================================

🎯 Purpose
----------
To understand how insertion works in a **Binary Search Tree**  
and how to perform **InOrder Traversal**, which prints the BST in **sorted order**.

In this file, you will learn:
✔ What a BST is  
✔ How insertion works  
✔ How InOrder Traversal works  
✔ Why the output becomes sorted  
✔ Time & space complexity  


==================================================================
🌳 What is a Binary Search Tree?
==================================================================
A BST is a binary tree with special ordering rules:

1️⃣ **Left subtree** contains values **≤ parent node**  
2️⃣ **Right subtree** contains values **> parent node**

This structure makes:
✔ Searching faster  
✔ Insertion ordered  
✔ Inorder traversal sorted  

==================================================================
🏷️ InOrder Traversal (Left → Root → Right)
==================================================================

                     5
                  /      \
                4         6
              /          /  \
             2          7    8
              \
               3
The rule:
---------
1️⃣ Traverse LEFT subtree  
2️⃣ Visit ROOT  
3️⃣ Traverse RIGHT subtree  

In a BST, this ALWAYS produces a **sorted list**  
because values in the left subtree < root < right subtree.

Example output for this BST:
2, 3, 4, 5, 6, 7, 8


==================================================================
💻 Code (Your code – only explained & formatted)
==================================================================
"""

# ============================================================
# 🏷️ BST NODE CLASS
# ============================================================
class BSTNode:
    def __init__(self, data):
        # Node contains: data + leftchild + rightchild
        self.data = data
        self.leftchild = None
        self.rightchild = None

# ============================================================
# 🏷️ INSERT FUNCTION — insertNodeBST
# ============================================================
def insertNodeBST(rootnode, node_value):

    # CASE 1 — Tree is empty → Insert root value
    if rootnode.data == None:
        rootnode.data = node_value

    # CASE 2 — Insert in LEFT subtree
    elif node_value <= rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.leftchild, node_value)

    # CASE 3 — Insert in RIGHT subtree
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.rightchild, node_value)

    return f"The Node {node_value} has been successfully Inserted "

# ============================================================
# 🏷️ INORDER TRAVERSAL — Left → Root → Right
# ============================================================
def inOrderTraversal(rootnode):
    # Empty subtree → nothing to print
    if not rootnode:
        return 
    
    # 1️⃣ Visit LEFT subtree
    inOrderTraversal(rootnode.leftchild)
    
    # 2️⃣ Print ROOT value
    print(rootnode.data)
    
    # 3️⃣ Visit RIGHT subtree
    inOrderTraversal(rootnode.rightchild)

# ============================================================
# 🏷️ DRIVER CODE — Insert + Display Sorted Output
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
print(newBST)   # This uses __str__ inside BSTNode

print("\n📘 InOrder Traversal Output:")
inOrderTraversal(newBST)

r"""
==================================================================
📤 Output (Expected)
==================================================================
The Node 5 has been successfully Inserted 
The Node 4 has been successfully Inserted 
The Node 6 has been successfully Inserted 
The Node 7 has been successfully Inserted 
The Node 2 has been successfully Inserted 
The Node 3 has been successfully Inserted 
The Node 8 has been successfully Inserted 

📘 BST Inorder Output (Sorted):
2 3 4 5 6 7 8

📘 InOrder Traversal Output:
2
3
4
5
6
7
8

==================================================================
🧩 Time & Space Complexity
==================================================================

INORDER TRAVERSAL:
------------------
Time:  O(N)   (visit every node)  
Space: O(N)   (recursive stack)  

==================================================================
✅ Summary
==================================================================
✔ Inserted nodes while maintaining BST properties  
✔ Implemented InOrder traversal  
✔ Understood why InOrder prints BST in sorted order  
✔ Learned complexity analysis  

Next Steps:
-----------
➡ Implement Searching  
➡ Implement Deletion (3 cases of deletion)  
➡ PreOrder + PostOrder traversals  

==================================================================
"""
