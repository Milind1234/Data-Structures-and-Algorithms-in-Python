"""
===============================================================================
📘 deleteAVL.py — Delete Entire AVL Tree (Notes + Safe Implementation)
===============================================================================

Purpose
-------
This short note explains two ways of "deleting" an entire AVL tree:
  1) The version you provided (sets rootnode.data = None and children = None)
     - This leaves a "dummy node" (an object with data None). The tree object
       still exists in memory, and levelOrderTraversal will still see a node.
  2) A recommended version that **returns None** so the caller can drop the
     root reference, allowing Python's garbage collector to reclaim the nodes.

Contents
--------
 - The original deleteAVL behavior (explained & shown)
 - Why it's problematic / what the side-effects are
 - Recommended deleteAVL implementation (delete by dropping root reference)
 - Example usage using your insertion sequence
 - Complexity summary and practical notes
===============================================================================
"""

from collections import deque

# ----------------------------
# Reproduced AVLNode & helpers (unchanged)
# ----------------------------
class AVLNode:
    def __init__(self , data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1

def levelOrderTraversal(rootnode):
    """
    Breadth-first traversal printing node.data in visit order.
    Kept exactly like your original function.
    """
    if not rootnode:
        return "Tree is Empty"
    queue = deque([rootnode])
    while queue:
        root = queue.popleft()
        print(root.data)

        if root.leftchild:
            queue.append(root.leftchild)
        if root.rightchild:
            queue.append(root.rightchild)

def getHeight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def getBalance(rootnode):
    if not rootnode:
        return 0
    return getHeight(rootnode.leftchild) - getHeight(rootnode.rightchild)

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftchild
    disbalanceNode.leftchild = disbalanceNode.leftchild.rightchild
    newRoot.rightchild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild) , getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild) , getHeight(newRoot.rightchild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightchild
    disbalanceNode.rightchild = disbalanceNode.rightchild.leftchild
    newRoot.leftchild = disbalanceNode
    disbalanceNode.height = 1 +  max(getHeight(disbalanceNode.leftchild) , getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild) , getHeight(newRoot.rightchild))
    return newRoot

def insertNode(rootnode, node_value):
    if not rootnode:
        return AVLNode(node_value)
    elif node_value < rootnode.data:
        rootnode.leftchild = insertNode(rootnode.leftchild , node_value)
    else:
        rootnode.rightchild = insertNode(rootnode.rightchild , node_value)

    rootnode.height = 1 + max(getHeight(rootnode.leftchild),
                              getHeight(rootnode.rightchild))
    balance = getBalance(rootnode)
    if balance > 1 and node_value < rootnode.leftchild.data:
        return rightRotate(rootnode)
    if balance > 1 and node_value > rootnode.leftchild.data:
        rootnode.leftchild = leftRotate(rootnode.leftchild)
        return rightRotate(rootnode)
    if balance < -1 and node_value > rootnode.rightchild.data:
        return leftRotate(rootnode)
    if balance < -1 and node_value < rootnode.rightchild.data:
        rootnode.rightchild = rightRotate(rootnode.rightchild)
        return leftRotate(rootnode)
    return rootnode

# ----------------------------
# 1) ORIGINAL deleteAVL (your provided version) — explained
# ----------------------------
def deleteAVL_original(rootnode):
    """
    Your original function:
      rootnode.data = None
      rootnode.leftchild = None
      rootnode.rightchild = None
      return "The AVL has been Successfully deleted"

    Effect:
      - The root variable in caller still points to an AVLNode instance.
      - That instance now has data = None and no children.
      - All previously reachable nodes (children) become unreachable from root
        and thus eligible for garbage collection (assuming no other references).
      - However, the root node object itself remains (a dummy node).
      - levelOrderTraversal(root) will still see that dummy node (prints None)
        because `rootnode` is not None.

    Example (what happens):
      Before delete:
          20
         /  \
        10  50
      After deleteAVL_original(root):
          (root)  <-- AVLNode with data = None, leftchild = None, rightchild = None

      levelOrderTraversal prints:
         None

    Why this might be surprising:
      - Many people expect the variable `root` to become None so that traversal
        reports "Tree is Empty". With this approach the node object still exists.
    """
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "The AVL has been Successfully deleted"

# ----------------------------
# 2) RECOMMENDED deleteAVL — correct way to "delete" entire tree
# ----------------------------
def deleteAVL(rootnode):
    """
    Recommended approach for 'delete entire tree' in Python:

    - The usual and simple way in Python is to remove references to the root node:
         root = None
      and (optionally) rely on garbage collector (gc) to reclaim memory.
    - In a function, return None and let caller set root = deleteAVL(root)
      so the caller's root reference is replaced by None.

    Implementation:
      - We do nothing to individual nodes; we simply return None to let the
        caller drop the reference to the entire structure.
      - If you have other references to nodes (outside this tree), those nodes
        will persist; only nodes unreachable from root will be collected.

    Usage:
      root = deleteAVL(root)   # now root is None

    Effect:
      levelOrderTraversal(root) -> "Tree is Empty"
    """
    # nothing to free manually — let caller drop root reference
    return None

# ----------------------------
# Example usage + demonstration
# ----------------------------
if __name__ == "__main__":
    # Build same AVL using your insertion sequence
    root = AVLNode(30)
    root = insertNode(root, 25)
    root = insertNode(root, 35)
    root = insertNode(root, 20)
    root = insertNode(root, 15)
    root = insertNode(root, 5)
    root = insertNode(root, 10)
    root = insertNode(root, 50)
    root = insertNode(root, 60)
    root = insertNode(root, 70)
    root = insertNode(root, 65)

    print("Level order traversal (BFS) BEFORE deleting entire tree:")
    levelOrderTraversal(root)

    # ---------------------------------------------------------
    # Using the original in-place method (keeps a dummy root)
    # ---------------------------------------------------------
    print("\nUsing deleteAVL_original(root) — sets root.data=None etc")
    deleteAVL_original(root)
    print("Level order traversal AFTER deleteAVL_original(root):")
    # Note: traversal sees a node object with data None (prints None)
    levelOrderTraversal(root)

    # Rebuild tree for demonstration of recommended approach
    root = AVLNode(30)
    root = insertNode(root, 25)
    root = insertNode(root, 35)
    root = insertNode(root, 20)
    root = insertNode(root, 15)
    root = insertNode(root, 5)
    root = insertNode(root, 10)
    root = insertNode(root, 50)
    root = insertNode(root, 60)
    root = insertNode(root, 70)
    root = insertNode(root, 65)

    print("\nRebuilt tree — BFS before recommended deletion:")
    levelOrderTraversal(root)

    # ---------------------------------------------------------
    # Recommended deletion: drop the root reference by receiving None
    # ---------------------------------------------------------
    print("\nUsing recommended deleteAVL (returns None); set root = deleteAVL(root)")
    root = deleteAVL(root)   # now root is None
    print("Level order traversal AFTER recommended deleteAVL(root):")
    # This prints "Tree is Empty"
    print(levelOrderTraversal(root))

# ----------------------------
# Complexity and notes
# ----------------------------
"""
Complexity:
 - deleteAVL_original:
     Time: O(1) — constant-time attribute assignments
     Space: O(1)
 - deleteAVL (recommended, returning None):
     Time: O(1)
     Space: O(1)

Garbage collection details:
 - Python reclaims memory for objects that become unreachable.
 - If you simply set the caller's root to None (root = None), the tree nodes
   become unreachable (assuming no other references), and the GC will collect them later.
 - If you created cycles or have external references to internal nodes, GC may
   need to run to collect them (but usually automatic).

Practical recommendations:
 - Use `root = deleteAVL(root)` (recommended). That makes the caller's root
   reference None and prints "Tree is Empty" via levelOrderTraversal.
 - Avoid the "set root.data=None" trick unless you intentionally want to keep a
   root object representing an "empty placeholder".
 - If you must force immediate cleanup for memory-critical applications:
     import gc
     root = deleteAVL(root)
     gc.collect()
   but this is rarely necessary.

Safety:
 - After deleting the tree the variable that used to hold the root must not be
   used as if it still points to a node (check for None).
"""

