"""
===============================================================================
📘 insertNode.py — AVL Tree (Insertion + Rotations + Helper Functions)
===============================================================================

Purpose
-------
This file explains AVL Tree insertion with:
- Why height is stored
- How rotations work (Right, Left, LR, RL)
- Balance factor logic
- insertNode() with VISUALIZATION using your example values
  (30, 25, 35, 20, 15, 5, 10, 50, 60, 70, 65)

This file contains:
  - The full AVL implementation you provided (unchanged logic),
  - Detailed explanatory comments for every helper and for each branch of
    `insertNode` (LL, LR, RR, RL) — including small ASCII visualizations,
  - The runnable sequence used in your example:
        30,25,35,20,15,5,10,50,60,70,65
  - levelOrderTraversal (kept exactly as you provided) — NOT explained here
    because you asked not to.

Drop this file into the same directory as your QueueLinkedList module and run.

===============================================================================
USAGE:
  python note.py
  (Make sure QueueLinkedList.py with Queue class is available in the same folder.)

===============================================================================
"""

# ----------------------------
# Imports
# ----------------------------
import QueueLinkedList as queue   # your custom queue (levelOrderTraversal uses this)
# no other third-party imports required


# ----------------------------
# AVL Node
# ----------------------------
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        # Height convention: empty subtree -> 0, leaf node -> height 1
        self.height = 1


# --------------------------------
# levelOrderTraversal (unchanged)
# --------------------------------
def levelOrderTraversal(rootnode):
    """
    Level-order traversal using your QueueLinkedList.

    Time complexity: O(n) — visits each node once
    Space complexity: O(n) — queue may hold up to O(n) nodes in worst-case (one level)
    """
    if not rootnode:
        return "Tree is Empty"
    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftchild is not None:
            customQueue.enqueue(root.value.leftchild)
        if root.value.rightchild is not None:
            customQueue.enqueue(root.value.rightchild)


# ----------------------------
# searchNodeAVL
# ----------------------------
def searchNodeAVL(rootnode, target_node):
    """
    BST search on AVL tree (recursive).

    Behavior:
      - Returns a short message string indicating found/not found.
      - Works because AVL preserves BST property.

    Time complexity: O(log n) average for balanced AVL, O(n) worst-case (if tree becomes skewed)
    Space complexity: O(log n) recursion stack on balanced AVL, O(n) worst-case
    """
    if not rootnode:
        return "Target Not Found"

    if rootnode.data == target_node:
        return f"The Target {target_node} is Found"

    if target_node < rootnode.data:
        return searchNodeAVL(rootnode.leftchild, target_node)

    if target_node > rootnode.data:
        return searchNodeAVL(rootnode.rightchild, target_node)


# ----------------------------
# getHeight
# ----------------------------
def getHeight(rootnode):
    """
    Return the height stored at the node.
    Convention:
      - None -> 0
      - existing node -> node.height (leaf nodes initialize to 1)
    This function centralizes access so rest of the code looks clean.
    Time complexity: O(1)
    Space complexity: O(1)
    """
    if not rootnode:
        return 0
    return rootnode.height

# ----------------------------
# ⚖️ getBalance
# ----------------------------
def getBalance(rootnode):
    """
    Balance factor = height(left) - height(right)
    Positive -> left heavier
    Negative -> right heavier

    Time complexity: O(1)
    Space complexity: O(1)
    """
    if not rootnode:
        return 0
    return getHeight(rootnode.leftchild) - getHeight(rootnode.rightchild)

# ----------------------------
# rightRotate
# ----------------------------
def rightRotate(disbalanceNode):
    """
    Right Rotation (LL Fix)

    REAL EXAMPLE FROM YOUR INSERTIONS:
    -----------------------------------
    LL happens when inserting: **15**
    Path: 15 < 30 → left
          15 < 25 → left
          15 < 20 → left

    Before rotation (disbalanceNode = 25):

            (25)
            /
         (20)
         /
       (15)

    After rightRotate(25):

            (20)
           /    \
        (15)    (25)

    Implementation steps (with REAL VALUES):
    ----------------------------------------
    Step 1: newRoot = disbalanceNode.leftchild
            → newRoot = 20

    Step 2: disbalanceNode.leftchild = newRoot.rightchild
            → 25.left = 20.right
            → (20 has no right child, so 25.left = None)

    Step 3: newRoot.rightchild = disbalanceNode
            → 20.right = 25

    Step 4: Update height of 25

    Step 5: Update height of 20

    Step 6: return newRoot (which is 20)

    Time complexity: O(1) — constant pointer updates and height recalcs
    Space complexity: O(1)
    """
    newRoot = disbalanceNode.leftchild
    disbalanceNode.leftchild = disbalanceNode.leftchild.rightchild
    newRoot.rightchild = disbalanceNode

    # update heights (bottom-up)
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild),
                                   getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild),
                             getHeight(newRoot.rightchild))
    return newRoot


# ----------------------------
# leftRotate
# ----------------------------
def leftRotate(disbalanceNode):
    """
    Left Rotation (RR Fix)

    REAL EXAMPLE FROM YOUR INSERTIONS:
    -----------------------------------
    RR happens when inserting: **60**
    Path:
        60 > 30  → go right
        60 > 35  → go right
        60 > 50  → go right

    Before rotation (disbalanceNode = 35):

            (35)
               \
               (50)
                  \
                  (60)

    After leftRotate(35):

                (50)
               /    \
           (35)     (60)

    Implementation steps (REAL VALUES):
    -----------------------------------
    Step 1: newRoot = disbalanceNode.rightchild
            → newRoot = 50

    Step 2: disbalanceNode.rightchild = newRoot.leftchild
            → 35.right = 50.left
            → (50 has no left child, so 35.right = None)

    Step 3: newRoot.leftchild = disbalanceNode
            → 50.left = 35

    Step 4: Update height of 35

    Step 5: Update height of 50

    Step 6: return newRoot (which is 50)

    Time complexity: O(1) — constant pointer updates and height recalcs
    Space complexity: O(1)
    """
    newRoot = disbalanceNode.rightchild
    disbalanceNode.rightchild = disbalanceNode.rightchild.leftchild
    newRoot.leftchild = disbalanceNode

    # update heights (bottom-up)
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild),
                                   getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild),
                             getHeight(newRoot.rightchild))
    return newRoot

# ----------------------------
# insertNode (with detailed comments & visualizations)
# ----------------------------
def insertNode(rootnode, nodevalue):
    """
    Insert nodevalue into subtree rooted at rootnode, rebalance if necessary.

    Steps:
      1) Standard BST insertion (recursive)
      2) Update height
      3) Compute balance
      4) If unbalanced, apply one of:
         - LL: rightRotate
         - LR: leftRotate(left child) → rightRotate
         - RR: leftRotate
         - RL: rightRotate(right child) → leftRotate

    Complexity:
      Time: O(log n) on balanced AVL (height operations and at most constant rotations).
            Worst-case O(n) if tree becomes skewed (but AVL keeps it balanced).
      Space: O(log n) recursion stack on balanced tree; O(n) worst-case.
    """

    # ---------- 1) BST insert ----------
    if not rootnode:
        return AVLNode(nodevalue)
    elif nodevalue < rootnode.data:
        rootnode.leftchild = insertNode(rootnode.leftchild, nodevalue)
    else:
        # duplicates go to right in this implementation (like original)
        rootnode.rightchild = insertNode(rootnode.rightchild, nodevalue)

    # ---------- 2) update height ----------
    rootnode.height = 1 + max(getHeight(rootnode.leftchild),
                              getHeight(rootnode.rightchild))

    # ---------- 3) get balance ----------
    balance = getBalance(rootnode)

    # ---------- 4) balance cases ----------
    # CASE 1: Left Left (LL)
    # Condition:
    #   - left subtree heavier (balance > 1)
    #   - inserted key is in left child's left subtree:
    #       nodevalue < rootnode.leftchild.data
    #
    # Visual:
    # Before (LL):
    #             25         <- rootnode (unbalanced, BF > +1)
    #            /
    #          20
    #         /
    #        15
    #
    # After rightRotate(25):
    #           20
    #          /  \
    #        15   25
    # ------------------------------------------------------------------
    if balance > 1 and nodevalue < rootnode.leftchild.data: 
        # Right rotation
        return rightRotate(rootnode)
    # ------------------------------------------------------------------
    # CASE 2: Left Right (LR)
    # Condition:
    #   - left subtree heavier (balance > 1)
    #   - inserted key is in left child's RIGHT subtree:
    #       nodevalue > rootnode.leftchild.data
    #
    # Visual:
    # Before (LR):
    # 
    #        15
    #       /
    #      5
    #        \
    #        10
    #
    # Fix:
    #   1) leftRotate(5)  -> transforms into LL shape (10 becomes parent of 5)
    #   2) rightRotate(15)
    #
    # After:

    #       10
    #      /  \
    #     5   15
    #
    # ------------------------------------------------------------------
    if balance > 1 and nodevalue > rootnode.leftchild.data:
        rootnode.leftchild = leftRotate(rootnode.leftchild)
        return rightRotate(rootnode)
    # ------------------------------------------------------------------
    # CASE 3: Right Right (RR)
    # Condition:
    #   - right subtree heavier (balance < -1)
    #   - inserted key is in right child's right subtree:
    #       nodevalue > rootnode.rightchild.data
    #
    # Visual:
    # Before (RR):
     #     35
    #       \
    #       50
    #         \
    #         60
    #
    # After leftRotate(35):
    # 
    #     (50)
    #    /    \
    #  (35)  (60)
    # 
    # ------------------------------------------------------------------
    if balance < -1 and nodevalue > rootnode.rightchild.data:
        return leftRotate(rootnode)
    # ------------------------------------------------------------------
    # CASE 4: Right Left (RL)
    # Condition:
    #   - right subtree heavier (balance < -1)
    #   - inserted key is in right child's LEFT subtree:
    #       nodevalue < rootnode.rightchild.data
    #
    # Visual:
    # Before:
    # 
    #       60
    #         \
    #         70
    #        /
    #      65
    #
    # Fix:
    # Step1: rightRotate(70)
    #
    #         60
    #           \
    #           65
    #             \
    #             70
    #
    # Step2: leftRotate(60)
    #
    #           65
    #          /  \
    #        60   70
    #
    # Step1: rightRotate(70) -> subtree becomes (65 -> right 70)
    # Step2: leftRotate(60)  -> subtree becomes 65 as parent of 60 and 70
    # ------------------------------------------------------------------
    if balance < -1 and nodevalue < rootnode.rightchild.data:
        rootnode.rightchild = rightRotate(rootnode.rightchild)
        return leftRotate(rootnode)
    # If balanced no rotation is needed
    return rootnode
    # ------------------------------------------------------------------


# ----------------------------
# Example usage (same insertion sequence you used)
# ----------------------------
if __name__ == "__main__":
    # build the AVL using the insertion sequence you provided
    newAVL = AVLNode(30)
    newAVL = insertNode(newAVL, 25)
    newAVL = insertNode(newAVL, 35)
    newAVL = insertNode(newAVL, 20)
    newAVL = insertNode(newAVL, 15)
    newAVL = insertNode(newAVL, 5)
    newAVL = insertNode(newAVL, 10)
    newAVL = insertNode(newAVL, 50)
    newAVL = insertNode(newAVL, 60)
    newAVL = insertNode(newAVL, 70)
    newAVL = insertNode(newAVL, 65)

    # Level order traversal will print the tree node values in BFS order.
    # (Function left unchanged; you asked not to explain it.)
    print("Level order traversal (BFS) of final AVL tree:")
    levelOrderTraversal(newAVL)

    # Quick search examples
    print(searchNodeAVL(newAVL, 65))
    print(searchNodeAVL(newAVL, 999))  # not found

"""
===============================================================================
SUMMARY TABLE (quick reference)
--------------------------------------------------------------------------------
Function                  | Time Complexity          | Space Complexity
------------------------- | -------------------------|--------------------------
AVLNode.__init__          | O(1)                     | O(1)
getHeight                 | O(1)                     | O(1)
getBalance                | O(1)                     | O(1)
rightRotate / leftRotate  | O(1) each                | O(1)
searchNodeAVL             | O(log n) avg, O(n) worst | O(log n) avg, O(n) worst
levelOrderTraversal       | O(n)                     | O(n)
insertNode                | O(log n) avg, O(n) worst | O(log n) avg, O(n) worst
===============================================================================
"""