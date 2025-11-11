r"""
📘 Topic: InOrder Traversal of Binary Tree (Linked List Representation)
=======================================================================

🎯 Purpose:
------------
To understand how **InOrder Traversal** works in a Binary Tree
and how to implement it recursively using Python.

In this traversal method, we visit:
-----------------------------------
1️⃣ Left Subtree  
2️⃣ Root Node  
3️⃣ Right Subtree

It follows the **Depth First Search (DFS)** traversal pattern,
but visits nodes in sorted order for a Binary Search Tree (BST).

=======================================================================
🌳 Tree Example:
=======================================================================

Let's consider this Binary Tree:

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7

Traversal follows the pattern:
-------------------------------
Left ➜ Root ➜ Right

🟨 Left Subtree: visit 4 → 2 → 5  
🟦 Root Node: visit 1  
🟩 Right Subtree: visit 6 → 3 → 7  

Final InOrder Sequence:
-------------------------
👉 4 → 2 → 5 → 1 → 6 → 3 → 7

=======================================================================
📊 Visualization 
=======================================================================

InOrder Traversal of Binary Tree
---------------------------------

        Left Subtree
             ↓
         Root Node
             ↓
        Right Subtree

Traversal Order:
4 → 2 → 5 → 1 → 6 → 3 → 7

📘 Diagram Flow:
---------------
                1
              /   \
           (L)2     (R)3
           / \       / \
          4   5     6   7

Left → Root → Right
===================
Left Subtree (4 → 2 → 5)
Root (1)
Right Subtree (6 → 3 → 7)

=======================================================================
💻 Python Implementation
=======================================================================
"""

# -----------------------------
# CLASS DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# -----------------------------
# TREE CREATION
# -----------------------------
newBT = TreeNode("1")

# Level 1 children
leftchild = TreeNode("2")
rightchild = TreeNode("3")

newBT.leftchild = leftchild
newBT.rightchild = rightchild

# Level 2 (left subtree)
tea = TreeNode("4")
coffee = TreeNode("5")
leftchild.leftchild = tea
leftchild.rightchild = coffee

# Level 2 (right subtree)
cola = TreeNode("6")
fanta = TreeNode("7")
rightchild.leftchild = cola
rightchild.rightchild = fanta

r"""
At this point, the Binary Tree looks like:

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7
"""

# -----------------------------
# INORDER TRAVERSAL FUNCTION
# -----------------------------
def inOrderTraversal(rootnode, level=0):
    """
    📘 Function: inOrderTraversal(rootnode)
    ---------------------------------------
    Traverses the Binary Tree in InOrder:
      1️⃣ Visit Left Subtree
      2️⃣ Visit Root Node
      3️⃣ Visit Right Subtree

    Uses recursion to visit every node in correct sequence.

    Base Condition:
      - If rootnode is None → return (stop recursion)
    """
    if not rootnode:
        return

    # Step 1: Visit Left Subtree
    inOrderTraversal(rootnode.leftchild, level + 1)

    # Step 2: Visit Root
    indent = "  " * level
    print(indent + rootnode.data)

    # Step 3: Visit Right Subtree
    inOrderTraversal(rootnode.rightchild, level + 1)


# -----------------------------
# FUNCTION CALL
# -----------------------------
print("🧭 InOrder Traversal Output:\n")
inOrderTraversal(newBT)

"""
Expected Output:
----------------
    4
  2
    5
1
    6
  3
    7

📘 Explanation:
---------------
Traversal path:
Left → Root → Right

So,
1️⃣ Visit Left Subtree → 4 → 2 → 5  
2️⃣ Visit Root Node → 1  
3️⃣ Visit Right Subtree → 6 → 3 → 7

Traversal Sequence:
👉 4 → 2 → 5 → 1 → 6 → 3 → 7
"""

# -----------------------------
# TIME & SPACE COMPLEXITY ANALYSIS
# -----------------------------
"""
📈 Time Complexity: O(n)
------------------------
- Each node is visited exactly once.
- n = total number of nodes in the tree.

📊 Space Complexity: O(n)
-------------------------
- Due to recursive calls using the call stack.
- In the worst case (skewed tree), stack depth = n.

=======================================================================
🧩 Summary
=======================================================================
✅ InOrder Traversal = Left ➜ Root ➜ Right  
✅ Recursive logic visits all nodes exactly once.  
✅ Time Complexity  → O(n)  
✅ Space Complexity → O(n)  
✅ DFS-based traversal (Depth First Search)

=======================================================================
📘 Next Steps:
--------------
In the next note, we will learn:
➡️ **PostOrder Traversal** — where we visit nodes in the order:
   Left ➜ Right ➜ Root
=======================================================================
"""
