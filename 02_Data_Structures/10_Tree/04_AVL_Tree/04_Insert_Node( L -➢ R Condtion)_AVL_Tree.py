r"""
📘 Topic: AVL Tree — Insertion (Case 2: LR — Left-Right Condition)
=========================================================================

In the previous note, we studied **LL condition** and fixed it using **Right Rotation**.

In this Note, we learn:

1️⃣ Why LR condition occurs  
2️⃣ How to identify LR case  
3️⃣ Why TWO rotations are required  
4️⃣ Example from the Note  
5️⃣ Algorithm  
6️⃣ Step-by-step diagrams  
7️⃣ Time & Space Complexity  

=====================================================================
🌳 1) Understanding LR (Left-Right) Condition
=====================================================================

The LR condition happens during insertion when the path to the inserted node is:

    LEFT → RIGHT

Example:

                   70
                /      \
              50        90
            /    \     /   \
          30     60   80   100
         /
       20
        \
         25   ← inserted here

Insertion logic:
- 25 < 70 → go left
- 25 < 50 → go left
- 25 < 30 → go left
- 25 > 20 → go right → insert

After insertion:

           30   ← disbalanced node
         /
       20
         \
          25

Height difference at node 30:
    left height = 2
    right height = 0
    difference = 2 → **UNBALANCED**

Path to inserted node:
    LEFT → RIGHT

This is the **LR Condition**.

=====================================================================
🔥 2) Why LR Requires TWO Rotations?
=====================================================================

LR condition is a *zig-zag shape*:

           30
         /
       20
         \
          25

To fix LR imbalance:
1️⃣ First convert LR → LL using **Left Rotation** (on child)  
2️⃣ Then fix LL using **Right Rotation** (on disbalanced node)  

So the repair steps are:

    Step 1: rotateLeft(disbalancedNode.leftChild)
    Step 2: rotateRight(disbalancedNode)

=====================================================================
🌀 3) Step 1 — Left Rotation on Left Child
=====================================================================

Disbalanced Node  = 30  
Left Child        = 20  

Before Left Rotation:

           30
         /
       20
         \
          25

After Left Rotate(20):

           30
         /
       25
      /
    20

After Step 1 the subtree becomes **LL shaped**, preparing for Step 2.

=====================================================================
🔄 4) Step 2 — Right Rotation on Disbalanced Node
=====================================================================

Disbalanced Node = 30

Before Right Rotation:

           30
         /
       25
      /
    20

After Right Rotation:

           25
         /    \
       20      30

Now this subtree is perfectly balanced.

=====================================================================
🌲 5) Final Balanced AVL Tree
=====================================================================

After performing
    ✔ Left Rotation on 20  
    ✔ Right Rotation on 30  

The final AVL tree becomes:

                   70
                /      \
              50        90
            /    \     /   \
          25     60   80   100
        /    \
      20      30


=====================================================================
🧩 6) Algorithm of Left-Right (LR) Condition
=====================================================================

Step 1:
    rotateLeft(disbalancedNode.leftChild)

Step 2:
    rotateRight(disbalancedNode)


Detailed algorithms:

--------------------------
rotateLeft(disbalancedNode):
--------------------------
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = newRoot.leftChild
    newRoot.leftChild = disbalancedNode
    update height(disbalancedNode)
    update height(newRoot)
    return newRoot


--------------------------
rotateRight(disbalancedNode):
--------------------------
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = newRoot.rightChild
    newRoot.rightChild = disbalancedNode
    update height(disbalancedNode)
    update height(newRoot)
    return newRoot

=====================================================================
🧪 7) Detailed Working Example (From Images)
=====================================================================

Initial subtree:

           30
         /
       10
         \
          20   ← causes LR imbalance

📍 Step 1 — Left Rotate(10)

Before:
        10
          \
           20

After:
        20
       /
     10

📍 Step 2 — Right Rotate(30)

Before:
        30
       /
     20
    /
  10

After:
        20
       /  \
     10    30

The subtree becomes balanced.

=====================================================================
⏱ 8) Time & Space Complexity
=====================================================================

LR fixing involves:
    • One left rotation
    • One right rotation

Both operations are constant-time pointer adjustments.

Therefore:

Time Complexity  →  O(1)  
Space Complexity →  O(1)  

=====================================================================
✅ Summary
=====================================================================

✔ LR = Left-Right Condition  
✔ Identified when path is LEFT → RIGHT  
✔ Requires **two rotations**  
    1. Left Rotation  (on left child)  
    2. Right Rotation (on disbalanced node)  

✔ After both rotations the subtree becomes balanced  
✔ Total complexity = O(1)

Next Note:
--------------
➡ Right-Right (RR) Condition  

=====================================================================
"""
