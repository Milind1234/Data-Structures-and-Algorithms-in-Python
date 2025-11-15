r"""
=====================================================================
📘 AVL Tree — Right-Right (RR) Condition  
Rotation Required → LEFT ROTATION  
=====================================================================

In previous Notes, we learned:

✔ LL Condition → fixed by **Right Rotation**  
✔ LR Condition → fixed by **Left Rotation + Right Rotation**

Now we study:

✔ **RR Condition (Right-Right)**  
✔ Fix = **Left Rotation**  

This note explains:
1️⃣ How RR imbalance is created  
2️⃣ How to detect it  
3️⃣ Left Rotation procedure  
4️⃣ Fully worked example  
5️⃣ Algorithm breakdown (step-by-step with variable values)  
6️⃣ Time & Space Complexity  

=====================================================================
🌳 1) Understanding RR (Right-Right) Condition
=====================================================================

RR occurs when:

    Path to newly inserted node is:
        RIGHT → RIGHT

This causes **right subtree height > left subtree height by 2**.

Therefore AVL tree becomes unbalanced.

To fix it:
👉 Apply **Left Rotation** on the disbalanced node.


=====================================================================
🌱 2) Example 1 — Creating a RR Imbalance
=====================================================================

Initial AVL Tree:

                50
              /     \
            40       60
                      \
                       65
                         \
                          70

Insert **70**:

- 70 > 50 → go right  
- 70 > 60 → go right  
- 70 > 65 → go right → insert as right child

Now subtree rooted at **60** becomes:

              60
                \
                 65
                   \
                    70

Height difference at node 60:
- left = 0
- right = 2  
⟹ **Disbalanced at 60 (RR Case)**

Path to inserted node from 60: RIGHT → RIGHT  
⟹ Confirmed RR Condition.


=====================================================================
🔥 3) Fixing RR → LEFT ROTATION on Disbalanced Node
=====================================================================

We rotate around **60** (the disbalanced node):

Before rotation:

            60
              \
               65
                 \
                  70


After **Left Rotation**:

            65
          /    \
        60      70

The right-heavy subtree becomes balanced.


=====================================================================
🧩 4) RR Example 2 (More Complex)
=====================================================================

Initial tree:

                    50
                 /       \
               40         65
                        /     \
                      60       70
                                 \
                                  75

Insert **75** → inserted as right child of 70.

Check heights bottom-up:

- Node 75 → OK  
- Node 70 → balanced  
- Node 65 → left = 1, right = 2 → still balanced  
- Node 50 → left height = 1, right height = 3 → DIFFERENCE = 2

⟹ Disbalanced node = **50**

Find grandchild with larger height → **70**  
Path from 50 → 65 → 70 = RIGHT → RIGHT  
⟹ **RR Condition**

Fix = Left Rotation at 50

After rotation:

                    65
                 /       \
               50         70
             /   \          \
           40    60         75

Tree becomes perfectly balanced.


=====================================================================
🧠 5) RR Left Rotation — Algorithm (Simple Explanation)
=====================================================================

Goal:
------
Make right child of disbalanced node become the new root.


Left Rotation Algorithm (RR Case)
----------------------------------

Given: disbalancedNode

STEP 1:
    newRoot = disbalancedNode.rightChild

STEP 2:
    disbalancedNode.rightChild =
        disbalancedNode.rightChild.leftChild

STEP 3:
    newRoot.leftChild = disbalancedNode

STEP 4:
    update height(disbalancedNode)

STEP 5:
    update height(newRoot)

STEP 6:
    return newRoot


=====================================================================
🧪 6) RR Algorithm — Step-By-Step Example
=====================================================================

Consider disbalanced subtree:

        30
          \
           40
             \
              50

This is **RR**, so perform **Left Rotation**.

Let:
    disbalancedNode = 30  
    right child = 40  
    right.right child = 50  

Step-By-Step Execution:
-----------------------

STEP 1:
    newRoot = disbalancedNode.rightChild  
            = 40

Now:
    newRoot = 40  
    disbalancedNode = 30

STEP 2:
    disbalancedNode.rightChild = newRoot.leftChild  
    newRoot.leftChild is currently NONE

So:
    30.right = None

STEP 3:
    newRoot.leftChild = disbalancedNode
⟹ 40.left = 30

Tree now looks like:

            40
          /    \
        30      50

STEP 4 & STEP 5:
Update heights:
- height(30) updated
- height(40) updated

STEP 6:
Return newRoot (40)

Final balanced subtree:

            40
          /    \
        30      50

Exactly as expected after RR rotation.


=====================================================================
⏱ 7) Time & Space Complexity
=====================================================================

Left Rotation Complexity:
    Time = O(1)
    Space = O(1)

Because:
- Only 2–3 pointer changes
- Updating heights for just 1–2 nodes


=====================================================================
✅ Summary
=====================================================================

✔ RR occurs when path of insertion is RIGHT → RIGHT  
✔ Causes right-heavy imbalance  
✔ Fix always = **Left Rotation**  
✔ Left Rotation makes right child the new root  
✔ Operation is O(1) and fast  
✔ Ensures AVL remains balanced (height = O(log n))


Next Note:
-------------
➡ Right-Left (RL) Condition (requires Right Rotation + Left Rotation)

=====================================================================
"""
