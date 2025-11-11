"""
📘 Topic: Binary Tree — Creation using Linked List Representation
=================================================================

In previous Notes, we learned:
---------------------------------
➡️ What is a Binary Tree  
➡️ Why we need it  
➡️ How to represent it using:
     1️⃣ Linked List
     2️⃣ Python List (Array Representation)

Now, in this Note, we will focus on:
---------------------------------------
✅ Common Binary Tree Operations  
✅ Creating a Binary Tree using **Linked List Representation**

=================================================================
📗 Common Operations on a Binary Tree
=================================================================

A Binary Tree supports the following core operations:

1️⃣ **Creation** of a new tree  
2️⃣ **Insertion** of a node  
3️⃣ **Deletion** of a node  
4️⃣ **Searching** for a node  
5️⃣ **Traversal** of all nodes (4 types)  
6️⃣ **Deletion of entire tree**

🧠 Note:
---------
Traversal appears before insertion in this notes because insertion **uses traversal internally**.
So, to understand insertion, we must first understand traversal.

=================================================================
📘 1. Creation of a Binary Tree (Linked List Representation)
=================================================================

🎯 Concept:
------------
In Linked List representation, each node of the Binary Tree is implemented
as an object of a class. Each node contains three components:

    [ data | left_child | right_child ]

The `left_child` and `right_child` initially point to `None`
(since no child nodes exist when the root is first created).

=================================================================
📦 Implementation
=================================================================
"""

# -----------------------------
# CLASS DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        """
        📘 Constructor (__init__):
        -------------------------
        Initializes a single node in a Binary Tree.

        Parameters:
        -----------
        data : any
            The value stored in the node.

        Attributes:
        ------------
        self.data       → value stored in the node
        self.leftChild  → pointer/reference to left child (None initially)
        self.rightChild → pointer/reference to right child (None initially)

        Example:
        --------
        node = TreeNode("Drinks")

        Creates a single node containing:
        [ data = "Drinks", leftChild = None, rightChild = None ]
        """
        self.data = data
        self.leftChild = None
        self.rightChild = None


# -----------------------------
# CREATE A NEW BINARY TREE (Root Node)
# -----------------------------
newBinaryTree = TreeNode("Drinks")

"""
=================================================================
📊 Visualization
=================================================================

When we create a single node:

               [ None | Drinks | None ]

        Drinks
        /    \
    None      None

📘 Explanation:
---------------
✅ The "Drinks" node is created as the root node.
✅ Since no children exist yet:
   - LeftChild → None
   - RightChild → None
✅ This is the simplest possible Binary Tree — containing only one node.

=================================================================
🧩 How it Works (Step-by-Step)
=================================================================
1️⃣ Define the class `TreeNode` with attributes:
    - `data`       → stores the node's value
    - `leftChild`  → points to left subtree (initially None)
    - `rightChild` → points to right subtree (initially None)

2️⃣ Create an instance of `TreeNode`:
    newBinaryTree = TreeNode("Drinks")

3️⃣ A new object is allocated in memory with:
    data = "Drinks"
    leftChild = None
    rightChild = None

=================================================================
🕒 Time & Space Complexity
=================================================================
⏱️ Time Complexity:  O(1)
💾 Space Complexity: O(1)

📘 Reason:
----------
Only one node is created and initialized.
No recursion or traversal is performed.

=================================================================
📚 Key Takeaways
=================================================================
✅ Binary Tree node = [ data | left pointer | right pointer ]  
✅ Creation involves only one operation → initializing the root  
✅ All further insertions will connect additional nodes using `leftChild` and `rightChild`  
✅ Creation step forms the base of every Binary Tree program  

=================================================================
🧠 Next Steps
=================================================================
From the next Note, we will study:
   👉 Traversal of Binary Tree  
      (Preorder, Inorder, Postorder, Level Order)

Traversal is learned before insertion because:
➡️ Traversal logic is required to correctly position new nodes.
=================================================================
"""
