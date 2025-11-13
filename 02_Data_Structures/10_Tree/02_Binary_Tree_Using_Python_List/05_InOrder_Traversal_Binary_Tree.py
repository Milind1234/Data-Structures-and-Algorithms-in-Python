r"""
📘 Topic: InOrder Traversal in Binary Tree (Python List Representation)
=======================================================================

🎯 Purpose:
-----------
To understand how **InOrder Traversal** works when a Binary Tree is stored  
inside a **Python List using index calculations** instead of pointers.

This method uses the classical DFS (Depth First Search) pattern:

        Left ➜ Root ➜ Right

But applied on an **array-backed binary tree**.

=======================================================================
🌳 Binary Tree (Array Representation)
=======================================================================

For a binary tree stored in a list:

- Index 1 → Root
- Index 2 → Left  child of index 1
- Index 3 → Right child of index 1
- Index 4 → Left  child of index 2
- Index 5 → Right child of index 2
- Index 6 → Left  child of index 3
- Index 7 → Right child of index 3

Example Tree:

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7

Stored in list as:

Index : 0   1   2   3   4   5   6   7
Value : [–, 1,  2,  3,  4,  5,  6,  7]

We start traversal from index **1**.

=======================================================================
🧠 InOrder Traversal (Array Version) — Logic
=======================================================================

InOrder Traversal Rule:
    1️⃣ Traverse LEFT subtree  
    2️⃣ Visit ROOT  
    3️⃣ Traverse RIGHT subtree  

For array representation:

- Left child  index = 2 * i
- Right child index = 2 * i + 1

Algorithm Steps for inOrderTraversal(i):

1️⃣ If index > lastUsedIndex → the node does not exist → STOP  
2️⃣ Recursively visit left child  → inOrderTraversal(i * 2)  
3️⃣ Process current node         → print(customList[i])  
4️⃣ Recursively visit right child → inOrderTraversal(i * 2 + 1)

This prints nodes in **sorted structure order** for complete binary trees.

=======================================================================
💻 Python Implementation
=======================================================================
"""

# ===========================================================
# 🏷️ CLASS DEFINITION — BinaryTree (Array-Based)
# ===========================================================

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxsize = size

    def __str__(self):
        return f"The Binary Tree Array -> {self.customList[1:self.lastUsedIndex+1]}"
    
    def insertNode(self , node_value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return " The Binary tree is Full"
        self.customList[self.lastUsedIndex + 1 ] = node_value
        self.lastUsedIndex += 1
        return f"The Node {node_value} is Inserted Successfully"

# ===========================================================
# 🏷️ INORDER TRAVERSAL — inOrderTraversal(index)
# ===========================================================

    def inOrderTraversal(self , index):
        r"""
        📘 InOrder Traversal (Array-Based Binary Tree)
        ==============================================

        Traverses the binary tree in the order:
             Left Subtree → Root → Right Subtree

        --------------------------------------------------------------------
        🧩 INTERNAL LOGIC
        --------------------------------------------------------------------
        Using array index math:
            Left child  = index * 2  
            Right child = index * 2 + 1

        Therefore InOrder becomes:
            1. Recur on left child  
            2. Visit node (root)  
            3. Recur on right child  

        --------------------------------------------------------------------
        ⛔ Base Condition:
        --------------------------------------------------------------------
        If index > lastUsedIndex → this node does not exist → stop recursion.

        --------------------------------------------------------------------
        📌 Example Output for Tree:
            [1, 2, 3, 4, 5, 6, 7]

        The InOrder result will be:
            4 → 2 → 5 → 1 → 6 → 3 → 7  

        Because it visits the tree as:
            Left → Root → Right
        --------------------------------------------------------------------
        """

        # Base case: stop if index exceeds used area of tree
        if index > self.lastUsedIndex:
            return 
        
        # Visit LEFT subtree
        self.inOrderTraversal(index * 2)

        # Visit ROOT
        print(self.customList[index])

        # Visit RIGHT subtree
        self.inOrderTraversal((index * 2) + 1)



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

print("\n📌 InOrder Traversal Output:")
newBT.inOrderTraversal(1)


r"""
=======================================================================
📤 Example Output
=======================================================================

The Node 1 is Inserted Successfully  
The Node 2 is Inserted Successfully  
The Node 3 is Inserted Successfully  
The Node 4 is Inserted Successfully  
The Node 5 is Inserted Successfully  
The Node 6 is Inserted Successfully  
The Node 7 is Inserted Successfully  

The Binary Tree Array -> ['1', '2', '3', '4', '5', '6', '7']

📌 InOrder Traversal Output:
4
2
5
1
6
3
7

=======================================================================
⏱ Time & Space Complexity
=======================================================================

🕒 Time Complexity:  
Traversal → **O(n)**  

📦 Space Complexity:  
Recursive Stack → **O(n)** in worst case  

=======================================================================
✅ Summary
=======================================================================

✔ Very simple InOrder traversal using array-indexing  
✔ No pointers required — all child nodes found using math  
✔ Produces natural sorted-like structure for complete binary trees  

Next Steps:
-----------
➡ PostOrder Traversal (Array Based)  

=======================================================================
"""
