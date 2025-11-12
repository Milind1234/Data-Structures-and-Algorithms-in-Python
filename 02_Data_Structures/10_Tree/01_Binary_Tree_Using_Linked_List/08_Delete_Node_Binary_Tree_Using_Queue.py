r"""
📘 Topic: Deletion in Binary Tree (Level Order / BFS Approach)
=============================================================

🎯 Purpose:
------------
To learn how to **delete a node** from a Binary Tree using **Level Order Traversal**.
Because a general binary tree has no BST ordering, we delete a node by:
  1) Finding the node to delete (by value),
  2) Finding the deepest (rightmost) node in the tree,
  3) Replacing the target node's data with the deepest node's data,
  4) Removing the deepest node.

This preserves the tree shape as a near-complete tree (fills top-to-bottom, left-to-right).

=======================================================================
🧠 Key Idea (Why this method?)
=======================================================================
- We cannot "shift" child pointers easily without changing structure.
- Replacing target node's data with deepest node's value and deleting the deepest node is
  a standard approach that keeps other subtrees intact.
- The deepest node is easy to find with a level-order traversal (BFS).

=======================================================================
⚠️ Important: Queue API assumption
=======================================================================
This note assumes your `QueueLinkedList.dequeue()` returns an object with a `.value` attribute:
- `q.dequeue()` → returns a queue-node like `{ value: TreeNode(...) }`
- Access tree node with `q.dequeue().value`
If your queue returns raw `TreeNode` objects instead, replace `root.value` with `root` in the code.
"""

# -----------------------------
# IMPORT CUSTOM QUEUE
# -----------------------------
import QueueLinkedList as queue  # your linked-list-based queue (as used previously)

# -----------------------------
# TREE NODE DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

# -----------------------------
# EXAMPLE TREE BUILD (for demo)
# -----------------------------
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

r"""
Initial Tree:

                 1
               /   \
             2       3
            / \     / \
           4   5   6   7
"""

# -----------------------------
# LEVEL-ORDER PRINTER (helper)
# -----------------------------
def levelOrderTraversal_LinkedList(rootnode):
    """
    Print tree nodes level by level using the custom queue.
    """
    if not rootnode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    while not customQueue.isEmpty():
        qnode = customQueue.dequeue()        # queue node wrapper
        node = qnode.value                   # actual TreeNode
        print(node.data)
        if node.leftchild is not None:
            customQueue.enqueue(node.leftchild)
        if node.rightchild is not None:
            customQueue.enqueue(node.rightchild)


# -----------------------------
# GET DEEPEST NODE
# -----------------------------
def getDeepestNode(rootnode):
    """
    Returns the deepest (rightmost in level order) TreeNode object.
    Uses level-order traversal to reach the last node visited.
    """
    if not rootnode:
        return None

    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)
    last = None

    while not customQueue.isEmpty():
        qnode = customQueue.dequeue()
        last = qnode.value
        # enqueue children for further traversal
        if last.leftchild is not None:
            customQueue.enqueue(last.leftchild)
        if last.rightchild is not None:
            customQueue.enqueue(last.rightchild)

    # 'last' now holds the deepest node
    return last


# -----------------------------
# DELETE DEEPEST NODE
# -----------------------------
def deleteDeepestNode(rootnode, deepest_node):
    """
    Deletes the deepest_node from the tree by scanning nodes level-order to find its parent
    and removing the proper child reference.
    Returns True if deleted, False otherwise.
    """
    if not rootnode or deepest_node is None:
        return False

    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    while not customQueue.isEmpty():
        qnode = customQueue.dequeue()
        node = qnode.value

        # If node's leftchild is the deepest node -> remove it
        if node.leftchild:
            if node.leftchild is deepest_node:
                node.leftchild = None
                return True
            else:
                customQueue.enqueue(node.leftchild)

        # If node's rightchild is the deepest node -> remove it
        if node.rightchild:
            if node.rightchild is deepest_node:
                node.rightchild = None
                return True
            else:
                customQueue.enqueue(node.rightchild)

    return False


# -----------------------------
# DELETE NODE (MAIN)
# -----------------------------
def deleteNodeBT(rootnode, delete_value):
    """
    Deletes the first node whose data == delete_value using the standard BFS-delete approach:
      1) Find the node to delete (target node)
      2) Find the deepest node
      3) Copy deepest node's data into the target node
      4) Delete the deepest node

    Returns a message about success/failure.
    """
    if not rootnode:
        return "Tree is empty"

    # 1) Find the node to delete using level-order search
    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    target_node = None
    while not customQueue.isEmpty():
        qnode = customQueue.dequeue()
        node = qnode.value
        if node.data == delete_value:
            target_node = node
            break
        if node.leftchild:
            customQueue.enqueue(node.leftchild)
        if node.rightchild:
            customQueue.enqueue(node.rightchild)

    if target_node is None:
        return f"❌ Node '{delete_value}' not found in the tree."

    # 2) Find deepest node
    deepest = getDeepestNode(rootnode)
    if deepest is None:
        return "Unexpected error: deepest node not found."

    # 3) Replace target node's data with deepest node's data
    target_node.data = deepest.data

    # 4) Delete the deepest node from the tree
    deleted = deleteDeepestNode(rootnode, deepest)
    if deleted:
        return f"✅ Node '{delete_value}' deleted (replaced with deepest node '{deepest.data}')."
    else:
        return "❌ Failed to delete deepest node."


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
"""
