r"""
📘 Topic: AVL Tree — Insertion (Case 1: No Rotation, Case 2: LL Rotation)
=========================================================================

In this Note, we learn:

1️⃣ When rotation is NOT required  
2️⃣ When rotation IS required  
3️⃣ LL (Left-Left) Condition  
4️⃣ Right Rotation (LL Fix)  
5️⃣ Working algorithm + example  
6️⃣ Time & Space Complexity  


=====================================================================
🌳 1) Understanding AVL Insertion
=====================================================================

When inserting a node in an AVL Tree:

👉 **Case A — Rotation is NOT required**  
👉 **Case B — Rotation IS required**  

AVL Rule:
---------
    | height(left subtree) - height(right subtree) | <= 1

If this difference becomes **2**, the tree is **unbalanced**.

Four types of imbalances:
1. LL  (Left Left)  
2. LR  (Left Right)  
3. RR  (Right Right)  
4. RL  (Right Left)

This note covers **LL condition**.

=====================================================================
🌿 2) Case A: Rotation NOT Required
=====================================================================

Insertion works exactly like BST insertion.

Example:

Insert 75:

Before inserting 75:

               70
            /       \
         50          90
       /   \       /     \
     30    60    80      100
    /  \
   20  40

After Inserting 75:


               70
            /       \
         50          90
       /   \       /     \
     30    60    80      100
    /  \.       /
   20  40.    75

Path:
- 75 > 70 → go right  
- 75 < 90 → left  
- 75 < 80 → left → insert  

Tree remains balanced → **No rotation required**.

=====================================================================
🔥 3) Case B: Rotation Required (LL Example)
=====================================================================

Insert **10**:


                   70
                /      \
               /        \
             50         90
           /   \      /    \
         30    60   80     100
        /
      20

Path:
- 10 < 70  
- 10 < 50  
- 10 < 30  
- 10 < 20 → insert  

Tree becomes:

       30 (unbalanced)
      /
    20
   /
 10

Height difference at node 30:
- left = 2  
- right = 0  
- difference = 2 → **IMBALANCED**

Direction to inserted node:
LEFT → LEFT  
So this is **LL condition**.

Fix = **Right Rotation**.

=====================================================================
🔄 4) LL Rotation — Concept (Right Rotation)
=====================================================================

Before Rotation:

           30
         /
       20
      /
    10

After RIGHT rotation:

           20   ← new root
         /    \
       10      30

Entire tree becomes balanced.

=====================================================================
🧩 5) LL Rotation — Algorithm 
=====================================================================

Right Rotation Algorithm (LL Case)
----------------------------------

Given: disbalancedNode

STEP 1:
    newRoot = disbalancedNode.leftChild

STEP 2:
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild

STEP 3:
    newRoot.rightChild = disbalancedNode

STEP 4:
    update height(disbalancedNode)

STEP 5:
    update height(newRoot)

STEP 6:
    return newRoot

This restores AVL balance during LL condition.

=====================================================================
🧪 6) LL Example — Step-by-Step Rotation
=====================================================================

Before rotation:

         30
       /
     20
    /
  10

Step-by-step:

1️⃣ newRoot = 20  
2️⃣ 30.left = 20.right (None)  
3️⃣ 20.right = 30  

After rotation:

         20
       /    \
     10      30

Tree is now balanced.

=====================================================================
⏱ 7) Time & Space Complexity
=====================================================================

Right Rotation:
    Time  → O(1)
    Space → O(1)

Because rotation adjusts only 2–3 pointers and updates two heights.

=====================================================================
✅ Summary
=====================================================================

✔ AVL insertion = BST insert + balance check  
✔ When height difference becomes 2 → rotation needed  
✔ LL condition happens when:
   - Path to inserted node is LEFT → LEFT  

✔ LL is fixed by **Right Rotation**  
✔ Rotation keeps AVL height = O(log n)  

Next Notes:
--------------
➡ Left-Right (LR) Condition  
➡ Right-Right (RR) Condition  
➡ Right-Left (RL) Condition  
➡ Full AVL Insert() Implementation  

=====================================================================
"""
