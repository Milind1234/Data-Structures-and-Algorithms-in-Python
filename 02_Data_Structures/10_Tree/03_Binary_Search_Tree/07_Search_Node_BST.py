r"""
📘 Topic: Searching a Node in a Binary Search Tree (BST)
=========================================================

🎯 Goal:
--------
Understand how to search for a value in a **Binary Search Tree (BST)**  
using **recursive comparison logic**.

A BST guarantees that:
- All LEFT subtree values  ≤ parent node  
- All RIGHT subtree values > parent node  

This property allows searching efficiently:
➡ Average Time: **O(log n)**  
➡ Worst Case (skewed tree): **O(n)**  


=========================================================
🌳 Example BST Used in This Code
=========================================================

We inserted the following values:

        4, 2, 6, 1, 3, 5, 7

BST structure becomes:

                    4
                 /     \
               2         6
             /  \      /   \
            1    3    5     7


=========================================================
🔎 HOW SEARCH WORKS (searchNodeBST)
=========================================================

We compare the target value with the **current node**:

1️⃣ If root is None → Tree empty → Not found  

2️⃣ If target == current node's data  
       → 🎉 FOUND  

3️⃣ If target < current data  
       → Search ONLY in LEFT subtree  

4️⃣ If target > current data  
       → Search ONLY in RIGHT subtree  

We recursively continue until:
✔ We find the value  
❌ Or we reach a NULL pointer (means value not present)  


=========================================================
💡 Example Searches
=========================================================

Searching 5:
- Compare with 4 → go RIGHT
- Compare with 6 → go LEFT
- Compare with 5 → FOUND ✔

Searching 10:
- Compare with 4 → go RIGHT
- Compare with 6 → go RIGHT
- Compare with 7 → go RIGHT → NULL  
→ NOT FOUND ❌  


=========================================================
💻 PYTHON CODE (BST Search)
=========================================================
"""

# ================================================================
# 🏷️ BST NODE CLASS
# ================================================================
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# ================================================================
# 🏷️ INSERT FUNCTION (Used Only for Building BST)
# ================================================================
def insertNodeBST(rootnode, node_value):
    if rootnode.data == None:
        rootnode.data = node_value
    elif node_value <= rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.leftchild, node_value)
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(node_value)
        else:
            insertNodeBST(rootnode.rightchild, node_value)

    return f"The Node {node_value} has been successfully Inserted "


# ================================================================
# 🏷️ SEARCH FUNCTION — searchNodeBST
# ================================================================
def searchNodeBST(rootnode, target_node):
    """
    Recursively searches for a value in the BST.
    Uses BST property to eliminate half of the tree each step.
    """
    # CASE 1 — Tree empty
    if rootnode is None or rootnode.data is None:
        return f"{target_node} is not  Present"

    # CASE 2 — Node found
    if rootnode.data == target_node:
        return f"{target_node} is Present in BST"

    # CASE 3 — Search LEFT subtree
    if target_node < rootnode.data:
        return searchNodeBST(rootnode.leftchild, target_node)

    # CASE 4 — Search RIGHT subtree
    return searchNodeBST(rootnode.rightchild, target_node)


# ================================================================
# 🏷️ BUILD BST FOR DEMO
# ================================================================
newBST = BSTNode(None)
print(insertNodeBST(newBST,4))
print(insertNodeBST(newBST,2))
print(insertNodeBST(newBST,6))
print(insertNodeBST(newBST,1))
print(insertNodeBST(newBST,3))
print(insertNodeBST(newBST,5))
print(insertNodeBST(newBST,7))

print("\n📘 BST Inorder Output (Sorted):")
print(newBST)   # optional (only works if __str__ defined)


# ================================================================
# 🏷️ SEARCH TEST
# ================================================================
print(searchNodeBST(newBST,10))
print(searchNodeBST(newBST,3))

r"""
=========================================================
📤 OUTPUT (Expected)
=========================================================

The Node 4 has been successfully Inserted
The Node 2 has been successfully Inserted
The Node 6 has been successfully Inserted
The Node 1 has been successfully Inserted
The Node 3 has been successfully Inserted
The Node 5 has been successfully Inserted
The Node 7 has been successfully Inserted

📘 BST Inorder Output (Sorted):
1 2 3 4 5 6 7

10 is not Present

=========================================================
⏱️ TIME & SPACE COMPLEXITY
=========================================================

Time Complexity:
    Average → O(log n)  
    Worst   → O(n)

Space Complexity:
    O(log n) due to recursion depth  
    (Worst: O(n) if skewed)

=========================================================
✔ SUMMARY
=========================================================
✔ Efficient BST search using recursive comparison  
✔ Skips half of the tree at each step  
✔ Much faster than linear search  
✔ Works on any properly formed BST  

=========================================================
"""



# def searchNodeBST(rootnode , target_node):
#     if not rootnode:
#         return "The BST is Empty"
#     elif rootnode.data == target_node:
#         return f"{target_node} is Present in BST"
#     elif target_node < rootnode.data:
#         if rootnode.leftchild is not None:
#             if rootnode.leftchild.data == target_node:
#                 return f"{target_node} is Present in BST"
#             else:
#                 searchNodeBST(rootnode.leftchild , target_node)
#         else:
#             if rootnode.rightchild is not None:
#                 if rootnode.rightchild.data == target_node:
#                     return f"{target_node} is Present in BST"
#                 else:
#                     searchNodeBST(rootnode.rightchild , target_node)
#     else:
#         return f"{target_node} is Not  Present in BST"