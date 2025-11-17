r"""
📘 Topic: Searching in Binary Tree (Python List Representation)
==============================================================

🎯 Purpose:
-----------
To search for a node inside a **List-based Binary Tree**.

Since this is NOT a Binary Search Tree (no ordering rule),
we must check **each element one-by-one**.

The list stores values level-by-level:

Index:  0    1    2    3    4  ...
Value: [– ,  1 ,  2 ,  3 ,  4 , ...]

So searching means:
➡ Scan each index in the list  
➡ Compare with target  
➡ If match → Found  
➡ Else → Continue  

==============================================================
🧠 searchNode() — Quick Algorithm
==============================================================

1️⃣ Loop over every index of the list  
2️⃣ If customList[i] == value → FOUND  
3️⃣ If loop finishes with no match → NOT FOUND  

Time Complexity:  
O(n) — must check all nodes in worst case  

Space Complexity:  
O(1) — only simple variables, no extra structure needed  

==============================================================
💻 Python Code (Class + searchNode)
==============================================================
"""

# ==========================================================
# 🏷️ CLASS — BinaryTree (Python List Based)
# ==========================================================

class BinaryTree:
    def __init__(self , size):
        self.customList = size * [None]      # Fixed-size list
        self.lastUsedIndex = 0               # Tracks last inserted index
        self.maxsize = size                  # Maximum size allowed


    # ------------------------------------------------------
    # PRINT TREE CONTENT
    # ------------------------------------------------------
    def __str__(self):
        return f"Binary Tree Array -> {self.customList[1:self.lastUsedIndex+1]} "


    # ------------------------------------------------------
    # INSERT FUNCTION (Level-order insertion)
    # ------------------------------------------------------
    def insertNode(self , value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return "The Binary Tree is Full"

        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return f"The Value {value} inserted successfully"


    # ==========================================================
    # 🏷️ SEARCH FUNCTION — searchNode(value)
    # ==========================================================
    def searchNode(self, node_value):
        """
        📘 searchNode(node_value)
        -------------------------
        Searches for a value inside the binary tree list.

        ✔ Linearly checks each index  
        ✔ Returns immediately if match is found  
        """
        for i in range(len(self.customList)):
            if self.customList[i] == node_value:
                return f"Node {node_value} Found"

        return f"Node {node_value} Not Found"


# -----------------------------
# TESTING
# -----------------------------
newBT = BinaryTree(8)

print(newBT.insertNode("1"))
print(newBT.insertNode("2"))
print(newBT.insertNode("3"))

print(newBT)

print(newBT.searchNode('2'))
print(newBT.searchNode('5'))


r"""
==============================================================
📤 Output:
==============================================================
The Value 1 inserted successfully  
The Value 2 inserted successfully  
The Value 3 inserted successfully  
Binary Tree Array -> ['1', '2', '3']  
Node 2 Found  
Node 5 Not Found  

==============================================================
✅ Summary
==============================================================
✔ Simple linear search  
✔ Works for ANY binary tree (not BST)  
✔ Time Complexity → O(n)  
✔ Space Complexity → O(1)  
✔ Searches level-by-level because of list representation  

Next:
-----
➡ Implement traversal (pre/in/post/level)  
➡ Implement deleteNode (replace with last element)  
==============================================================
"""
