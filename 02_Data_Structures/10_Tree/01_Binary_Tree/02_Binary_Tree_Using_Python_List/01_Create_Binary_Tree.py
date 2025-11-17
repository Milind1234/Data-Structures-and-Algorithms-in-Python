r"""
📘 Topic: Creating a Binary Tree Using Python List (Array Representation)
========================================================================

🎯 Purpose:
-----------
To learn how to **represent and create** a Binary Tree using a **Python list**  
instead of using nodes and linked references.

This method is also known as **Array Representation of Binary Tree** and is
commonly used for **Complete Binary Trees** (like heaps).


=======================================================================
🌳 How Binary Tree is Stored in a Python List
=======================================================================

We use a simple **mathematical relationship** to store nodes:

If a node is stored at index `i`, then:

    LEFT CHILD  →  2 * i  
    RIGHT CHILD →  2 * i + 1

Example Tree:
-------------
                N1
              /    \
            N2      N3
           / \     / \
         N4  N5  N6  N7

Array Representation:
---------------------

Index:   0    1    2    3    4    5    6    7
Value:  [x,  N1,  N2,  N3,  N4,  N5,  N6,  N7]

⚠️ We keep index 0 empty intentionally!
This simplifies child/parent calculations.


=======================================================================
🧠 Why Do We Leave Index 0 Empty?
=======================================================================

Because calculations become extremely easy:

- Left child of index `i`   → `2*i`
- Right child of index `i`  → `2*i + 1`
- Parent of index `i`       → `i//2`

This avoids off-by-one errors and makes tree navigation simple.


=======================================================================
🧱 BinaryTree Class Structure
=======================================================================

We store three things:

1️⃣ **customList** → The Python list (fixed size, initially filled with None)  
2️⃣ **lastUsedIndex** → Tracks the last filled index in the list  
3️⃣ **maxSize** → Maximum size of the array (tree capacity)

Purpose of `lastUsedIndex`:
---------------------------
This tells us **where the next node should be inserted**.
We always insert in the next available cell to keep tree *complete*.


=======================================================================
💻 Python Implementation
=======================================================================
"""

class BinaryTree:
    def __init__(self, size):
        """
        📘 Constructor (__init__):
        -------------------------
        Creates a binary tree using a fixed-size Python list.

        Parameters:
        -----------
        size : int
            Maximum number of elements the binary tree can store.

        What We Initialize:
        -------------------
        - customList → A list of given size filled with None.
        - lastUsedIndex → 0 (we skip index 0)
        - maxSize → size
        """
        self.customList = size * [None]  # Fixed-size array
        self.lastUsedIndex = 0           # Index 0 is unused
        self.maxSize = size              # Capacity of tree

newBT = BinaryTree(8)
"""
=======================================================================
📤 Usage Example
=======================================================================

# Create a binary tree of size 8
newBT = BinaryTree(8)

This will internally create:

Index: 0  1  2  3  4  5  6  7
Value: [None, None, None, None, None, None, None, None]

Nothing printed yet because creation only initializes structure.


=======================================================================
📈 Time & Space Complexity
=======================================================================

⏱ Time Complexity:
-------------------
O(1)
- Only initializes variables and a list.

💾 Space Complexity:
--------------------
O(n)
- A list of size `n` is created.


=======================================================================
✅ Summary
=======================================================================

✔ This representation stores a complete binary tree efficiently  
✔ Left/Right children can be accessed using simple formulas  
✔ Creation takes constant time  
✔ Uses fixed-size Python list  
✔ Ideal for heaps & complete binary trees  

=======================================================================
📘 Next Steps:
--------------
➡️ Next note: **Insertion into Binary Tree using Python List**  
=======================================================================
"""
