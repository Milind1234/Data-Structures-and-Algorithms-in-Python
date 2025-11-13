r"""
📘 Topic: Level Order Traversal in Binary Tree (Python List Representation)
==========================================================================

🎯 Purpose:
-----------
To understand how **Level Order Traversal (Breadth-First Traversal)** works  
in a Binary Tree stored inside a **Python List (array-based implementation)**.

Unlike linked-list binary trees (which need a Queue),  
array-based trees can perform LevelOrder traversal **directly**  
because the elements are **already stored level by level**.

=======================================================================
🌳 Binary Tree Representation Using Python List
=======================================================================

We store the binary tree in a Python list where:

- Index 1 → Root
- Index 2 → Left child of root
- Index 3 → Right child of root
- Index 4 → Left child of node at index 2
- ...

Example Tree:

                1
             /     \
           2         3
         /  \      /  \
        4    5    6    7

Stored as:

Index:   0   1   2   3   4   5   6   7
Value:  [–,  1,  2,  3,  4,  5,  6,  7]

Since nodes are stored **in level order**, traversal becomes very easy:
→ Just loop from index 1 to lastUsedIndex.

=======================================================================
🧠 Level Order Traversal — Core Idea
=======================================================================

Level Order Traversal (BFS):

     Visit nodes level by level  
     LEFT ➜ RIGHT for each level

In array-based tree:
- The list indices already guarantee this order.
- So LevelOrder = simply print elements from 1 → lastUsedIndex.

=======================================================================
💡 Algorithm (Simple & Efficient)
=======================================================================

FUNCTION levelOrderTraversal(startIndex):

1️⃣ Loop i from startIndex → lastUsedIndex  
2️⃣ Print customList[i]  
3️⃣ (Done)

No recursion required  
No queue required  
Time complexity O(n)

=======================================================================
💻 Python Code (Your Code With Explanations)
=======================================================================
"""

# ===========================================================
# 🏷️ CLASS DEFINITION — BinaryTree (Array-Based)
# ===========================================================

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]     # Fixed-size array
        self.lastUsedIndex = 0              # Tracks last node
        self.maxsize = size                 # Maximum capacity

    def __str__(self):
        # Pretty-print only the used portion of the list
        return f"The Binary Tree Array -> {self.customList[1:self.lastUsedIndex+1]}"
    
    def insertNode(self , node_value):
        # Check if array is full
        if self.lastUsedIndex + 1 == self.maxsize:
            return " The Binary tree is Full"

        # Insert at next available position
        self.customList[self.lastUsedIndex + 1 ] = node_value
        self.lastUsedIndex += 1

        return f"The Node {node_value} is Inserted Successfully"
    
# ===========================================================
# 🏷️ LEVEL ORDER TRAVERSAL — levelOrderTraversal(index)
# ===========================================================

    def levelOrderTraversal(self , index):
        r"""
        📘 Level Order Traversal (Array-Based Binary Tree)
        ==================================================

        🎯 Goal:
        --------
        Print all nodes **level by level**, starting from the root.

        ------------------------------------------------------------
        🧠 Why it's so simple here?
        ------------------------------------------------------------
        Because the binary tree is stored **in level order** inside the list.

        Example:
            Tree: 1, 2, 3, 4, 5, 6, 7
            Array: [None, 1, 2, 3, 4, 5, 6, 7]

        The list itself already maintains:
            Level 1 → 1  
            Level 2 → 2, 3  
            Level 3 → 4, 5, 6, 7  

        So traversal = just print the array from 1 → lastUsedIndex.

        ------------------------------------------------------------
        🧩 Algorithm:
        ------------------------------------------------------------
        FOR i from `index` TO `lastUsedIndex`:
             print customList[i]

        ------------------------------------------------------------
        ⏱ Time Complexity:
        ------------------------------------------------------------
        O(n) — every node printed once

        ------------------------------------------------------------
        📌 Example Output for Tree [1..7]:
        ------------------------------------------------------------
        1
        2
        3
        4
        5
        6
        7
        """
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])


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

print("\n📌 Level Order Traversal Output:")
newBT.levelOrderTraversal(1)


r"""
=======================================================================
📤 Example Output:
=======================================================================
The Node 1 is Inserted Successfully  
The Node 2 is Inserted Successfully  
The Node 3 is Inserted Successfully  
The Node 4 is Inserted Successfully  
The Node 5 is Inserted Successfully  
The Node 6 is Inserted Successfully  
The Node 7 is Inserted Successfully  

The Binary Tree Array -> ['1', '2', '3', '4', '5', '6', '7']

📌 Level Order Traversal Output:
1  
2  
3  
4  
5  
6  
7  

=======================================================================
✅ Summary
=======================================================================
✔ Level Order = Straightforward list printing  
✔ No queue needed  
✔ Very efficient in array-based trees  
✔ Perfect for complete binary trees  

Next Steps:
-----------
➡ Search in array-based Binary Tree  
➡ Deletion from array-based Binary Tree  
=======================================================================
"""
