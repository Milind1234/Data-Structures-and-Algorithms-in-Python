r"""
📘 Topic: PostOrder Traversal of Binary Tree (Linked List Representation)
=======================================================================

🎯 Purpose:
------------
To understand how **PostOrder Traversal** works in a Binary Tree
and how to implement it recursively using Python.

In this traversal method, we visit:
-----------------------------------
1️⃣ Left Subtree  
2️⃣ Right Subtree  
3️⃣ Root Node  

It follows the **Depth First Search (DFS)** pattern
but visits the root node *last* — after visiting both subtrees.

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
Left ➜ Right ➜ Root

🟨 Left Subtree: visit 4 → 5 → 2  
🟩 Right Subtree: visit 6 → 7 → 3  
🟦 Root Node: visit 1 (last)

Final PostOrder Sequence:
--------------------------
👉 4 → 5 → 2 → 6 → 7 → 3 → 1

=======================================================================
📊 Visualization 
=======================================================================

PostOrder Traversal of Binary Tree
----------------------------------

      Left Subtree
            ↓
       Right Subtree
            ↓
         Root Node

Traversal Order:
4 → 5 → 2 → 6 → 7 → 3 → 1

📘 Diagram Flow:
---------------
                1
              /   \
           (L)2     (R)3
           / \       / \
          4   5     6   7

Left → Right → Root
===================
Left Subtree (4 → 5 → 2)
Right Subtree (6 → 7 → 3)
Root (1)

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

# Level 1
leftchild = TreeNode("2")
rightchild = TreeNode("3")

newBT.leftchild = leftchild
newBT.rightchild = rightchild

# Level 2 (Left Subtree)
N4 = TreeNode("4")
N5 = TreeNode("5")
leftchild.leftchild = N4
leftchild.rightchild = N5

# Level 2 (Right Subtree)
N6 = TreeNode("6")
N7 = TreeNode("7")
rightchild.leftchild = N6
rightchild.rightchild = N7

r"""
At this point, the Binary Tree looks like:

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7
"""

# -----------------------------
# POSTORDER TRAVERSAL FUNCTION
# -----------------------------
def postOrderTraversal(rootNode, level=0):
    """
    📘 Function: postOrderTraversal(rootNode)
    ----------------------------------------
    Traverses the Binary Tree in PostOrder:
      1️⃣ Visit Left Subtree
      2️⃣ Visit Right Subtree
      3️⃣ Visit Root Node

    Uses recursion to visit every node in correct sequence.

    Base Condition:
      - If rootNode is None → return (stop recursion)
    """
    if not rootNode:
        return

    # Step 1️⃣: Visit Left Subtree
    postOrderTraversal(rootNode.leftchild, level + 1)

    # Step 2️⃣: Visit Right Subtree
    postOrderTraversal(rootNode.rightchild, level + 1)

    # Step 3️⃣: Visit Root Node
    indent = "  " * level
    print(indent + rootNode.data)


# -----------------------------
# FUNCTION CALL
# -----------------------------
print("🧭 PostOrder Traversal Output:\n")
postOrderTraversal(newBT)

"""
Expected Output:
----------------
    4
    5
  2
    6
    7
  3
1

📘 Explanation:
---------------
Traversal path:
Left ➜ Right ➜ Root

So,
1️⃣ Visit Left Subtree → 4 → 5 → 2  
2️⃣ Visit Right Subtree → 6 → 7 → 3  
3️⃣ Visit Root Node → 1  

Traversal Sequence:
👉 4 → 5 → 2 → 6 → 7 → 3 → 1
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
✅ PostOrder Traversal = Left ➜ Right ➜ Root  
✅ Root node is always visited *last*.  
✅ Recursive logic visits all nodes exactly once.  
✅ Time Complexity  → O(n)  
✅ Space Complexity → O(n)  
✅ DFS-based traversal (Depth First Search)

=======================================================================
📘 Next Steps:
--------------
In the next Note, we will learn:
➡️ **LevelOrder Traversal** — a Breadth First Search (BFS) technique
   where we visit nodes *level by level* from top to bottom.
=======================================================================
"""
