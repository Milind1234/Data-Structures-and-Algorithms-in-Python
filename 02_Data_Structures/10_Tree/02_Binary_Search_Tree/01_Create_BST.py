r"""
===============================================================================
📘 Topic: Creating a Binary Search Tree (BST) — Linked List Representation
===============================================================================

🎯 Purpose:
-----------
To understand:
- What operations can be performed on a Binary Search Tree (BST)
- How to create a BST using **linked list node structure**
- Why BST creation is an **O(1)** operation

Before implementing insertion, deletion, search, and traversal, we begin with
the very first operation → **Creating a BST Node**.

===============================================================================
🌳 What Operations Can We Perform on a BST?
===============================================================================

A Binary Search Tree supports the following operations:

1️⃣ Create a BST  
2️⃣ Insert a node  
3️⃣ Delete a node  
4️⃣ Search for a value  
5️⃣ Traverse all nodes (preorder, inorder, postorder, level-order)  
6️⃣ Delete the entire BST  

In this lecture, we focus only on **BST creation**.

===============================================================================
🌲 What Does "Creating a BST" Mean?
===============================================================================

Creating a BST simply means:

➡ Creating a node structure  
➡ Setting `data`, `leftchild`, and `rightchild`  
➡ Making the *root* node of the tree  

We create a class where:
- `data` stores the value
- `leftchild` points to the left subtree
- `rightchild` points to the right subtree

This is the fundamental building block for all upcoming operations.

===============================================================================
💻 CODE — Create BST Node Class
===============================================================================
"""

class BSTNode:
    def __init__(self, data):
        """
        📘 __init__ — Constructor for Binary Search Tree Node
        -----------------------------------------------------

        A BST node contains:
        - data        → Value stored inside the node
        - leftchild   → Pointer to left subtree
        - rightchild  → Pointer to right subtree

        Both children are initially set to None.
        """
        self.data = data
        self.lefthcild = None      # (Note: Typo kept intentionally as per your code)
        self.rightchild = None


# Creating a new BST (root node)
newBST = BSTNode(None)

"""
===============================================================================
🧠 Explanation of Code
===============================================================================

1️⃣ **We define a class `BSTNode`**  
   This class represents a single node in a binary search tree.

2️⃣ **Inside the constructor:**
   - `self.data` stores the node's value.
   - `self.lefthcild = None` initializes the left subtree as empty.
   - `self.rightchild = None` initializes the right subtree as empty.

3️⃣ **Creating the BST**
   When we write:
        newBST = BSTNode(None)
   we are creating the *root node* of our BST.

   Later, during insertion:
   - If root data is None → the first insert will place a value into root.
   - If root already has a value → insertion will follow BST rules.

===============================================================================
⏱ Time & Space Complexity
===============================================================================

📌 Time Complexity → **O(1)**  
Why?  
We only initialize:
- data → constant time  
- left child → constant time  
- right child → constant time  

📌 Space Complexity → **O(1)**  
Why?  
We create only *one node*.

===============================================================================
📘 Summary
===============================================================================

✔ BST is created using a simple node with:
   • data  
   • leftchild  
   • rightchild  

✔ Root can start with:
   • a value  
   • or None (empty tree)

✔ Time Complexity → O(1)  
✔ Space Complexity → O(1)

This is the very first step in building a Binary Search Tree.
In the **next lecture**, we will learn:

➡ How to **insert nodes** into the BST  
➡ How BST maintains ordering automatically  

===============================================================================
"""
