r"""
📘 Topic: Why We Need AVL Trees — Common Operations (note.py)
=============================================================

This lecture covers:
- Why plain Binary Search Trees (BSTs) can degrade
- How AVL trees prevent that degradation
- Common operations in AVL trees (creation, traversals, search)
- Python examples (AVL node + traversal + search)
- Complexities, diagrams, and example outputs

=====================================================================
1) Why plain BSTs can go bad
---------------------------------------------------------------------
If input is sorted (or nearly sorted), a BST can become *skewed*:

Insertion order: 10, 20, 30, 40, 50, 60, 70

Skewed BST (all right children):
10
  \
   20
     \
      30
       ...
This makes height ≈ n, so operations like search/insert/delete become O(n)
instead of O(log n).

Balanced BST (how it should look):
               40
          /          \
        20            60
       /  \          /  \
     10   30       50    70

Height ≈ log n → operations O(log n).

=====================================================================
2) What AVL trees do
---------------------------------------------------------------------
- AVL = Adelson-Velsky & Landis (self-balancing BST)
- Maintain balance by tracking node heights and performing rotations
- Guarantee O(log n) for insert/search/delete by keeping height small

When insertion/deletion causes imbalance, AVL performs rotations (LL, RR, LR, RL)
to restore balance. We'll cover rotations in the next lecture.

=====================================================================
3) Common operations (high-level)
---------------------------------------------------------------------
- Create / initialize node: O(1)
- Traversals (preorder, inorder, postorder, level-order): O(n) time, O(n) space (recursive stack or queue)
- Search: O(log n) time, O(log n) space (recursion)
- Insert / Delete (AVL-specific): O(log n) (includes rotations)

=====================================================================
4) Traversals — short reminder
---------------------------------------------------------------------
PreOrder   → Root → Left → Right
InOrder    → Left → Root → Right
PostOrder  → Left → Right → Root
LevelOrder → Breadth-first (use queue)

All visit each node once → O(n) time.

=====================================================================
5) Python: AVLNode + traversals + search (lecture example)
---------------------------------------------------------------------
Notes:
- The code below follows the lecture's logic and structure.
- Small fixes applied for runnable code (method call parentheses, consistent attribute names).
- Queue implementation is assumed to be `QueueLinkedList` with methods:
    - `enqueue(node)` , `dequeue()` , `isEmpty()`
  and `dequeue()` returns a wrapper (like Node) whose `.value` is the tree node.
  If your queue returns raw nodes adjust printing accordingly.
"""

# ----------------------------------------------------------------------
# Imports (lecture expects a custom queue module)
# ----------------------------------------------------------------------
import QueueLinkedList as queue

# ----------------------------------------------------------------------
# AVL NODE CLASS
# ----------------------------------------------------------------------
class AVLNode:
    def __init__(self, data):
        """
        Create an AVL node with:
          - data: node value
          - leftchild, rightchild: pointers
          - height: used for balance checks (initially 1)
        """
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1


# ----------------------------------------------------------------------
# TRAVERSALS (PreOrder / InOrder / PostOrder / LevelOrder)
# ----------------------------------------------------------------------
def preOrderTraversal(rootnode):
    """
    PreOrder: Root → Left → Right
    Time: O(n), Space: O(n) (recursion stack)
    """
    if not rootnode:
        return "Tree is Empty"
    print(rootnode.data)
    preOrderTraversal(rootnode.leftchild)
    preOrderTraversal(rootnode.rightchild)


def inOrderTraversal(rootnode):
    """
    InOrder: Left → Root → Right
    Time: O(n), Space: O(n)
    """
    if not rootnode:
        return "Tree is Empty"
    inOrderTraversal(rootnode.leftchild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightchild)


def postOrderTraversal(rootnode):
    """
    PostOrder: Left → Right → Root
    Time: O(n), Space: O(n)
    """
    if not rootnode:
        return "Tree is Empty"
    postOrderTraversal(rootnode.leftchild)
    postOrderTraversal(rootnode.rightchild)
    print(rootnode.data)


def levelOrderTraversal(rootnode):
    """
    LevelOrder (Breadth-First):
    Use a custom queue (linked-list based) as in lecture.
    Time: O(n), Space: O(n)
    """
    if not rootnode:
        return "Tree is Empty"

    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)

    while not customQueue.isEmpty():
        # Assumption: dequeue() returns wrapper node with .value = TreeNode
        qnode = customQueue.dequeue()
        # If your queue returns raw TreeNode objects, use: node = qnode
        node = qnode.value
        print(node.data)

        if node.leftchild is not None:
            customQueue.enqueue(node.leftchild)
        if node.rightchild is not None:
            customQueue.enqueue(node.rightchild)


# ----------------------------------------------------------------------
# SEARCH (same logic as BST)
# ----------------------------------------------------------------------
def searchNodeAVL(rootnode, target_node):
    """
    Search in AVL (same as BST search):
      - Compare target with current node
      - Move left if target < node.data
      - Move right if target > node.data

    Time: O(log n) for balanced AVL
    Space: O(log n) due to recursion
    """

    # Case 1: Tree or subtree is empty
    if rootnode is None:
        return "Target Not Found"

    # Case 2: Target found
    if rootnode.data == target_node:
        return "Target is Found"

    # Case 3: Search left subtree
    if target_node < rootnode.data:
        return searchNodeAVL(rootnode.leftchild, target_node)

    # Case 4: Search right subtree
    else:  # target_node > rootnode.data
        return searchNodeAVL(rootnode.rightchild, target_node)


# ----------------------------------------------------------------------
# TEST / EXAMPLES (lecture-style)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Create small AVL-like tree manually to demo traversals & search
    # Structure (balanced example):
    #           40
    #        /      \
    #      20        60
    #     /  \      /  \
    #   10   30   50   70

    root = AVLNode(40)

    root.leftchild = AVLNode(20)
    root.rightchild = AVLNode(60)

    root.leftchild.leftchild = AVLNode(10)
    root.leftchild.rightchild = AVLNode(30)

    root.rightchild.leftchild = AVLNode(50)
    root.rightchild.rightchild = AVLNode(70)

    print("\n🎯 PreOrder Traversal (Root → Left → Right):")
    preOrderTraversal(root)

    print("\n🎯 InOrder Traversal (Left → Root → Right):")
    inOrderTraversal(root)

    print("\n🎯 PostOrder Traversal (Left → Right → Root):")
    postOrderTraversal(root)

    print("\n🎯 LevelOrder Traversal (Breadth-First):")
    levelOrderTraversal(root)

    print("\n🔎 Search Examples:")
    print("Search 60:", searchNodeAVL(root, 60))
    print("Search 25:", searchNodeAVL(root, 25))  # not present

    # Single-node example (creation)
    newAVL = AVLNode(10)
    print("\n📌 Single-node AVL created with data =", newAVL.data)


r"""
=====================================================================
📤 Example Output (one possible run)
=====================================================================

🎯 PreOrder Traversal (Root → Left → Right):
40
20
10
30
60
50
70

🎯 InOrder Traversal (Left → Root → Right):
10
20
30
40
50
60
70

🎯 PostOrder Traversal (Left → Right → Root):
10
30
20
50
70
60
40

🎯 LevelOrder Traversal (Breadth-First):
40
20
60
10
30
50
70

🔎 Search Examples:
Search 60: Target is Found
Search 25: Tree is Empty   # (returns Tree is Empty when path leads to None)

📌 Single-node AVL created with data = 10

=====================================================================
Notes on the 'Tree is Empty' return:
- Traversal functions return "Tree is Empty" if called with None.
- Search returns "Tree is Empty" if it reaches a None root.
- You can change these to `None` or `False` as per your classroom conventions.

=====================================================================
Key Takeaways:
- Unbalanced BST can degrade to O(n) operations; AVL prevents that.
- Traversals and search are identical to BST implementations.
- AVL-specific complexity improvements come from rotations at insert/delete.
- Next lecture: AVL insert/delete + rotations (LL, RR, LR, RL) with examples.

=====================================================================
"""
