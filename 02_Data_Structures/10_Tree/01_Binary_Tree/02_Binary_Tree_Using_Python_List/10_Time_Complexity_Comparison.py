"""
===============================================================================
📘 Topic: Binary Tree — Python List vs Linked List (Comparison Note)
===============================================================================

This note compares how Binary Trees behave when implemented using:

1️⃣ Python List (Array-based)  
2️⃣ Linked List (Node & Pointers)

Both implementations support the same operations,
but their **time complexity**, **space usage**,  
and **practical behavior** differ.

===============================================================================
🌳 1. Overview
===============================================================================

Binary Tree can be stored in two ways:

A) **Python List (Fixed-size Array)**
   - Index 0 is unused.
   - Parent → index = i  
     Left Child  = 2i  
     Right Child = 2i + 1  
   - Tree must have a MAX size fixed earlier.

B) **Linked List (Pointers)**
   - Each node holds: data, left pointer, right pointer.
   - Tree grows dynamically (no fixed capacity).

===============================================================================
📊 2. Time & Space Complexity Comparison Table
===============================================================================

Operation                       | Python List (Fixed Array)         | Linked List
------------------------------- | ---------------------------------- | -------------------
Create Binary Tree              | Time: O(1)   | Space: O(n)        | Time: O(1) | Space: O(1)
Insert a Node                   | Time: O(1)   | Space: O(1)        | Time: O(n) | Space: O(n)
Delete a Node                   | Time: O(n)   | Space: O(1)        | Time: O(n) | Space: O(n)
Search for a Node               | Time: O(n)   | Space: O(1)        | Time: O(n) | Space: O(n)
Traverse Binary Tree            | Time: O(n)   | Space: O(1)        | Time: O(n) | Space: O(n)
Delete Entire Binary Tree       | Time: O(1)   | Space: O(1)        | Time: O(1) | Space: O(1)
Space Efficient?                | ❌ No (fixed space used)           | ✅ Yes

===============================================================================
🧠 3. Why the Differences?
===============================================================================

🔹 **Python List (Array-based)**  
- Requires allocating a fixed-size list → O(n) memory immediately.  
- Insert is O(1) (place at next index).  
- Delete & search require scanning list → O(n).  
- May waste space if tree is not full.

🔹 **Linked List Tree**  
- Nodes created only when needed → memory efficient.  
- Insert requires finding first empty position → O(n).  
- Search & delete require traversal → O(n).  
- Good when tree grows dynamically.

===============================================================================
📌 4. Practical Usage Guide
===============================================================================

Use **Python List** when:  
✔ Tree height is small  
✔ Maximum size is known  
✔ Fast insertion is needed  
✔ You want simple index formulas

Use **Linked List** when:  
✔ Tree is dynamic / unbounded  
✔ Memory efficiency is required  
✔ You want flexible growth  
✔ You prefer pointer-based structures

===============================================================================
🏁 5. Summary
===============================================================================

- Both implementations support the same core operations.  
- **Array-based tree is faster for INSERT**, but uses more memory.  
- **Linked List tree is more flexible and space efficient**.  
- Traversal and search are **O(n)** for both.

===============================================================================
End of Notes
===============================================================================
"""
