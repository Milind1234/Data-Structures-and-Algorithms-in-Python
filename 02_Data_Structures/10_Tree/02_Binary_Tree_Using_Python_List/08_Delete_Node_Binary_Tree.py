r"""
📘 Topic: Delete Node in Binary Tree (Python List Representation)
=================================================================

🎯 Purpose:
-----------
To understand how to **delete a node** from a Binary Tree that is stored  
in a **Python List (array-based representation)**.

Array-based binary trees allow **O(1)** index access, making deletion easier:
We simply replace the target node with the **last node** in the tree  
and then remove the last node.

This ensures the tree remains a **Complete Binary Tree**.

=====================================================================
🌳 Binary Tree Structure (List Representation)
=====================================================================

Binary Tree stored like this:

Index:    0    1    2    3    4    5    6    7
Value:   [– ,  1,   2,   3,   4,   5,   6,   7]

Parent-Child relations:
- Left child  = 2 * i  
- Right child = 2 * i + 1  

Since list already stores nodes **level-wise**, deletion only needs index updates.

=====================================================================
🧠 deleteNodeBT() — Algorithm Logic
=====================================================================

We delete by following **3 simple steps**:

1️⃣ **Search for the node** with given value  
    - Loop through list from index 1 → lastUsedIndex  

2️⃣ When found, **replace it with the last node** in the tree  
    - customList[i] = customList[lastUsedIndex]

3️⃣ **Delete last node** and reduce lastUsedIndex  
    - customList[lastUsedIndex] = None  
    - lastUsedIndex -= 1  

This ensures:
✔ Tree remains complete  
✔ No holes inside the list  
✔ Efficient deletion without shifting elements  

=====================================================================
💡 Example
=====================================================================

Tree:
        1
      /   \
     2     3
    / \   / \
   4  5  6   7

Array: [None, 1, 2, 3, 4, 5, 6, 7]

Delete "3":

- Last node = 7
- Replace index of "3" with "7"
- Remove last element

Resulting tree:

        1
      /   \
     2     7
    / \   /
   4  5  6

Array becomes:
[None, 1, 2, 7, 4, 5, 6]

=====================================================================
💻 Python Code (Your Code With Added Explanations)
=====================================================================
"""

# ===================================================================
# 🏷️ CLASS DEFINITION — Binary Tree (Array-Based Implementation)
# ===================================================================

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]        # Fixed-size list
        self.lastUsedIndex = 0                 # Tracks last filled index
        self.maxsize = size                    # Maximum capacity

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

# ===================================================================
# 🏷️ DELETE NODE — deleteNodeBT(delete_value)
# ===================================================================

    def deleteNodeBT(self , delete_value):
        r"""
        📘 deleteNodeBT(delete_value)
        ==============================

        🎯 Purpose:
        -----------
        Delete a node from the Binary Tree (array-based)  
        **by replacing it with the last node**.

        ------------------------------------------------------------
        🧠 HOW IT WORKS (Algorithm)
        ------------------------------------------------------------

        1️⃣ Check if the tree is empty  
             if lastUsedIndex == 0 → nothing to delete

        2️⃣ Scan list from index 1 → lastUsedIndex  
             if customList[i] == delete_value → FOUND

        3️⃣ Replace found node with last node  
             customList[i] = customList[lastUsedIndex]

        4️⃣ Remove last node and update lastUsedIndex  
             customList[lastUsedIndex] = None  
             lastUsedIndex -= 1

        ------------------------------------------------------------
        🧩 Visualization
        ------------------------------------------------------------

        Delete: 3  
        List: [1,2,3,4,5,6,7]

        Last node = 7  
        Replace index-of(3) with 7  
        Remove final 7  

        Result:
        [1,2,7,4,5,6]

        ------------------------------------------------------------
        ⏱ Complexity
        ------------------------------------------------------------
        Time   → O(n)   (search in array)  
        Space  → O(1)

        ------------------------------------------------------------
        """
        if self.lastUsedIndex == 0:
            return "There is no node to delete"

        for i in range(1,self.lastUsedIndex+1):

            # 🎯 Found the node to delete
            if self.customList[i] == delete_value:

                # Replace with last node
                self.customList[i] = self.customList[self.lastUsedIndex]

                # Delete last node
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1

                return f"The Node {delete_value} has been successfully deleted"


# ===================================================================
# 🧪 TESTING THE OPERATIONS
# ===================================================================

newBT = BinaryTree(9)

print(newBT.insertNode("1"))
print(newBT.insertNode("2"))
print(newBT.insertNode("3"))
print(newBT.insertNode("4"))
print(newBT.insertNode("5"))
print(newBT.insertNode("6"))
print(newBT.insertNode("7"))

print(newBT)

print("\n🪓 Deleting Node '3':")
print(newBT.deleteNodeBT("3"))

print("\n🌳 Tree After Deletion:")
newBT.levelOrderTraversal(1)

r"""
=====================================================================
📤 Example Output
=====================================================================

The Node 1 is Inserted Successfully  
The Node 2 is Inserted Successfully  
The Node 3 is Inserted Successfully  
The Node 4 is Inserted Successfully  
The Node 5 is Inserted Successfully  
The Node 6 is Inserted Successfully  
The Node 7 is Inserted Successfully  

The Binary Tree Array -> ['1', '2', '3', '4', '5', '6', '7']

🪓 Deleting Node '3':
The Node 3 has been successfully deleted

🌳 Tree After Deletion:
1  
2  
7  
4  
5  
6  

=====================================================================
✅ Summary
=====================================================================

✔ Deletion replaces the deleted node with **deepest node**  
✔ Ensures the tree remains **complete**  
✔ Very efficient for array-based binary trees  
✔ Time Complexity → O(n) (search)  
✔ Space Complexity → O(1)

=====================================================================
Next:
-----
➡ Delete Entire Binary Tree  
➡ Search Operation  
➡ Traversals (Inorder / Preorder / Postorder)

=====================================================================
"""
