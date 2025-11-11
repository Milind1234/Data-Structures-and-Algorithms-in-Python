r"""
📘 Topic: Preorder Traversal of Binary Tree (Linked List Representation)
=======================================================================

🎯 Purpose:
------------
To understand how **Preorder Traversal** works in a Binary Tree
and how to implement it recursively using Python.

In this traversal method, we visit:
-----------------------------------
1️⃣ Root Node  
2️⃣ Left Subtree  
3️⃣ Right Subtree

It follows the algorithmic pattern of **Depth First Search (DFS)**.

=======================================================================
🌳 Tree Example:
=======================================================================

Let's consider this Binary Tree (Drinks Example):

                 Drinks
                 /    \
              Hot      Cold
             /  \      /  \
          Tea  Coffee  Cola  Fanta

Traversal follows the pattern:
-------------------------------
Root ➜ Left ➜ Right

🟦 Root Node: visit Drinks first  
🟨 Left Subtree: visit Hot → Tea → Coffee  
🟩 Right Subtree: visit Cold → Cola → Fanta  

Final Preorder Sequence:
-------------------------
👉 Drinks → Hot → Tea → Coffee → Cold → Cola → Fanta

=======================================================================
📊 Visualization 
=======================================================================

PreOrder Traversal of Binary Tree
---------------------------------

        Root Node
            ↓
       Left Subtree
            ↓
       Right Subtree

Traversal Order:
Drinks → Hot → Tea → Coffee → Cold → Cola → Fanta

📘 Diagram Flow:
---------------
                Drinks
              /        \
           (L)Hot       (R)Cold
           /   \         /   \
        Tea   Coffee   Cola  Fanta

Root → Left → Right
===================
Root (Drinks)
  ├─ Left (Hot → Tea → Coffee)
  └─ Right (Cold → Cola → Fanta)

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
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        """Return node info for debugging."""
        left = self.leftChild.data if self.leftChild else None
        right = self.rightChild.data if self.rightChild else None
        return f"[ Data: {self.data}, Left: {left}, Right: {right} ]"


# -----------------------------
# TREE CREATION
# -----------------------------
newBT = TreeNode("Drinks")

# Level 1
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild

# Level 2
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee

cola = TreeNode("Cola")
fanta = TreeNode("Fanta")
rightChild.leftChild = cola
rightChild.rightChild = fanta

r"""
At this point, the Binary Tree looks like:

                 Drinks
                 /    \
              Hot      Cold
             /  \      /  \
          Tea  Coffee  Cola  Fanta
"""

# -----------------------------
# PREORDER TRAVERSAL FOR BINARY TREE
# -----------------------------
def preOrderTraversal(rootNode, level=0):
    """
    Preorder traversal that prints the node data with indentation,
    so the output shows the hierarchical structure.

    Parameters:
      - rootNode : BinaryTreeNode
      - level : int (indentation depth, 0 for root)

    Behavior:
      - If rootNode is None -> return
      - Print " " * (level * indent_size) + rootNode.data
      - Recurse left with level+1, then right with level+1

    This is useful for visual hierarchy output (Root → Left → Right).
    """
    if not rootNode:
        return
    indent = "  " * (level * 1)  # adjust multiplier to increase spaces per level
    print(indent + rootNode.data)
    preOrderTraversal(rootNode.leftChild, level + 1)
    preOrderTraversal(rootNode.rightChild, level + 1)

# -----------------------------
# FUNCTION CALL
# -----------------------------
print("🧭 Preorder Traversal Output:")
preOrderTraversal(newBT)

"""
Expected Output:
----------------
Drinks
Hot
Tea
Coffee
Cold
Cola
Fanta

📘 Explanation:
---------------
Traversal path is:
Root → Left → Right

So,
1️⃣ Visit Root (Drinks)
2️⃣ Traverse Left Subtree → Hot → Tea → Coffee
3️⃣ Traverse Right Subtree → Cold → Cola → Fanta

Traversal Sequence:
Drinks → Hot → Tea → Coffee → Cold → Cola → Fanta
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
✅ Preorder Traversal = Root ➜ Left ➜ Right  
✅ Recursive logic visits all nodes exactly once.  
✅ Time Complexity  → O(n)  
✅ Space Complexity → O(n)  
✅ DFS-based traversal (Depth First Search)

=======================================================================
📘 Next Steps:
--------------
In the next lecture, we will learn:
➡️ **Inorder Traversal** — where we visit nodes in the order:
   Left ➜ Root ➜ Right
=======================================================================
"""