"""
===============================================================================
📘 Topic: Introduction to Binary Search Tree (BST)
===============================================================================

Welcome to a new section: **Binary Search Tree (BST)**.

In this section, you will learn:

✔ What a BST is  
✔ How it differs from a normal Binary Tree  
✔ Why it is faster  
✔ How to create, insert, search, delete using Linked List representation  
✔ Complete operations implementation  

This note focuses on understanding the *concepts* and *motivation* behind BST.

===============================================================================
🌳 What is a Binary Search Tree (BST)?
===============================================================================

A **Binary Search Tree** is a special type of Binary Tree that follows two rules:

1️⃣ **Left Subtree Property**  
    All nodes in the left subtree have values **less than or equal to**
    the parent node.

2️⃣ **Right Subtree Property**  
    All nodes in the right subtree have values **greater than**
    the parent node.

These two rules apply *recursively* to every subtree.

This arrangement allows very fast search, insertion, and deletion.

===============================================================================
🌲 Example BST (from the image)
===============================================================================

                         70
                       /     \
                     50       90
                   /   \     /   \
                 30    60   80   100
                /  \
              20   40

Check the BST properties:

✔ Left subtree of 70 contains: 50,30,60,20,40 → all < 70  
✔ Right subtree of 70 contains: 90,80,100 → all > 70  

Now check node 50:

- Left: 30 (<50)  
- Right: 60 (>50)  

Check node 30:

- Left: 20 (<30)  
- Right: 40 (>30)  

Same applies to node 90:

- Left: 80 (<90)  
- Right: 100 (>90)  

Every node respects the BST rules → therefore this is a valid BST.

===============================================================================
⚡ Why Do We Need a BST?
===============================================================================

A regular **Binary Tree** does NOT store elements in any order.
To search a value, you must check **every** node → **O(n)**.

But a BST is sorted!

This means:
- At each step, you eliminate **half of the tree**.
- Just like binary search.

Search path example for searching 20:

1 → 70 (20 < 70 → go left)  
2 → 50 (20 < 50 → go left)  
3 → 30 (20 < 30 → go left)  
4 → 20 ✔ Found!

Instead of scanning 7 nodes, we only visited 4.

This “halving” continues recursively and results in:

👉 **O(log n)** average time complexity  
(for balanced trees)

This is MUCH faster than a normal binary tree.

===============================================================================
🧠 How Does BST Achieve Fast Operations?
===============================================================================

Because BST is arranged in sorted order:

- You always know which direction to go:
    left → smaller  
    right → larger

This avoids checking unnecessary nodes.

➡ Search:    O(log n)  
➡ Insert:    O(log n)  
➡ Delete:    O(log n)

(If tree becomes skewed, worst case becomes O(n) — like a linked list)

===============================================================================
📌 Binary Tree vs Binary Search Tree (Important Differences)
===============================================================================

| Feature | Binary Tree | Binary Search Tree (BST) |
|--------|--------------|---------------------------|
| **Ordering** | No ordering rule | MUST follow left ≤ parent < right |
| **Search time** | O(n) | O(log n) on average |
| **Insertion rule** | Insert anywhere (level order) | Insert based on value comparison |
| **Deletion** | Harder, uses deepest replacement | Structured → uses successor/predecessor |
| **Use case** | Hierarchical data | Fast searching, dynamic sets, indexing |
| **Speed** | Slower | Much faster for search, insert, delete |
| **Space** | Same | Same |
| **Structure** | Unrestricted | Always sorted |

🔥 KEY POINT  
> BST is not just a binary tree.  
> It is a binary tree with ordering — this ordering gives speed.

===============================================================================
📘 Summary
===============================================================================

✔ A Binary Search Tree is a Binary Tree **with ordering rules**  
✔ Left child ≤ parent and Right child > parent  
✔ This ordering makes search, insert, delete very fast (O(log n))  
✔ BST avoids scanning the entire tree — it eliminates half each time  
✔ BST is extremely useful for:
      • Searching  
      • Maintaining sorted data  
      • Dynamic insert/delete operations  
✔ You will implement BST using a **Linked List (Node-based)** structure

===============================================================================
Next Steps →
--------------
In the next note, we will begin implementing:
➡ Creating a BST  
➡ Inserting nodes properly  
➡ Searching values efficiently  
===============================================================================
"""
