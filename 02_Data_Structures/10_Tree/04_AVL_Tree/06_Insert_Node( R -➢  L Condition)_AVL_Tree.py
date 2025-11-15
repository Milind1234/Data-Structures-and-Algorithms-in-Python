r"""
=====================================================================
📘 AVL Tree — Right-Left (RL) Condition  
Rotation Required → RIGHT ROTATION + LEFT ROTATION  
=====================================================================

This is the **fourth imbalance case** in AVL Trees.

So far, we learned:

✔ LL  → Right Rotation  
✔ LR  → Left Rotation + Right Rotation  
✔ RR  → Left Rotation  

Now we study:

✔ **RL (Right-Left) Condition**  
✔ Fix: **Right Rotation (on Right Child) → Left Rotation (on Disbalanced Node)**

This note explains:
1️⃣ How RL imbalance forms  
2️⃣ How to detect RL  
3️⃣ Why 2 rotations are needed  
4️⃣ Full RL example from slides  
5️⃣ Step-by-step algorithm (with variable values)  
6️⃣ Time & Space Complexity  

=====================================================================
🌳 1) Understanding the RL Condition
=====================================================================

RL occurs when:

    Path to newly inserted node = RIGHT → LEFT

This means:
- We first go **right** from disbalanced node  
- Then we go **left** from that right child  

This creates a “zig-zag” shape, which cannot be fixed by a single rotation.

Therefore:
👉 First fix the “child subtree” with **Right Rotation**  
👉 Then fix the whole disbalanced node with **Left Rotation**  


=====================================================================
🌱 2) Example — How RL imbalance is created
=====================================================================

Initial AVL Tree:

                        50
                      /     \
                    40       60
                              \
                               70
                              /
                            65   ← insert here

Insert **65**:

- 65 > 50 → go right  
- 65 > 60 → go right  
- 65 < 70 → go left  
→ Insert as left child of 70

Updated subtree:

                      60
                        \
                         70
                        /
                      65

Now check balance:

Node 65 → balanced  
Node 70 → balanced  
Node 60:
    left height = 0
    right height = 2
    → difference = 2 → **Disbalanced node = 60**

Find path from 60 to grandchild:
    RIGHT → LEFT
⟹ **RL Condition** detected.


=====================================================================
🔥 3) Fixing RL Condition — Two Rotations
=====================================================================

RL fix requires:

    STEP 1: Right Rotation on right child (70)
    STEP 2: Left Rotation on disbalanced node (60)

Reason:
- First step changes the zig-zag shape into straight RR  
- Second step balances the new RR using left rotation


=====================================================================
🌀 4) RL Fix — Step 1: Right Rotation on Right Child (70)
=====================================================================

Before rotation:

                  70
                /
              65

Variables:
    disbalancedNode.rightChild = 70  
    So rotation happens on **70**

Right Rotation steps (conceptually):

1️⃣ newRoot = 70.left = 65  
2️⃣ 70.left = 65.right  (None)  
3️⃣ newRoot.right = 70  

After Step 1:

                65
                  \
                   70

Now subtree for node 60 becomes:

                      60
                        \
                         65
                           \
                            70

This is now **RR condition**, ready for Left Rotation.


=====================================================================
🌀 5) RL Fix — Step 2: Left Rotation on Disbalanced Node (60)
=====================================================================

Before rotation:

                      60
                        \
                         65
                           \
                            70

Left Rotation steps:

1️⃣ newRoot = 60.right = 65  
2️⃣ 60.right = 65.left (None)  
3️⃣ newRoot.left = 60  

Final subtree:

                      65
                    /    \
                  60      70

Perfectly balanced.


=====================================================================
🧪 6) Full RL Example — Combined (from slides)
=====================================================================

Start:

        60                     (Disbalanced)
          \
           70
          /
        65

STEP 1 → Right rotation on 70:

        65
          \
           70

STEP 2 → Left rotation on 60:

              65
            /    \
          60      70

AVL subtree is now balanced.


=====================================================================
🧩 7) RL Algorithm — With Variable Values
=====================================================================

Let:
    disbalancedNode = node where imbalance detected (e.g., 60)
    rightChild = disbalancedNode.rightChild (e.g., 70)
    grandchild = rightChild.leftChild (e.g., 65)

Two-step algorithm:

─────────────────────────────────────────────
Step 1: Right Rotate(disbalancedNode.rightChild)
─────────────────────────────────────────────

Given rightChild:

    newRoot = rightChild.leftChild        → 65
    rightChild.leftChild = newRoot.rightChild
        → 65.right is None
    newRoot.rightChild = rightChild       → 70

Result:
        65
          \
           70


─────────────────────────────────────────────
Step 2: Left Rotate(disbalancedNode)
─────────────────────────────────────────────

Given disbalancedNode = 60:

    newRoot = disbalancedNode.rightChild
        → rightChild is now 65
    disbalancedNode.rightChild = newRoot.leftChild
        → 65.left is None
    newRoot.leftChild = disbalancedNode
        → 65.left = 60

Final:
              65
            /    \
          60      70


=====================================================================
⏱ 8) Time & Space Complexity
=====================================================================

For RL:

Right Rotation → O(1)  
Left Rotation  → O(1)

Total:
    Time = O(1)
    Space = O(1)

Only 2–3 pointer updates are done in each rotation.


=====================================================================
✅ Summary (Very Important for Exams)
=====================================================================

✔ RL condition occurs when path is RIGHT → LEFT  
✔ Fix = **Right Rotation → Left Rotation**  
✔ First rotate the child (to convert RL → RR)  
✔ Then rotate the parent (RR → balanced)  
✔ Final tree always becomes height-balanced  
✔ Time complexity = O(1)  

Next Lecture:
-------------
➡ Combining LL + LR + RR + RL into the **complete AVL insertion algorithm**

=====================================================================
"""
