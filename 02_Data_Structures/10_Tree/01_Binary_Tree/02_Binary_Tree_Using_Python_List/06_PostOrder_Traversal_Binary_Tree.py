r"""
📘 Topic: PostOrder Traversal in Binary Tree (Python List Representation)
========================================================================

🎯 Purpose:
-----------
To understand how **PostOrder Traversal** works in a Binary Tree stored  
as a **Python List (Array Representation)**.

Traversal Order (DFS):
        Left ➜ Right ➜ Root

This is the opposite direction of PreOrder, and different from InOrder.

=======================================================================
🌳 Binary Tree Structure (Array-Based)
=======================================================================

For an array-backed binary tree:

- Index 1 → Root
- Index 2 → Left child of 1
- Index 3 → Right child of 1
- Index 4 → Left child of 2
- Index 5 → Right child of 2
- Index 6 → Left child of 3
- Index 7 → Right child of 3

If we insert (1 to 7):

              1
           /     \
         2         3
       /  \       /  \
      4    5     6    7

Array representation:

Index : 0   1   2   3   4   5   6   7
Value : [–, 1,  2,  3,  4,  5,  6,  7]

=======================================================================
🧠 PostOrder Traversal (Array Version) — Logic
=======================================================================

**Recurrence Rule:**  
1️⃣ Traverse LEFT subtree  
2️⃣ Traverse RIGHT subtree  
3️⃣ Visit ROOT  

Index math:  
- Left child  → index * 2  
- Right child → index * 2 + 1  

Algorithm (postOrderTraversal(i)):

1. If index > lastUsedIndex → STOP (node doesn't exist)  
2. Recur into left child  
3. Recur into right child  
4. Print the current node value  

PostOrder prints nodes from bottom → up, children before parent.

=======================================================================
🔍 Example Output for Tree [1..7]
=======================================================================

Left Subtree: 4 → 5 → 2  
Right Subtree: 6 → 7 → 3  
Root: 1  

Final PostOrder Sequence:
👉 4, 5, 2, 6, 7, 3, 1

=======================================================================
💻 Python Implementation
=======================================================================
"""

# ===========================================================
# 🏷️ CLASS DEFINITION — BinaryTree (Array-Based)
# ===========================================================

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]     # Fixed-size list
        self.lastUsedIndex = 0              # Tracks last filled index
        self.maxsize = size                 # Capacity limit

    def __str__(self):
        # Pretty print only the used section (ignore index 0)
        return f"The Binary Tree Array -> {self.customList[1:self.lastUsedIndex+1]}"
    
    def insertNode(self , node_value):
        # Tree is full
        if self.lastUsedIndex + 1 == self.maxsize:
            return " The Binary tree is Full"

        # Insert at next available index
        self.customList[self.lastUsedIndex + 1 ] = node_value
        self.lastUsedIndex += 1
        return f"The Node {node_value} is Inserted Successfully"

# ===========================================================
# 🏷️ POSTORDER TRAVERSAL — postOrderTraversal(index)
# ===========================================================

    def postOrderTraversal(self , index):
        r"""
        📘 PostOrder Traversal (Array-Based Binary Tree)
        =================================================

        Traversal Rule:
            LEFT ➜ RIGHT ➜ ROOT

        ------------------------------------------------------------
        🧠 Internal Logic (with Index Math)
        ------------------------------------------------------------
        Given a node at index *i*:
            Left child  → i * 2
            Right child → i * 2 + 1

        So PostOrder works as:

            1️⃣ Visit left child subtree  
                postOrderTraversal(i * 2)

            2️⃣ Visit right child subtree  
                postOrderTraversal(i * 2 + 1)

            3️⃣ Visit root (current node)  
                print(customList[i])

        ------------------------------------------------------------
        ⛔ Base Condition:
        ------------------------------------------------------------
        If index exceeds lastUsedIndex → STOP recursion  
        (no such node in the list)

        ------------------------------------------------------------
        📌 Example Output:
            For tree [1..7], result is:
            4 → 5 → 2 → 6 → 7 → 3 → 1
        ------------------------------------------------------------
        """
        
        # Stop if index is outside tree
        if index > self.lastUsedIndex:
            return 
        
        # 1️⃣ LEFT subtree
        self.postOrderTraversal(index * 2)

        # 2️⃣ RIGHT subtree
        self.postOrderTraversal((index * 2) + 1)

        # 3️⃣ ROOT (print current node)
        print(self.customList[index])



# ===========================================================
# 🧪 TESTING
# ===========================================================

newBT = BinaryTree(9)

print(newBT.insertNode("1"))
print(newBT.insertNode("2"))
print(newBT.insertNode("3"))
print(newBT.insertNode("4"))
print(newBT.insertNode("5"))
print(newBT.insertNode("6"))
print(newBT.insertNode("7"))

print(newBT)

print("\n📌 PostOrder Traversal Output:")
newBT.postOrderTraversal(1)


r"""
=======================================================================
📤 Example Output
=======================================================================

4  
5  
2  
6  
7  
3  
1  

=======================================================================
⏱ Time & Space Complexity
=======================================================================

🕒 Time Complexity  
PostOrder Traversal → **O(n)**  
(visit every node exactly once)

📦 Space Complexity  
Recursive stack → **O(n)** worst case  

=======================================================================
✅ Summary
=======================================================================

✔ Uses array indexing instead of pointers  
✔ Follows standard PostOrder sequence  
✔ Bottom-up traversal  
✔ Very efficient & easy to implement  

Next Steps:
-----------
➡ Level Order Traversal (Array Based)
➡ Deleting Node from Array-Based Binary Tree

=======================================================================
"""
