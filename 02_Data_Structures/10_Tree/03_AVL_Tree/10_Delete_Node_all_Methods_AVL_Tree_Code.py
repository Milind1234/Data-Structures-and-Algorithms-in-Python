"""
===============================================================================
📘 deleteNode.py — AVL Tree (Deletion + Rebalance + Helper Functions)
===============================================================================

Purpose
-------
This file explains AVL Tree **deletion** with:
- Why height is stored and how it's maintained
- How we remove nodes (leaf, one-child, two-children via inorder successor)
- How balance factors are computed after deletion
- How rotations (Right, Left, LR, RL) are applied during deletion
- Step-by-step visualizations for rebalancing cases after deletion
- A worked example using your exact insertion sequence:
    30, 25, 35, 20, 15, 5, 10, 50, 60, 70, 65
  followed by deletions of: 30, 35, 25

This file contains:
  - The full AVL implementation you provided (logic unchanged),
  - Detailed explanatory comments for every helper and for each branch of
    `deleteNode` — including small ASCII visualizations,
  - The runnable sequence used in your example, and the observed
    level-order (BFS) outputs before and after the deletions.

Run:
    python note.py
to see the level order traversal printed before and after the deletions.

Notes:
  - Height convention used here: empty subtree -> 0, leaf node -> 1
  - Duplicates: insertion places duplicates to the right (same as original)
  - levelOrderTraversal is unchanged from your original
===============================================================================
"""

# ----------------------------
# Imports
# ----------------------------
from collections import deque

# ----------------------------
# AVL Node
# ----------------------------
class AVLNode:
    def __init__(self , data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        # Height convention: empty subtree -> 0, leaf node -> 1
        self.height = 1

# --------------------------------
# levelOrderTraversal (unchanged)
# --------------------------------
def levelOrderTraversal(rootnode):
    """
    Breadth-first traversal printing node.data in visit order.
    Kept exactly as provided in your original code.
    Time: O(n), Space: O(n)
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
# getBalance
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
# rightRotate (LL fix)
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

    Using your values, LL occurred at **25** when the subtree became:

            (25)
            /
          (20)
          /
        (15)

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
            → height(25) = 1 + max(height(None), height(None)) = 1

    Step 5: Update height of 20
            → height(20) = 1 + max(height(15), height(25)) = 2

    Step 6: return newRoot (which is 20)

    Time complexity: O(1) — only constant pointer rearrangements
    Space complexity: O(1)
    """

    newRoot = disbalanceNode.leftchild
    disbalanceNode.leftchild = disbalanceNode.leftchild.rightchild
    newRoot.rightchild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild) , getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild) , getHeight(newRoot.rightchild))
    return newRoot

# ----------------------------
# leftRotate (RR fix)
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
    disbalanceNode.height = 1 +  max(getHeight(disbalanceNode.leftchild) , getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild) , getHeight(newRoot.rightchild))
    return newRoot

# ----------------------------
# insertNode (kept for completeness)
# ----------------------------
def insertNode(rootnode, node_value):
    """
    Standard BST insertion + AVL rebalancing (LL, LR, RR, RL).
    Implementation kept unchanged.
    """
    if not rootnode:
        return AVLNode(node_value)
    elif node_value < rootnode.data:
        rootnode.leftchild = insertNode(rootnode.leftchild , node_value)
    else:
        rootnode.rightchild = insertNode(rootnode.rightchild , node_value)

    rootnode.height = 1 + max(getHeight(rootnode.leftchild) , getHeight(rootnode.rightchild))
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
# getMinValueNode
# ----------------------------
def getMinValueNode(rootnode):
    """
    Returns the node with minimum data in subtree (leftmost).
    Used to find inorder-successor during deletion.
    """
    if not rootnode or rootnode.leftchild is None:
        return rootnode
    return getMinValueNode(rootnode.leftchild)

# ----------------------------
# deleteNode (detailed comments + visuals)
# ----------------------------
def deleteNode(rootnode , delete_Node):
    """
    Delete delete_Node from subtree rooted at rootnode and rebalance.

    Algorithm outline:
      1) Standard BST deletion:
         - Recurse left or right until you find the node.
         - If found:
             a) If node has no left child -> return right child (could be None)
             b) If node has no right child -> return left child
             c) If node has two children:
                - find inorder successor = min node of right subtree
                - copy successor.data into current node
                - delete successor from right subtree (recursive)
      2) After deletion, update height of this node.
      3) Compute balance factor.
      4) Rebalance using four cases (LL, LR, RR, RL) — note conditions use
         balance(child) to pick single/double rotation correctly for deletion.
    """
    # ---------- 1) Standard BST delete ----------
    if not rootnode:
        return rootnode
    elif delete_Node < rootnode.data:
        rootnode.leftchild = deleteNode(rootnode.leftchild, delete_Node)
    elif delete_Node > rootnode.data:
        rootnode.rightchild = deleteNode(rootnode.rightchild , delete_Node)
    else:
        # Node found
        # Case: node with only right child or no child
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        # Case: node with only left child
        elif rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        # Case: node with two children
        # Get inorder successor (smallest in right subtree)
        temp = getMinValueNode(rootnode.rightchild)
        # Copy successor's data to this node
        rootnode.data = temp.data
        # Delete the inorder successor from right subtree
        rootnode.rightchild = deleteNode(rootnode.rightchild , temp.data)

    # If the tree had one node and we deleted it, return
    if rootnode is None:
        return rootnode

    # ---------- 2) Update height ----------
    rootnode.height = 1 + max(getHeight(rootnode.leftchild) , getHeight(rootnode.rightchild))

    # ---------- 3) Get balance ----------
    balance = getBalance(rootnode)

    # ---------- 4) Rebalance ----------
    # Case: Left Left (LL)
    # If left-heavy and left child is balanced or left-heavy -> single right rotation
    if balance > 1 and getBalance(rootnode.leftchild) >= 0:
        # Visual with integers:
        #     25                              20
        #    /  \     Right Rotate (25)     /   \
        #   20  T3   - - - - - - - ->     15     25
        #  /  \                          /         \
        # 15  T2                        T2          T3
        return rightRotate(rootnode)

    # Case: Right Right (RR)
    # If right-heavy and right child is balanced or right-heavy -> single left rotation
    if balance < -1 and getBalance(rootnode.rightchild) <= 0:
        # Visual with integers:
        #   35                               50
        #  /  \     Left Rotate (35)       /    \
        # T1   50  - - - - - - - ->      35     60
        #     /  \                      /  \
        #   T2   60                    T1  T2
        return leftRotate(rootnode)

    # Case: Left Right (LR)
    # If left-heavy but left child is right-heavy -> leftRotate(left child) then rightRotate
    if balance > 1 and getBalance(rootnode.leftchild) < 0:
        # Visual with integers:
        #   15                                15                              10
        #  /  \                              /   \                          /    \
        # 5   T4   LeftRotate(5)           10     T4   RightRotate(15)     5      15
        #  \        - - - - - - - ->      /  \        - - - - - - - ->    / \    /  \
        #  10                            5   T3                          1   2  3    4
        #
        # Here T1..T4 are represented by small ints below:
        # T1 -> 1, T2 -> 2, T3 -> 3, T4 -> 4 (placeholders for subtrees)
        rootnode.leftchild = leftRotate(rootnode.leftchild)
        return  rightRotate(rootnode)

    # Case: Right Left (RL)
    # If right-heavy but right child is left-heavy -> rightRotate(right child) then leftRotate
    if balance < -1 and getBalance(rootnode.rightchild) > 0:
        # Visual with integers:
        #   60                              60                              65
        #  /  \                           /    \                          /     \
        # T1   70  RightRotate(70)      T1      65   LeftRotate(60)      60      70
        #     /    - - - - - - - ->            /  \   - - - - - - - ->  /  \    /  \
        #    65                              T2   70                  T1   T2  T3  T4
        #
        # Here T1..T4 are represented by small ints:
        # T1 -> 50, T2 -> 55, T3 -> 66, T4 -> 80 (example subtree placeholders)
        rootnode.rightchild = rightRotate(rootnode.rightchild)
        return leftRotate(rootnode)

    # Node is balanced
    return rootnode

# ----------------------------
# Worked example (same insertion + deletion sequence you used)
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

    # Print the level order traversal BEFORE deletions
    print("Level order traversal (BFS) of AVL tree BEFORE Deletion:")
    # The BFS order observed with this exact code & sequence (one valid observed order):
    # 20, 10, 50, 5, 15, 30, 65, 25, 35, 60, 70
    levelOrderTraversal(newAVL)

    # Now apply deletions as in your script
    print("\nDeleting Node : 30")
    newAVL = deleteNode(newAVL , 30)   # delete root (two-child case)
    newAVL = deleteNode(newAVL , 35)   # delete a node that may trigger rebalancing
    newAVL = deleteNode(newAVL, 25)    # delete another node causing rebalancing

    # Print the level order traversal AFTER deletions
    print("\nLevel order traversal (BFS) of AVL tree AFTER Deletion:")
    # The BFS order observed after the three deletions (one observed final shape):
    # 20, 10, 65, 5, 15, 50, 70, 60
    levelOrderTraversal(newAVL)

# ----------------------------
# Detailed deletion scenarios & visuals
# ----------------------------
"""
Deletion Scenarios — detailed explanation & small visuals

1) Deleting a leaf node:
   - Easiest case. Just return None to the parent and update heights up the tree.
   Visual:
        P
       / \
      A  (X)   -- delete X (leaf)
   After:
      P.left = None
   Then update P.height and rebalance upward if needed.

2) Deleting a node with one child:
   - Replace the node with its child (return the child to the parent).
   Visual:
       P
        \
        (N)
          \
          (C)
   After:
       P.right = C
   Then update heights and rebalance.

3) Deleting a node with two children:
   - Use inorder successor (min in right subtree).
   - Copy successor.value into the node-to-delete.
   - Delete successor from the right subtree (successor has at most one child).
   Visual:
        node (N)
        /    \
      L       R
             /
           succ
   Steps:
     - N.data = succ.data
     - remove succ from R
     - update heights and rebalance on the way back

4) Rebalancing after deletion:
   - Same rotation primitives as for insertion (rightRotate, leftRotate)
   - But the conditions for single vs double rotation rely on child balances.
     Example: If a node becomes left-heavy (balance > +1) but its left
     child is right-heavy (child balance < 0) we must do LR (leftRotate on
     left child then rightRotate on node).

Practical notes & gotchas:
  - Always update heights after the recursive delete before checking balance.
  - Check for the None case after deletion (if the node was removed, return).
  - The inorder successor is guaranteed to be in the right subtree and to have
    no left child, so removing it is simpler (0 or 1 child).

Why these child-balance checks differ from insertion checks:
  - On insertion you can inspect the inserted key to decide rotation direction
    (e.g., node_value < root.left.data => LL). On deletion the structure of
    subtrees changes and we don't have a single "just inserted" key to inspect.
    Therefore deletion uses `getBalance(child)` checks to decide whether child
    is left/right heavy and thus which rotation path to take.

Example narrative for your sequence:
  - Deleting 30 (root with two children):
     * find inorder successor = min of right subtree of 30 (value comes from
       nodes inserted earlier; for this sequence the successor chosen by the
       algorithm will be copied into the root).
     * copy successor value into root, then delete successor from right subtree.
     * this may cascade updates and rotations up the tree.

  - Subsequent deletions (35, 25) follow the same deletion + rebalance steps.

Observed BFS outputs (from running the code with the provided sequence):
  - BEFORE deletions:
      20, 10, 50, 5, 15, 30, 65, 25, 35, 60, 70

  - AFTER deleting 30, 35, 25:
      20, 10, 65, 5, 15, 50, 70, 60

  Depending on tie-breaking and rotation ordering these BFS orders are one
  correct result for the provided algorithm and insertion sequence.
"""

# -------------------------------
# SUMMARY TABLE (quick reference)
# -------------------------------
"""
-------------------------------------------------------------------------------------
| Function                  | Time Complexity          | Space Complexity.          |
|-------------------------- | ------------------------ | -------------------------- |
| AVLNode.__init__          | O(1)                     | O(1)                       |
| getHeight                 | O(1)                     | O(1)                       |
| getBalance                | O(1)                     | O(1).                      |
| rightRotate / leftRotate  | O(1) each                | O(1).                      |
| getMinValueNode           | O(h) (height)            | O(h) recursion             |
| insertNode                | O(log n) avg, O(n) worst | O(log n) avg recursion.    |
| deleteNode                | O(log n) avg, O(n) worst | O(log n) avg recursion.    |
| levelOrderTraversal       | O(n)                     | O(n)                       |
-------------------------------------------------------------------------------------
"""
