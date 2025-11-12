r"""
📘 Topic: Deletion in Binary Tree (Level Order Traversal using deque)
====================================================================

🎯 Purpose:
------------
To understand how to **delete a node** from a Binary Tree using **Level Order Traversal**
(BFS approach) with Python’s `collections.deque`.

Unlike a Binary Search Tree (BST), a **Binary Tree** does not maintain a sorted structure.
Therefore, we cannot directly find or remove a node based on ordering.
Instead, we use **Level Order Traversal (Breadth-First Search)**.

====================================================================
🧠 Key Idea — BFS-based Deletion
====================================================================
Deletion happens in **three main steps:**

1️⃣ **Find the node** with the given value (to delete).  
2️⃣ **Find the deepest (rightmost) node** in the tree.  
3️⃣ **Replace the target node’s data** with the deepest node’s data  
    and **delete the deepest node** from the tree.

This method keeps the tree **structure balanced** and maintains completeness
(top to bottom, left to right).

====================================================================
🌳 Example Binary Tree
====================================================================

Before Deletion:
----------------
             1
           /   \
         2       3
        / \     / \
       4   5   6   7

Delete Node = 3  
→ Deepest Node = 7  
→ Replace (3 → 7)  
→ Delete Node 7

After Deletion:
---------------
             1
           /   \
         2       7
        / \     /
       4   5   6

====================================================================
💡 Algorithm Logic
====================================================================

Step 1️⃣ → Start from root.  
Step 2️⃣ → Traverse Level Order using a queue:
             - Keep track of each node.
Step 3️⃣ → When you find the node to delete, store its reference.
Step 4️⃣ → Continue traversal until the last node (deepest node).
Step 5️⃣ → Replace the target node’s value with deepest node’s data.
Step 6️⃣ → Delete the deepest node from the tree.

====================================================================
💻 Python Implementation
====================================================================
"""

from collections import deque

# ---------------------------------------
# BINARY TREE NODE
# ---------------------------------------
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# ---------------------------------------
# LEVEL ORDER TRAVERSAL (Helper Function)
# ---------------------------------------
def levelOrderTraversal(rootnode):
    """
    📘 Function: levelOrderTraversal(rootnode)
    ------------------------------------------
    Traverses the binary tree in Level Order (Breadth-First Search)
    and prints each node's data.

    Logic:
    -------
    - Initialize deque with the root node.
    - Pop one node at a time.
    - Print its value.
    - Enqueue its children (left → right).
    """
    if not rootnode:
        print("🌳 Tree is empty")
        return

    queue = deque([rootnode])

    while queue:
        root = queue.popleft()
        print(root.data)

        if root.leftchild:
            queue.append(root.leftchild)
        if root.rightchild:
            queue.append(root.rightchild)


# ---------------------------------------
# GET DEEPEST NODE
# ---------------------------------------
def getDeepestNode(rootnode):
    """
    📘 Function: getDeepestNode(rootnode)
    -------------------------------------
    Returns the **deepest (rightmost)** node in the binary tree.

    Logic:
    -------
    - Perform Level Order traversal.
    - The last node visited will be the deepest node.
    """
    if not rootnode:
        return None

    queue = deque([rootnode])
    while queue:
        root = queue.popleft()
        if root.leftchild:
            queue.append(root.leftchild)
        if root.rightchild:
            queue.append(root.rightchild)
    return root  # Last visited node


# ---------------------------------------
# DELETE DEEPEST NODE
# ---------------------------------------
def deleteDeepestNode(rootnode, deepest_node):
    """
    📘 Function: deleteDeepestNode(rootnode, deepest_node)
    -----------------------------------------------------
    Deletes the given **deepest node** from the tree.

    Logic:
    -------
    - Traverse tree using BFS.
    - When a node’s left or right child matches the deepest node:
        → Remove the reference.
    """
    if not rootnode:
        return

    queue = deque([rootnode])
    while queue:
        root = queue.popleft()

        # If current node IS the deepest node (edge case)
        if root is deepest_node:
            root = None
            return

        # Check right child
        if root.rightchild:
            if root.rightchild is deepest_node:
                root.rightchild = None
                return
            else:
                queue.append(root.rightchild)

        # Check left child
        if root.leftchild:
            if root.leftchild is deepest_node:
                root.leftchild = None
                return
            else:
                queue.append(root.leftchild)


# ---------------------------------------
# DELETE NODE BY VALUE
# ---------------------------------------
def deleteNodeBT(rootnode, delete_value):
    """
    📘 Function: deleteNodeBT(rootnode, delete_value)
    ------------------------------------------------
    Deletes a node from the Binary Tree using Level Order traversal.

    Logic:
    -------
    1️⃣ Traverse the tree (BFS) until the target node is found.
    2️⃣ Find the deepest node.
    3️⃣ Copy deepest node's data into the target node.
    4️⃣ Delete the deepest node from the tree.
    """
    if not rootnode:
        return "🌳 Tree is empty"

    queue = deque([rootnode])
    while queue:
        root = queue.popleft()

        # Check if this node matches the target value
        if root.data == delete_value:
            deepest_node = getDeepestNode(rootnode)
            root.data = deepest_node.data
            deleteDeepestNode(rootnode, deepest_node)
            return f"✅ Node '{delete_value}' deleted successfully"

        if root.leftchild:
            queue.append(root.leftchild)
        if root.rightchild:
            queue.append(root.rightchild)

    return f"❌ Node '{delete_value}' not found"


# ---------------------------------------
# SAMPLE TREE CREATION
# ---------------------------------------
newBT = TreeNode("1")
newBT.leftchild = TreeNode("2")
newBT.rightchild = TreeNode("3")
newBT.leftchild.leftchild = TreeNode("4")
newBT.leftchild.rightchild = TreeNode("5")
newBT.rightchild.leftchild = TreeNode("6")
newBT.rightchild.rightchild = TreeNode("7")

r"""
Initial Tree (Before Deletion):

             1
           /   \
         2       3
        / \     / \
       4   5   6   7
"""

# ---------------------------------------
# TEST OPERATIONS
# ---------------------------------------
print("🌲 Original Tree:")
levelOrderTraversal(newBT)

print("\n🪓 Deleting Node '3'...")
print(deleteNodeBT(newBT, "3"))

print("\n🌿 Tree After Deletion:")
levelOrderTraversal(newBT)


r"""
====================================================================
📤 Example Output:
====================================================================

🌲 Original Tree:
1
2
3
4
5
6
7

🪓 Deleting Node '3'...
✅ Node '3' deleted successfully

🌿 Tree After Deletion:
1
2
7
4
5
6

====================================================================
⚙️ Step-by-Step Working:
====================================================================

1️⃣ Target Node = 3  
2️⃣ Deepest Node = 7  
3️⃣ Replace data → Node(3).data = '7'  
4️⃣ Delete deepest node → remove 7

Result:
1
2
7
4
5
6

====================================================================
🧩 Time & Space Complexity
====================================================================

📈 Time Complexity: O(n)
------------------------
- Each node is visited at most once during BFS traversal.

📊 Space Complexity: O(n)
-------------------------
- Queue can hold all nodes of a level in worst case.

====================================================================
✅ Summary
====================================================================

✔ Uses **Level Order Traversal (BFS)**  
✔ Replaces node’s value with **deepest node’s value**  
✔ Maintains tree’s **shape (completeness)**  
✔ Time Complexity → O(n)  
✔ Space Complexity → O(n)

====================================================================
📘 Next Steps:
--------------
➡️ Next, we will learn **Delete Entire Binary Tree** 
   and **Traversal combinations with recursion & queues**.
====================================================================
"""
