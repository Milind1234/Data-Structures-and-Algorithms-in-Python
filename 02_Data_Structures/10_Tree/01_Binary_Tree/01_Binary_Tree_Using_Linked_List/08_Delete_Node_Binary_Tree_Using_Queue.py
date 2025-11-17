"""
📘 Topic: Delete a Node in Binary Tree (Using Custom Queue - Linked List Queue)
===============================================================================

🎯 Purpose:
-----------
To delete a node from a **Binary Tree** (NOT BST) using **Level Order Traversal**.

Deletion requires three major operations:

1️⃣ Find the target node (value to delete).  
2️⃣ Find the **deepest node** (last node in Level Order).  
3️⃣ Copy deepest node → target node, then delete the deepest node.

This keeps the Binary Tree **complete and balanced**.

-------------------------------------------------------------------------------
🧠 Why this method?
-------------------------------------------------------------------------------
A binary tree fills from **left → right → next level**.
Deleting a node in the middle would leave a “hole”, breaking completeness.

✔ Replacing with the deepest node **keeps structure intact**  
✔ Exactly how heap deletion works  
-------------------------------------------------------------------------------
🌳 Visual Example
-------------------------------------------------------------------------------

Before deletion:
                1
              /   \
            2       3
           / \     / \
          4   5   6   7

Delete node = 3  
Deepest node = 7  
→ Replace 3 → 7  
→ Remove original deepest node (7)

After deletion:
                1
              /   \
            2       7
           / \     /
          4   5   6
-------------------------------------------------------------------------------
"""

import QueueLinkedList as queue  # Custom queue (Linked List based)


# ================================================================
# 📘 TreeNode Class — No changes made
# ================================================================
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# ================================================================
# 📘 Create Binary Tree (Your Structure - Unchanged)
# ================================================================
newBT = TreeNode("1")

leftchild = TreeNode("2")
rightchild = TreeNode("3")

newBT.leftchild = leftchild
newBT.rightchild = rightchild

N4 = TreeNode("4")
N5 = TreeNode("5")
leftchild.leftchild = N4
leftchild.rightchild = N5

N6 = TreeNode("6")
N7 = TreeNode("7")
rightchild.leftchild = N6
rightchild.rightchild = N7


# ================================================================
# 📘 LEVEL ORDER TRAVERSAL (Custom Queue)
# ================================================================
def levelOrderTraversal_LinkedList(rootnode):
    """
    🌲 LEVEL ORDER TRAVERSAL (Breadth-First Search)
    ==============================================
    Algorithm:
    ----------
    1️⃣ Create an empty queue.
    2️⃣ Enqueue the root node.
    3️⃣ While queue not empty:
        - Dequeue a node (front of queue)
        - Print its value
        - Enqueue left child (if exists)
        - Enqueue right child (if exists)

    Why BFS?
    --------
    - Helps us scan all nodes level-by-level.
    - Used to find deepest node & target node during deletion.
    """
    if not rootnode:
        return
    else:
        customQueue = queue.Queue()          # Step 1: Create queue
        customQueue.enqueue(rootnode)        # Step 2: Insert root

        print("\n🌲 Level Order Traversal:")

        while not(customQueue.isEmpty()):    # Step 3: BFS Loop
            root = customQueue.dequeue()     # Take first-in node
            print(" →", root.value.data)

            # Enqueue children (Left → Right)
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)

            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)



# ================================================================
# 📘 Get Deepest Node (Rightmost node in last level)
# ================================================================
def getDeepestNode(rootnode):
    """
    🔍 GET DEEPEST NODE
    ====================
    Purpose:
    --------
    The deepest node is the **last node visited** during BFS.

    Algorithm:
    ----------
    1️⃣ Initialize queue with root.
    2️⃣ Perform Level Order traversal.
    3️⃣ The final popped node = deepest node.
    4️⃣ Return that node.

    Why deepest node?
    ------------------
    This node will replace the target node’s value
    to maintain tree completeness.
    """
    if not rootnode:
        return "Tree is Empty"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)

        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()

            # Continue BFS until last node
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)

            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)

        deepestNode = root.value
        return deepestNode   # Last visited node



# ================================================================
# 📘 Delete Deepest Node From the Tree
# ================================================================
def deleteDeepestNode(rootnode, deepest_node):
    """
    ❌ DELETE DEEPEST NODE
    =======================
    Purpose:
    --------
    Delete the physical deepest node from the tree.

    Algorithm:
    ----------
    1️⃣ Run BFS using queue.
    2️⃣ For each node:
        - If node == deepest_node → delete it (root.value = None)
        - If node.leftchild == deepest_node → remove link
        - If node.rightchild == deepest_node → remove link
    3️⃣ Stop after deleting.

    Why delete separately?
    -----------------------
    After copying deepest node data into target node,
    we must remove deepest node to avoid duplicates.
    """
    if not rootnode:
        return 
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            # CASE 1: Node itself is deepest node
            if root.value is deepest_node:
                root.value = None
                return 

            # CASE 2: Deepest node is RIGHT CHILD
            if root.value.rightchild:
                if root.value.rightchild is deepest_node:
                    root.value.rightchild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightchild)

            # CASE 3: Deepest node is LEFT CHILD
            if root.value.leftchild:
                if root.value.leftchild is deepest_node:
                    root.value.leftchild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftchild)



# ================================================================
# 📘 DELETE NODE BY VALUE (Main Function)
# ================================================================
def deleteNodeBT(rootnode, delete_node):
    """
    🪓 DELETE NODE BY VALUE (Main Function)
    ======================================

    Steps:
    ------
    1️⃣ Perform BFS to locate the target node:
         - root.value.data == delete_node

    2️⃣ Retrieve deepest node using getDeepestNode()

    3️⃣ Replace target node’s value with deepest node’s value

    4️⃣ Call deleteDeepestNode() to remove deepest node

    Why this works:
    ----------------
    - Guaranteed to preserve binary tree structure.
    - Avoids "holes" that break completeness.
    """
    if not rootnode:
        return "Empty Tree"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            # 🎯 STEP 1: Target found
            if root.value.data == delete_node:
                deepestnode = getDeepestNode(rootnode)  # STEP 2
                root.value.data = deepestnode.data      # STEP 3
                deleteDeepestNode(rootnode, deepestnode) # STEP 4
                return f"🎉 Node '{delete_node}' deleted successfully!"

            # Continue BFS
            if (root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)

            if (root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)

        return "❌ Failed to delete – Node not found!"


# -----------------------------
# DEMONSTRATION
# -----------------------------
print("\n=== BEFORE DELETION ===")
levelOrderTraversal_LinkedList(newBT)

# delete node '3' (as in your example)
print("\n=> Deleting node '3' ...")
print(deleteNodeBT(newBT, "3"))

print("\n=== AFTER DELETION ===")
levelOrderTraversal_LinkedList(newBT)

r"""
Expected sequence (one valid outcome):

Before deletion:
1
2
3
4
5
6
7

Deleting node '3':
- find node with data '3' (node at level 2, right child of 1)
- deepest node is '7'
- copy deepest.data into target node -> node 3.data = '7'
- delete deepest node (remove node 7)

After deletion (level-order):
1
2
7   # replaced 3 with deepest node's data
4
5
6

Notes:
- The deepest node (7) is removed; the target location now contains the deepest node's original value.
- If there are multiple nodes with the same data value, this deletes the first one encountered in level order.
"""

# -----------------------------
# COMPLEXITY & NOTES
# -----------------------------
r"""
Time Complexity:
 - getDeepestNode: O(n)
 - deleteDeepestNode: O(n)
 - deleteNodeBT (combined): O(n) overall (each node visited a constant number of times)

Space Complexity:
 - O(n) due to the queue storing nodes of a level (worst-case).

Edge Cases & Behaviour:
 - If tree is empty → function returns "Tree is empty".
 - If delete_value not found → returns "Node ... not found".
 - If the tree has only one node (root) and it's the node to delete:
     - getDeepestNode returns root; deleteDeepestNode will not find a parent to unlink.
     - In this simplistic implementation the root still contains a value. If you want to
       support removing the single-node tree (set root to None), you should return the new root
       from deleteNodeBT (or wrap root in a mutable container). For lecture simplicity we keep
       this demonstration focused on the common multi-node case.
 - Queue API assumption: if your queue's dequeue returns raw TreeNode objects (not wrappers),
   replace `qnode = customQueue.dequeue(); node = qnode.value` with `node = customQueue.dequeue()`.

Suggested Improvement:
 - Return the new root from deleteNodeBT to support deleting the root node in single-node trees.
 - Provide a deque-based version (below) for simpler production-ready code.

 
=======================================================================
🔵 FULL ALGORITHM FLOWCHART (deleteNodeBT)
=======================================================================

                ┌──────────────────────────────┐
                │       Start deleteNodeBT      │
                └───────────────┬──────────────┘
                                │
                                ▼
                    ┌──────────────────────┐
                    │ Is rootnode None ?   │
                    └───────┬──────────────┘
                            │Yes
                            ▼
                   Return "Empty Tree"
                            │
                            │No
                            ▼
                ┌──────────────────────────────┐
                │ Create queue & enqueue root  │
                └───────────────┬──────────────┘
                                │
                                ▼
                   ┌─────────────────────────┐
                   │ While queue NOT empty   │
                   └───────────┬─────────────┘
                               │
                               ▼
                     Dequeue current = root
                               │
                               ▼
         ┌─────────────────────────────────────────────────┐
         │ Does root.value.data == delete_node ?           │
         └──────────────┬──────────────────────────────────┘
                        │Yes
                        ▼
          ┌────────────────────────────────────────────┐
          │ deepest = getDeepestNode(rootnode)         │
          │ root.value.data = deepest.data             │
          │ deleteDeepestNode(rootnode, deepest)       │
          └───────────────────────┬────────────────────┘
                                  ▼
                     Return "Node deleted successfully"
                                  │
                                  └────────────────────────

                        No
                        │
                        ▼
               Enqueue left child (if exists)
                        │
                        ▼
               Enqueue right child (if exists)
                        │
                        ▼
                 Continue loop until queue empty

            ┌────────────────────────────┐
            │ Node not found → return ❌ │
            └────────────────────────────┘


=======================================================================
🟩 ASCII STEP-BY-STEP EXPLANATION
=======================================================================

Before Deletion:
----------------
            1
          /   \
        2       3
       / \     / \
      4   5   6   7

Searching for node '3' using BFS:
Queue movement:
[1]
[2, 3]
[3, 4, 5] → FOUND 3 ✔

Finding Deepest Node:
Queue:
[1]
[2, 3]
[4, 5, 6, 7] → deepest = 7

Replacing:
Node 3.data = 7

Deleting deepest node (7):
Tree becomes:

            1
          /   \
        2       7
       / \     /
      4   5   6

 
 
 """
