r"""
📘 Topic: PreOrder Traversal in Binary Tree (Python List Representation)
=======================================================================

🎯 Purpose:
-----------
To understand how **PreOrder Traversal** works when a Binary Tree is implemented  
using a **Python List (Array representation)**.

This is different from linked-list trees, because here node relationships  
are determined **mathematically using index formulas**:

    Left Child Index  =  2 * i  
    Right Child Index =  2 * i + 1  

---

🌳 Example Tree (Stored Using Python List)
-----------------------------------------

                 1
               /   \
              2     3
             / \   / \
            4  5  6   7

Array Representation:

Index : 0   1   2   3   4   5   6   7
Value : [–, 1,  2,  3,  4,  5,  6,  7]

We start PreOrder from index **1** (root).

---

📘 PreOrder Traversal Rule (DFS - Depth First Search)
-----------------------------------------------------

PreOrder always visits nodes in this order:

1️⃣ **Root**  
2️⃣ **Left Subtree**  
3️⃣ **Right Subtree**

Flow:
Root → Left → Right

---

🧠 PreOrder (Array Version) — How It Works
------------------------------------------

When using a list-based binary tree:

- We don't follow pointers → We compute child indices.
- For any index `i`:
      left child  = 2 * i  
      right child = 2 * i + 1

Algorithm Steps for preOrderTraversal(i):

1️⃣ Process current node  
    → print(customList[i])

2️⃣ Recur on left subtree  
    → preOrderTraversal(2 * i)

3️⃣ Recur on right subtree  
    → preOrderTraversal(2 * i + 1)

Stopping Condition:
-------------------
If `index > lastUsedIndex`, the node does not exist → stop recursion.

This ensures we never go outside the valid tree area.

---

"""

# ===========================================================
# 🏷️ CLASS DEFINITION — BinaryTree (Array Based)
# ===========================================================

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxsize = size

    def __str__(self):
        return f"The Binary Tree Array -> {self.customList[1:self.lastUsedIndex+1]}"
    
# ===========================================================
# 🏷️ INSERT FUNCTION — insertNode(value)
# ===========================================================
    def insertNode(self , node_value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return "The Binary tree is Full"
        
        # Insert value in next free index
        self.customList[self.lastUsedIndex + 1] = node_value
        self.lastUsedIndex += 1
        return f"The Node {node_value} is Inserted Successfully"

# ===========================================================
# 🏷️ PREORDER TRAVERSAL — preOrderTraversal(index)
# ===========================================================
    def preOrderTraversal(self,index):
        r"""
        📘 PreOrder Traversal (Array-Based Binary Tree)
        ===============================================

        🎯 Purpose:
        -----------
        To visit nodes in the order:
            Root → Left → Right

        ----------------------------------------------------------------------------
        🧠 INTERNAL LOGIC (How This Function Works)
        ----------------------------------------------------------------------------
        When using array storage, each node is accessed by index:

            🔹 Node at index i
            🔹 Left child  = index * 2
            🔹 Right child = index * 2 + 1

        So PreOrder becomes:
            1. Visit index i   → print value
            2. Visit index*2   (left child)
            3. Visit index*2+1 (right child)

        ----------------------------------------------------------------------------
        ⛔ Base Condition (Stopping Rule)
        ----------------------------------------------------------------------------
        If index > lastUsedIndex:
            → Node does not exist
            → Stop recursion

        This prevents accessing invalid list positions.

        ----------------------------------------------------------------------------
        🌳 Example Output for Tree [1,2,3,4,5,6,7]
        ----------------------------------------------------------------------------
        1
        2
        4
        5
        3
        6
        7

        Which matches:  Root → Left → Right
        ----------------------------------------------------------------------------
        """
        
        # Base condition → Stop if current index exceeds valid tree range
        if index > self.lastUsedIndex:
            return 
        
        # Step 1: Visit ROOT node
        print(self.customList[index])
        
        # Step 2: Visit LEFT subtree
        self.preOrderTraversal(index * 2)
        
        # Step 3: Visit RIGHT subtree
        self.preOrderTraversal((index * 2) + 1)


# ===========================================================
# 🧪 TESTING THE TREE
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

print("\n📌 PreOrder Traversal Output:")
newBT.preOrderTraversal(1)

r"""
=======================================================================
📤 Expected Output:
=======================================================================

The Node 1 is Inserted Successfully
The Node 2 is Inserted Successfully
The Node 3 is Inserted Successfully
The Node 4 is Inserted Successfully
The Node 5 is Inserted Successfully
The Node 6 is Inserted Successfully
The Node 7 is Inserted Successfully

The Binary Tree Array -> ['1', '2', '3', '4', '5', '6', '7']

📌 PreOrder Traversal Output:
1
2
4
5
3
6
7

=======================================================================
⏱ Time & Space Complexity
=======================================================================

🕒 Time Complexity:  
PreOrder Traversal → **O(n)** (visits all nodes)

📦 Space Complexity:  
→ **O(n)** in worst case (recursive stack)

=======================================================================
✅ Summary
=======================================================================

✔ PreOrder visits values as Root → Left → Right  
✔ Very easy with array index math  
✔ No pointers, just arithmetic  
✔ Perfect for complete binary trees  

Next Steps:
-----------
➡ InOrder Traversal (Array Based)  
➡ PostOrder Traversal (Array Based)  

=======================================================================
"""
