r"""
===============================================================================
📘 Topic: Inserting a Node in a Binary Search Tree (BST) — Linked List Representation
===============================================================================

🎯 Purpose:
-----------
To understand how **insertion works in a Binary Search Tree (BST)** using recursion.

In this lecture, we learn:

- How insertion maintains BST ordering  
- How recursion helps navigate left/right subtrees  
- Why BST insertion is efficient (O(log n) average case)


===============================================================================
🌳 Quick Recap: What is a BST?
===============================================================================

A Binary Search Tree has **two strict properties**:

1️⃣ Left subtree contains values **≤ parent**  
2️⃣ Right subtree contains values **> parent**

This makes searching, inserting, and deleting much faster compared to a normal Binary Tree.

Example BST:

                5
              /   \
             3     8
            / \   / \
           2  4  7   10


===============================================================================
🧠 HOW INSERTION WORKS (Concept)
===============================================================================

To insert a new value into a BST:

1️⃣ If root is empty → insert there  
2️⃣ If value ≤ root → go to LEFT subtree  
3️⃣ If value > root → go to RIGHT subtree  
4️⃣ Continue recursively until you find an empty spot  

Insertion ALWAYS maintains BST ordering.


===============================================================================
💻 CODE — BST Node + Insert Function (Your Code With Comments)
===============================================================================
"""

class BSTNode:
    def __init__(self, data):
        # Each node contains: data, leftchild, rightchild
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def __str__(self):
        """
        📘 __str__ Method — Inorder Traversal Output
        --------------------------------------------
        We print the BST using **inorder traversal**, which always gives
        sorted output for a BST.

        Left → Root → Right
        """
        result = []
    
        def inorder(node):
            if node:
                inorder(node.leftchild)
                result.append(str(node.data))
                inorder(node.rightchild)
    
        inorder(self)
        return " ".join(result)
    

# ============================================================
# 🏷️ INSERT FUNCTION — insertNodeBST
# ============================================================

def insertNodeBST(rootnode, node_value):
    """
    📘 Function: insertNodeBST(rootnode, node_value)
    ------------------------------------------------
    Inserts a new value into the BST while maintaining BST rules.

    ------------------------------------------------------------------
    🧠 Algorithm (Step-by-Step)
    ------------------------------------------------------------------
    1️⃣ If the root is empty → assign new value to root node  
    2️⃣ If new value ≤ root value:
            - If left is empty → insert here  
            - Else → recursively insert in LEFT subtree
    3️⃣ Else (new value > root value):
            - If right is empty → insert here  
            - Else → recursively insert in RIGHT subtree
    ------------------------------------------------------------------

    🌳 Example Insertions (based on your input order)
    --------------------------------------------------
        Insert 5  → becomes root
        Insert 4  → goes LEFT of 5
        Insert 6  → goes RIGHT of 5
        Insert 7  → goes RIGHT of 6
        Insert 2  → goes LEFT of 4
        Insert 3  → goes RIGHT of 2
        Insert 8  → goes RIGHT of 7

    The BST formed:

                      5
                   /     \
                 4         6
               /   \         \
              2     ?         7
               \               \
                3               8
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


r"""
===============================================================================
⏱ Time & Space Complexity
===============================================================================

Average Case:
-------------
📌 Time Complexity → O(log n)  
📌 Space Complexity → O(log n)   (due to recursion stack)

Worst Case (skewed tree like a linked list):
--------------------------------------------
📌 Time Complexity → O(n)  
📌 Space Complexity → O(n)

===============================================================================
✅ Summary
===============================================================================

✔ Insertions follow BST rules  
✔ Recursion makes traversal simple  
✔ Inorder traversal prints sorted values  
✔ Efficient average performance (O(log n))  
✔ This forms the foundation for searching and deletion  

===============================================================================
"""
