"""
===============================================================================
📘 note.py — AVL Tree: DELETE a node —
===============================================================================

These notes explain  visuals step-by-step and show full tree diagrams
for each example. Each case uses the real numbers visible (70,50,90,30,60,80,100,20,40,85 and small variants like 55 where
it show that intermediate).

CONVENTIONS:
- "Before" = tree right before the deletion that triggers the example action.
- "After"  = tree after performing deletion (and rotations if required).
- BF = balance factor = height(left) - height(right)
- We always show the *full* tree used before drilling into the
  local subtree where deletion and rotation happen.

===============================================================================
SHARED REFERENCE TREE 
===============================================================================
The main tree :

                 (70)
                /     \
             (50)     (90)
            /  \      /  \
         (30) (60) (80) (100)
         /  \        \
       (20) (40)     (85)

Use this as the global backdrop — individual cases below either use this
tree exactly or a small variant derived from it.

===============================================================================
CASE 1 — Rotation NOT required (simple BST removals)
===============================================================================
This show three simple deletion subcases where no rotation is required.

1.A — Delete a leaf node (example: delete 40)
---------------------------------------------
Full tree BEFORE :


                 (70)
                /     \
             (50)     (90)
            /  \      /  \
         (30) (60) (80) (100)
         /  \        \
       (20) (40)     (85)

Action:
  delete(40) — 40 is a leaf (no children).

Local BEFORE subtree (focused):
      (30)
      /  \
    (20) (40)   <-- delete this node

Local AFTER:
      (30)
      /
    (20)

Explanation:
 - Remove leaf 40 by unlinking it from parent 30.
 - Update heights on the path: 30 → 50 → 70 → ...
 - In these , no ancestor BF exceeds ±1 after updates, so **no rotation**.

1.B — Delete node with one child (example: delete 30 after 40 removed)
----------------------------------------------------------------------
Start from the tree after 40 removal:

Full tree BEFORE:
                 (70)
                /     \
             (50)     (90)
            /  \      /  \
         (30) (60) (80) (100)
         /          \
       (20)         (85)

Action:
  delete(30) — 30 has one child (20).

Local BEFORE subtree (focused):
      (50)
     /    \
   (30)  (60)
    /
  (20)

Local AFTER (after linking child to parent):
      (50)
     /    \
   (20)  (60)

Explanation:
 - Replace 30 by its single child 20 (i.e., 50.left = 20).
 - Update heights upward. If no BF goes beyond ±1, no rotations are required.
 - This demonstrates simple pointer replacement; tree stays AVL-balanced here.

1.C — Delete node with two children (use inorder successor) (example: delete 70)
--------------------------------------------------------------------------------
Full tree BEFORE :
                 (70)
                /     \
             (50)     (90)
            /  \      /  \
         (30) (60) (80) (100)
         /  \        \
       (20) (40)     (85)

Action:
  delete(70) — root has two children. Use inorder successor: smallest in right subtree.

Inorder successor of 70:
 - Right subtree of 70 is rooted at 90.
 - The minimum in that subtree is node 80 (assuming 80 has no left child).
 - (In some  80 had right child 85; 80 is still the leftmost.)

Steps:
 1. Copy successor value 80 into root position (70 becomes 80).
 2. Delete the original successor node (the node 80 that sits in 90's subtree).
 3. Fix pointers and update heights up the tree.

Local BEFORE (right-subtree focus):
    (90)
    /
  (80)
    \
    (85)

After copying 80 into root and removing original 80:
 - New root value becomes 80.
 - Delete the original node 80 (replace by its child 85 if it has one).
 - Update heights and check balances. If no |BF| > 1, no rotations.

Explanation:
 - Two-child deletion reduces to at-most-one-child deletion at successor.
 - This show deletion of root using successor and then no rotation needed in that example.

===============================================================================
CASE 2 — Rotation REQUIRED (BF becomes ±2 at an ancestor)
===============================================================================
When deletion causes an ancestor's BF to reach +2 or -2 we must rebalance.
Below each case we show the **full tree used i**, the **local before**
and **after** subtrees, and the exact rotation sequence (with numbers — no x/y/z).

===============================================================================
CASE 2.A — Left-Left (LL) — RIGHT rotation on 50 (example triggered by delete 60)
--------------------------------------------------------------------------------
Full tree BEFORE :
                 (70)
                /     \
             (50)     (90)
            /  \      /  \
         (30) (60) (80) (100)
         /  \        \
       (20) (40)     (85)

Action that triggers imbalance:
  delete(60)
  - After removing 60, node 50's left subtree height (via 30) becomes 2 while
    right subtree height becomes 0 ⇒ BF(50) = +2.

Local BEFORE (focused on node 50 subtree after delete 60):
       (50)        <-- unbalanced node
       /
     (30)
     /
   (20)

This is a **Left-Left** (LL) path: 50 -> left(30) -> left(20).

Fix:
  - Perform rightRotate(50).

Local AFTER (after rightRotate(50)):
       (30)
       /  \
     (20) (50)

Full tree AFTER (replacing subtree under 70):
                 (70)
                /     \
             (30)     (90)
            /  \      /  \
         (20) (50) (80) (100)
                 \
                 ( )   # 60 removed

Explanation:
 - Right rotation promotes 30 into 50's previous position.
 - 50 becomes right child of 30; heights updated. The whole tree becomes AVL-balanced.

===============================================================================
CASE 2.B — Left-Right (LR) — leftRotate(80) then rightRotate(90) (example triggered by delete 100)
---------------------------------------------------------------------------------------------------
Full tree BEFORE (example where deletion of 100 causes imbalance at 90):
                 (70)
                /     \
             (50)     (90)
            /  \      /  \
         (30) (60) (80) (100)
         /  \        \
       (20) (40)     (85)

Action that triggers imbalance:
  delete(100)
  - Removing 100 reduces height on 90's right subtree, making left side deeper;
    BF(90) becomes +2.
  - Now look at 90.left = 80 — that node is right-heavy because it has right child 85:
    path from 90 to deeper grandchild is Left -> Right (90 -> 80 -> 85) → LR.

Local BEFORE (focused on 90 subtree after delete 100):
      (90)            <-- unbalanced z
      /
    (80)             <-- left child y
      \
     (85)            <-- right-heavy child x

Fix (two steps):
 1) leftRotate(80)   # rotate around 80 to convert LR into LL
    After step 1 local subtree:
       (85)
       /
     (80)

 2) rightRotate(90)  # now do right rotation on 90
    Final local subtree after both rotations:
       (85)
      /    \
    (80)   (90)

Full tree AFTER (subtree replaced under root 70):
                 (70)
                /     \
             (50)     (85)
            /  \     /    \
         (30) (60) (80)  (90)
         /  \
       (20) (40)

Explanation:
 - Double rotation first corrects the shape at child 80, then balances 90.
 - This matches animation: left on 80 then right on 90.

===============================================================================
CASE 2.C — Right-Right (RR) — LEFT rotation on 50 (example triggered by delete 30)
-----------------------------------------------------------------------------------
Full tree BEFORE (variant  where right subtree is heavier):
                 (70)
                /     \
             (50)     (90)
            /  \      /  \
         (30) (60) (80) (100)
         /  \        \
       (20) (40)     (85)

Action that triggers imbalance:
  delete(30)
  - Removing 30 drops 50's left height significantly; now 50's right subtree
    (60) becomes deeper such that BF(50) = -2 ⇒ Right-Right case if 60 is right-heavy.

Local BEFORE (focused on 50 subtree after delete 30):
     (50)           <-- unbalanced z
       \
       (60)         <-- right child y
         \
         (70?) or (some deeper right) <-- path shows right-right

(For a clean RR example the local shape is:)
     (50)
       \
       (60)
         \
         (70)

Fix:
  - Perform leftRotate(50).

Local AFTER (after leftRotate(50)):
       (60)
      /    \
    (50)  (70)

Full tree AFTER (replace subtree under 70 accordingly):
                 (70)
                /     \
             (60)     (90)
            /  \      /  \
         (50) ...  (80) (100)
         /
       (20)

Explanation:
 - Left rotation promotes 60; 50 becomes left child.
 - This show left rotation movement and final balanced state.

===============================================================================
CASE 2.D — Right-Left (RL) — rightRotate(60) then leftRotate(50)
----------------------------------------------------------------
Full tree BEFORE ( demonstrates RL; we show a variant that matches):
                 (70)
                /     \
             (50)     (90)
            /  \      /  \
         (30) (60) (80) (100)
         /  \   \
       (20) (40) (55)
                   \
                   (??)  # 55 is left child of 60 making a left-heavy 60

Action that triggers imbalance:
  delete(some node on left side) that causes BF(50) to become -2 (right-heavy),
  and 60 (the right child of 50) is itself left-heavy because it has a left child 55.
  So path from 50 to deeper grandchild is Right -> Left (50 -> 60 -> 55) => RL.

Local BEFORE (focused on 50 subtree):
     (50)           <-- unbalanced z (BF = -2)
       \
       (60)         <-- right child y (left-heavy)
       /
     (55)           <-- left child x

Fix (two steps):
 1) rightRotate(60)   # rotate right at y to make y right-heavy
    After step 1 local shape:
       (55)
         \
         (60)

 2) leftRotate(50)    # rotate left at z to finish rebalance
    After step 2:
       (55)
      /    \
    (50)  (60)

Full tree AFTER (subtree under 70 replaced):
                 (70)
                /     \
             (55)     (90)
            /  \      /  \
         (50) (60) (80) (100)
         /  \
       (30) (..)

Explanation:
 - Double rotation converts RL into balanced subtree by first rotating at the child,
   then rotating at the now-unbalanced parent.
 - The animation shows right rotation on 60 followed by left rotation on 50.

===============================================================================
HOW TO DECIDE WHICH CASE (practical checklist)
===============================================================================
1. After deletion, at each ancestor node (starting from parent of deleted node and
   moving up to root), recompute:
      height = 1 + max(height(left), height(right))
      BF = height(left) - height(right)

2. If |BF| <= 1 → continue upward; no rotation at this node.

3. If BF = +2 (left-heavy):
     - if height(left.left) >= height(left.right) → LL → rightRotate(node)
     - else → LR → leftRotate(node.left) then rightRotate(node)

   If BF = -2 (right-heavy):
     - if height(right.right) >= height(right.left) → RR → leftRotate(node)
     - else → RL → rightRotate(node.right) then leftRotate(node)

4. After performing rotation(s) at the unbalanced ancestor, update heights and
   continue walking upward — deletion can create multiple imbalances.

===============================================================================
TIME & SPACE COMPLEXITY (concise)
===============================================================================
- getHeight / BF calc: O(1) time, O(1) space per node (height stored in node).
- Single rotation (left or right): O(1) time, O(1) space.
- Inorder successor (finding min in subtree): O(h) time, O(1) space.
- Deletion (full operation):
    Time: O(h) where h = tree height. For AVL, h = O(log n) ⇒ deletion is O(log n).
    Space: O(h) recursion stack if implemented recursively (or O(1) iterative).

Note: deletion may require multiple rotations while walking up to root, but
each ancestor is visited only once, so total work remains O(h).

===============================================================================
FINAL CHECKLIST (one-liner cheats)
===============================================================================
- Delete with BST rules
- Update heights bottom-up
- If ancestor BF becomes +2/-2, inspect that ancestor's heavier child
  and apply single or double rotation using the **actual** nodes shown in the
 (e.g., rightRotate(50), leftRotate(50), leftRotate(80)+rightRotate(90), etc.)
- Continue upward; deletion can rebalance multiple ancestors.

===============================================================================
END — 
===============================================================================
"""
