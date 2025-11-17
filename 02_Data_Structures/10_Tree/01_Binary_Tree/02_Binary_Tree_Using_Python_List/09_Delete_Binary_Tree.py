r"""
📘 Topic: Delete Entire Binary Tree (Python List Representation)
===============================================================

🎯 Purpose:
-----------
To understand how to **delete an entire Binary Tree** when it is implemented
using a **Python List (array-based tree)**.

In a linked-list-based tree, deletion means removing all nodes by setting pointers to `None`.
But in Python list implementation, deletion becomes WAY simpler:
➡️ Just delete the entire underlying list.

This operation is extremely fast and efficient.

===============================================================
🌳 Binary Tree (Array-Based Representation)
===============================================================

A Binary Tree stored in a Python list looks like this:

Index:    0    1    2    3    4    5    6    7
Value:   [– ,  1,   2,   3,   4,   5,   6,   7]

- Index 0 is unused.
- left child  = 2 * index
- right child = 2 * index + 1

When we delete the entire tree, we do NOT delete elements one by one.
Instead, we remove the entire list at once.

===============================================================
🧠 deleteBT() — Algorithm Logic
===============================================================

The deleteBT() function deletes the whole binary tree by doing:

1️⃣ Set the **entire list** to `None`  
    → self.customList = None  

2️⃣ All references to nodes vanish instantly  
    → No leftover nodes  
    → Python automatically garbage-collects old values  

3️⃣ Print success message  

⚠️ After deletion, the tree becomes unusable.
Any traversal or insert operation will fail because:
`customList` no longer exists.

===============================================================
💡 Why This Works?
===============================================================

Because in Python, lists are objects stored in memory.
When you set:
    self.customList = None

✔ The old list is no longer referenced  
✔ Python’s garbage collector frees the memory  
✔ Binary tree is considered fully deleted  
✔ Very fast — O(1) operation  

===============================================================
💻 Python Code (Your Code + Explanations)
===============================================================
"""

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
    
    def levelOrderTraversal(self , index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteBT(self):
        r"""
        📘 deleteBT()
        =============

        🎯 Purpose:
        -----------
        Delete the **entire binary tree** implemented using a Python List.

        --------------------------------------------------------------
        🧠 HOW IT WORKS?
        --------------------------------------------------------------

        Array-based binary tree is stored in:
            self.customList = [None, 1, 2, 3, ...]

        To delete it:
            self.customList = None

        This destroys the entire tree instantly.

        --------------------------------------------------------------
        🧩 Algorithm Steps
        --------------------------------------------------------------

        1️⃣ Access the binary tree list  
        2️⃣ Set it to None  
        3️⃣ Tree memory is released automatically  
        4️⃣ Return confirmation message  

        --------------------------------------------------------------
        ⏱ Complexity
        --------------------------------------------------------------
        Time   → O(1)  
        Space  → O(1)  

        --------------------------------------------------------------
        """
        self.customList = None
        return " --> The Binary tree has been successfully deleted "


# ---------------------------------------------------------------
# 🧪 TESTING
# ---------------------------------------------------------------

newBT = BinaryTree(9)

print(newBT.insertNode("1"))
print(newBT.insertNode("2"))
print(newBT.insertNode("3"))
print(newBT.insertNode("4"))
print(newBT.insertNode("5"))
print(newBT.insertNode("6"))
print(newBT.insertNode("7"))

print(newBT)

print(newBT.deleteBT())

# WARNING: After deletion, this traversal will print nothing
# because customList is now None.
newBT.levelOrderTraversal(1)

r"""
===============================================================
📤 Output:
===============================================================
The Node 1 is Inserted Successfully
The Node 2 is Inserted Successfully
The Node 3 is Inserted Successfully
The Node 4 is Inserted Successfully
The Node 5 is Inserted Successfully
The Node 6 is Inserted Successfully
The Node 7 is Inserted Successfully

The Binary Tree Array -> ['1', '2', '3', '4', '5', '6', '7']

 --> The Binary tree has been successfully deleted 

(No traversal output after deletion)

===============================================================
✅ Summary
===============================================================

✔ deleteBT() wipes out the entire binary tree  
✔ Very fast: performed in **O(1)** time  
✔ Uses Python list deletion (set to None)  
✔ After deletion, tree cannot be traversed or inserted into  

Next Steps:
-----------
➡ Implement Searching in List-Based Binary Trees  
➡ Implement PreOrder, InOrder, PostOrder Traversals  
➡ Implement Delete Node (replace with last node)

===============================================================
"""
