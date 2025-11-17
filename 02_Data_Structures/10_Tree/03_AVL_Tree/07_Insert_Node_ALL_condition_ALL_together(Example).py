"""
===============================================================================
📘 note.py — AVL Tree Insertion (ALL 4 CASES Together) — FULL EXAMPLE NOTES
===============================================================================

Purpose:
--------
These notes explain the **complete AVL insertion flow** using one big example
that triggers **all four imbalance cases**:

    ✔ LL (Left-Left)
    ✔ LR (Left-Right)
    ✔ RR (Right-Right)
    ✔ RL (Right-Left)

The example sequence used :

    Insert in this order:
    30, 25, 35, 20, 15, 5, 10, 50, 60, 70, 65

You see:
  - How each insertion happens as BST insertion
  - How imbalance is detected
  - How the correct rotation is chosen
  - How subtree roots change after each rotation

This is a **theory-focused note**, no actual code implementation.

===============================================================================
🌳 1. REMINDER: AVL Rules
===============================================================================

After every insertion:

    balanceFactor(node) = height(left) – height(right)

AVL requires:

    |balanceFactor(node)| <= 1

When |BF| becomes 2 → imbalance → one of the four cases:

    LL → Right Rotation
    LR → Left rotation on child + Right rotation on node
    RR → Left Rotation
    RL → Right rotation on child + Left rotation on node

We detect the case by following the path to the **inserted grandchild**.

===============================================================================
🌱 2. BEGIN THE BIG EXAMPLE INSERTIONS
===============================================================================

Insert these values step-by-step:

    30, 25, 35, 20, 15, 5, 10, 50, 60, 70, 65

Below is the exact breakdown.

-------------------------------------------------------------------------------
Step 1: Insert 30
-------------------------------------------------------------------------------
Tree is empty → 30 becomes root.

Balanced.   (30)

-------------------------------------------------------------------------------
Step 2: Insert 25
-------------------------------------------------------------------------------
25 < 30 → goes to left of 30.

               (30)
               /
             (25)

Still balanced.

-------------------------------------------------------------------------------
Step 3: Insert 35
-------------------------------------------------------------------------------
35 > 30 → goes to right of 30.
                  (30)
                 /    \
               (25)  (35)

Still balanced.

-------------------------------------------------------------------------------
Step 4: Insert 20
-------------------------------------------------------------------------------
20 < 30 → go left  
20 < 25 → go left → insert under 25
                     (30)
                    /    \
                  (25)  (35)
                  /
                (20) 
                      
Balanced.

-------------------------------------------------------------------------------
Step 5: Insert 15
-------------------------------------------------------------------------------
Path: 15 < 30 → left  
      15 < 25 → left  
      15 < 20 → left → insert under 20

Now node **25** becomes unbalanced:

    left height = 2  
    right height = 0  
    → BF = +2

Path to grandchild = Left → Left → **LL**

✔ FIX = Right Rotation on 25
Before rotation (just the affected part):

                     (25)
                     /
                   (20)
                   /
                 (15)

                After rotateRight(25):
                      (20)
                     /    \
                   (15)  (25)

                Full tree:
                         (30)
                        /    \
                     (20)    (35)
                     /  \
                  (15) (25)

Full tree remains balanced.

-------------------------------------------------------------------------------
Step 6: Insert 5
-------------------------------------------------------------------------------
Path: 5 < 30 → 20 → 15 → 5 < 15 → insert left of 15

Now node **30** becomes unbalanced:

    left height = 3  
    right height = 1  
    → BF = +2

Path to grandchild = Left → Left → **LL**

✔ FIX = Right Rotation on 30

Before rotation (affected area):
                        (30)
                        /
                    (20)
                   /    \
                (15)   (25)
                /
             (5)

After rotateRight(30):

                      (20)
                     /    \
                  (15)    (30)
                  /       /   \
                (5)    (25)   (35)


Tree is balanced again.

-------------------------------------------------------------------------------
Step 7: Insert 10
-------------------------------------------------------------------------------
Path:
  10 < 20 → left
  10 < 15 → left
  10 > 5  → insert right of 5

Now node **15** becomes unbalanced:

    left height = 2  
    right height = 0  
    → BF = +2

Path to grandchild = Left → Right → **LR**

✔ FIX:
    Step 1: rotateLeft(5)
    Step 2: rotateRight(15)

  Before rotations (local):

                    (15)
                   /
                 (5)      
                   \
                    (10)

Step1 rotateLeft(5) → becomes:

                    (10)
                    /
                (5)
                (15 stays as parent)

Step2 rotateRight(15) (i.e. rotateRight on node 15's subtree):

                    (10)
                    /   \
                  (5)  (15)

Full tree after fixes:

                      (20)
                   /       \
                 (10)       (30)
               /   \      /    \
             (5)   (15) (25)   (35)
 
 Full tree remains balanced.

-------------------------------------------------------------------------------
Step 8: Insert 50
-------------------------------------------------------------------------------
Path: 50 > 20 → right → 30 → right → 35 → right → insert

                     (20)
                  /       \
               (10)        (30)
              /   \       /    \
            (5)  (15)   (25)   (35)
                                  \
                                  (50)


Tree still balanced. No rotation needed.

-------------------------------------------------------------------------------
Step 9: Insert 60
-------------------------------------------------------------------------------
Path:
  60 > 20 → right
  60 > 30 → right
  60 > 35 → right
  60 > 50 → right → insert

Node **35** becomes unbalanced:

    left height = 0  
    right height = 2  
    → BF = -2

Path to grandchild = Right → Right → **RR**

✔ FIX = Left Rotation on 35

Before:

               (35)
                 \
                 (50)
                   \
                   (60)

After rotateLeft(35):

                 (50)
                 /  \
               (35) (60)

Full tree:

                          (20)
                       /       \
                    (10)       (30)
                   /   \      /    \
                 (5)  (15) (25)   (50)
                               /     \
                            (35)    (60)
Tree balanced.

-------------------------------------------------------------------------------
Step 10: Insert 70
-------------------------------------------------------------------------------
Path:
  70 > 20
  70 > 30
  70 > 50
  70 > 60 → right → insert

Node **30** becomes unbalanced:

    left height = 1  
    right height = 3  
    → BF = -2

Among 30's two grandchildren, 60 is deeper → we pick that path:

Path: Right → Right → **RR**

✔ FIX = Left Rotation on 30

Before (right subtree of 20):

                       (30)
                      /    \
                   (25)   (50)
                          /  \
                        (35) (60)
                               \
                               (70)

After rotateLeft(30):

                        (50)
                       /    \
                     (30)   (60)
                     /  \     \
                  (25)(35)   (70)

Full tree:

                        (20)
                     /       \
                  (10)       (50)
                 /   \      /    \
               (5)  (15) (30)   (60)
                         /  \      \
                       (25) (35)   (70)

Tree again balanced.

-------------------------------------------------------------------------------
Step 11: Insert 65
-------------------------------------------------------------------------------
Path:
  65 > 20
  65 > 50
  65 > 60
  65 < 70 → insert left of 70

Node **60** becomes unbalanced:

    left height = 0  
    right height = 2  
    → BF = -2

Path to grandchild = Right → Left → **RL**

✔ FIX:
    Step 1: rotateRight(70)     # on right child
    Step 2: rotateLeft(60)      # on disbalanced node

Before insertion right side:

                           (60)
                             \
                             (70)
                            /
                          (65)

Step1 rotateRight(70):

                           (65)
                          /   \
                        (60) (70)   (but 60 will still be parent in next step's view)

Step2 rotateLeft(60):

                      (65)
                     /   \
                   (60)  (70)

Full right subtree integrated:

                        (50)
                       /    \
                     (30)   (65)
                     /  \   /  \
                  (25)(35)(60)(70)

Full final AVL tree:

                            (20)
                         /       \
                        /          \
                      /              \
                   (10)              (50)
                  /   \            /     \
                (5)  (15)       (30)     (65)
                               /  \      /   \
                             (25  (35) (60)  (70)


Tree is balanced.

===============================================================================
🌟 FINAL AVL TREE (after all 11 insertions)
===============================================================================

  
                            (20)
                          /      \
                         /        \
                        /          \
                       /            \
                      /              \
                   (10)              (50)
                  /   \            /     \
                (5)  (15)       (30)     (65)
                               /  \      /   \
                             (25  (35) (60)  (70)

(Exact shapes depend on diagram style, but structure is AVL balanced.)

===============================================================================
🔄 Rotation Summary for This Example
===============================================================================

LL encountered at:
  - inserting 15  → fix at node 25  
  - inserting 5   → fix at node 30

LR encountered at:
  - inserting 10  → fix at node 15

RR encountered at:
  - inserting 60  → fix at node 35
  - inserting 70  → fix at node 30

RL encountered at:
  - inserting 65  → fix at node 60

All four AVL cases occurred in one example.

===============================================================================
⏱ Time & Space Complexity
===============================================================================

BST insertion: O(log n) in AVL  
Height update while climbing back: O(log n)

Rotation:
  - Right rotation : O(1)
  - Left rotation  : O(1)
  - LR / RL cases  : O(1) + O(1) = O(1)

Total insertion complexity:  
    Time: O(log n)  
    Space: O(log n) recursion or iterative stack

===============================================================================
✔ END OF note.py — Full AVL Insertion Walkthrough
===============================================================================
"""
