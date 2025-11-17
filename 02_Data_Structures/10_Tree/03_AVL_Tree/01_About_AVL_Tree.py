r"""
======================================================================================
📘 AVL Tree — Complete Concept Notes (Beautiful + Beginner-Friendly + Deep Explanation)
======================================================================================

An **AVL Tree** is a *self-balancing Binary Search Tree (BST)*.  
It guarantees that the tree **never becomes skewed**, keeping operations fast.

AVL Tree ensures:
    ➤ Searching → O(log n)
    ➤ Insertion → O(log n)
    ➤ Deletion → O(log n)

This is possible because **every node remains balanced**.

======================================================================================
🌳 1. AVL Tree Definition
======================================================================================

An AVL Tree is a Binary Search Tree in which **the height difference between the left 
and right subtree of ANY node is at most 1**.

This height difference is called the **Balance Factor**:

    balance_factor = height(left subtree) – height(right subtree)

Valid balance factors for AVL Tree:
    ✔ -1
    ✔  0
    ✔ +1

If any node has balance factor outside this range (like -2 or +2),  
the AVL property is violated → the tree becomes unbalanced → **rotation** is needed.

======================================================================================
🌱 2. AVL Tree Is Still a BST
======================================================================================

All BST rules still apply:

    left child  <  node value
    right child >  node value

Example BST rules inside an AVL:

                   70
                 /     \
               50       90
              /  \     /  \
            30   60   80  100
           / \
         20   40

Everything on the left is smaller than parent,  
everything on the right is larger.

======================================================================================
🧠 3. Height Balance Intuition
======================================================================================

The **height of left subtree** and **height of right subtree** should be close.

Let’s analyze this tree:

                   70
                 /     \
               50       90
              /  \
            30   60
           / \
         20   40

Heights:
    height(left subtree of 50)  = 2     (through 30 → 20/40)
    height(right subtree of 50) = 1     (through 60)
    difference = 2 - 1 = 1  ✔ Balanced

Check root (70):
    left height  = 3
    right height = 2
    difference   = 1 ✔ Balanced

This entire tree is AVL-balanced.

======================================================================================
❌ 4. Example of an UNBALANCED (Not AVL) Node
======================================================================================

Example:

                   70
                 /    
               50
              /
            30
           /
         20

Heights:
    For node 50:
        left height = 2
        right height = 0
        difference = 2 ❌ NOT allowed

    For node 70:
        left height = 3
        right height = 0
        difference = 3 ❌ NOT allowed

Therefore this is **NOT an AVL Tree**.

======================================================================================
📌 5. More Examples (like the images you uploaded)
======================================================================================

Example 1 — All Nodes Balanced ✔ (AVL Tree)

   height(left)=2, height(right)=2 → diff=0
                   70
                 /     \
               50       90
              / \      / \
            30  60    80 100

   height(left)=1, height(right)=1 → diff=0
               50
             /    \
           30      60

   height(left)=1, height(right)=1 → diff=0
               90
             /    \
           80     100


Example 2 — Also Balanced ✔

   height(left)=3, height(right)=2 → diff=1
                   70
                 /     \
               50       90
              / \      /
            30  60    80
           /
         20

   height(left)=2, height(right)=1 → diff=1
               50
             /    \
           30      60
          /
        20

   height(left)=1, height(right)=1 → diff=0
               90
              /
            80


Example 3 — STILL Balanced ✔ (leaf nodes are NOT considered for checking)

   height(left)=1, height(right)=0 → diff=1 (acceptable)
               30
             /    
           20

Everything is within the allowed range.

======================================================================================
🚫 6. Non-AVL Example (like your screenshot)
======================================================================================

                   70
                 /    
               50
             /    
           30
         /
       20
      /
    10

At node 30:
    left height  = 2
    right height = 0
    difference = 2 ❌

At node 50:
    left height = 3
    right height = 0
    diff = 3 ❌

At node 70:
    left height = 4
    right height = 0
    diff = 4 ❌

This is NOT an AVL Tree.

======================================================================================
🔄 7. How AVL Tree Fixes It — Rotations (Only Concept)
======================================================================================

When balance factor becomes ±2,
AVL performs **rotation** to restore balance:

Rotation Types:
    1) Left-Left (LL)    → Right Rotate
    2) Right-Right (RR)  → Left Rotate
    3) Left-Right (LR)   → Left Rotate + Right Rotate
    4) Right-Left (RL)   → Right Rotate + Left Rotate

Rotations make the tree balanced again **without breaking BST rules**.

Example (LL case):

 BEFORE:            AFTER:

     30                20
    /                 / \
   20               10  30
  /
 10

======================================================================================
⚙ 8. Why Do We Need AVL Trees?
======================================================================================

Regular BST can degrade into a linked list (height = n):

    Insert sorted data → BST Skewed → Time = O(n)

AVL guarantees:
    Tree height = O(log n)
    Search/Insert/Delete = O(log n)

Thus, AVL remains **fast and reliable**, even in worst-case scenarios.

Used in:
    • databases  
    • indexing systems  
    • memory allocators  
    • language runtimes  

======================================================================================
⏱ 9. Time & Space Complexity Summary
======================================================================================

Operation              Time       Space
--------------------------------------------
Create tree            O(1)       O(1)
Search                 O(log n)   O(log n)
Insert                 O(log n)   O(log n)
Delete                 O(log n)   O(log n)
Traverse               O(n)       O(n)
Delete entire tree     O(1)       O(1)

======================================================================================
✔ FINAL SUMMARY (Quick Revision)
======================================================================================

✓ AVL Tree = Self-balancing BST  
✓ Balance factor ∈ {-1, 0, +1}  
✓ Height difference > 1 → NOT AVL  
✓ Fix imbalance using rotations  
✓ Always keeps tree height = O(log n)  
✓ Search/Insert/Delete = fast  

======================================================================================
End of AVL Notes
======================================================================================
"""
