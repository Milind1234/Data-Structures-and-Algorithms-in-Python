r"""
📘 Topic: Creating & Inserting Nodes in a Binary Tree (Python List Representation)
=================================================================================

🎯 Purpose:
-----------
To represent a **Binary Tree** using a Python List and insert nodes in **level-order**.

=================================================================================
🌳 How Binary Tree Works Using a List
=================================================================================

We store values in a Python list called `customList`.

⚠️ Index 0 is NOT used — helps with easy math.

Child index formulas:
---------------------
Left Child  = 2 * i  
Right Child = 2 * i + 1  

Example:

            1
          /   \
        2       3
       / \     / \
      4   5   6   7

Stored as:
Index:  0   1   2   3   4   5   6   7
Value: [–,  1,  2,  3,  4,  5,  6,  7]

Insertions always go to:
    nextIndex = lastUsedIndex + 1

=================================================================================
🧠 insertNode() — Quick Algorithm
=================================================================================
1️⃣ Check if tree is full  
2️⃣ Compute next index  
3️⃣ Insert value into that index  
4️⃣ Increase lastUsedIndex  
5️⃣ Return success message  

This ensures nodes fill **level-by-level**, **left-to-right** automatically.

=================================================================================
💻 Python Code
=================================================================================
"""

# ==========================================================
# 🏷️ CLASS — BinaryTree (Python List Based)
# ==========================================================

class BinaryTree:
    def __init__(self , size):
        self.customList = size * [None]     # Fixed-size list
        self.lastUsedIndex = 0              # Tracks last filled index
        self.maxSize = size                 # Maximum capacity


    # ==========================================================
    # 🏷️ INSERT FUNCTION — insertNode(value)
    # ==========================================================
    def insertNode(self , value):
        r"""
        📘 insertNode(value) — Insert in Level-Order
        ============================================

        Inserts the value at the next free index:
            index = lastUsedIndex + 1

        This automatically forms a **Complete Binary Tree**.
        """

        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is Full"

        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return f"The Value '{value}' has been successfully inserted"


    # ==========================================================
    # 🏷️ __str__ — Print Only Filled Portion
    # ==========================================================
    def __str__(self):
        return f"Binary Tree Array → {self.customList[1:self.lastUsedIndex+1]}"


# -----------------------------
# TESTING
# -----------------------------
newBT = BinaryTree(8)

print(newBT.insertNode("1"))
print(newBT.insertNode("2"))
print(newBT.insertNode("3"))

print(newBT)

r"""
=================================================================================
📤 Output:
=================================================================================
The Value '1' has been successfully inserted  
The Value '2' has been successfully inserted  
The Value '3' has been successfully inserted  
Binary Tree Array → ['1', '2', '3']

=================================================================================
⏱ Complexity
=================================================================================
Time   → O(1)  
Space  → O(n)

=================================================================================
✅ Summary
=================================================================================
✔ Very fast O(1) insertions  
✔ Perfect level-order growth  
✔ Clean list-based binary tree representation  

Next Steps:
-----------
➡ Traversal (Level-Order)  
➡ Searching nodes  
➡ Deleting nodes  

=================================================================================
"""
