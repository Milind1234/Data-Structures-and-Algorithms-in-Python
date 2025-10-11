# note.py
# ------------------------------------------------------
# 📘 Queue Comparison (List vs Circular List vs Linked List)
# ✅ Topic: Time and Space Complexity Comparison & Use Case Selection
# ------------------------------------------------------

"""
📌 INTRODUCTION

In previous notes, we created and analyzed **three different types of Queues**:
    1️⃣ Queue using Python List (No Capacity Limit)
    2️⃣ Queue using Python List with Capacity (Circular Queue)
    3️⃣ Queue using Linked List

This note compares them based on **time complexity**, **space complexity**, and **practical usage**.

The goal is to understand:
   ➜ Which queue performs better in which situation  
   ➜ How time and space trade-offs differ among them  
"""

# ---------------------------------------------------------------
# 🧩 QUEUE TYPE 1 — Python List (No Capacity Limit)
# ---------------------------------------------------------------
"""
✅ Description:
   - Implemented using a regular Python list.
   - Uses built-in `append()` for enqueue and `pop(0)` for dequeue.

⚙️ Mechanism:
   Enqueue → list.append(value)
   Dequeue → list.pop(0)

⚠️ Problems:
   - When popping from index 0 → shifts all remaining elements left → O(n)
   - When the list grows beyond its internal capacity → Python reallocates memory → O(n)

🧠 Visualization:
   Enqueue (append at end):
       [10, 20, 30]  → append(40) → [10, 20, 30, 40]

   Dequeue (remove from front):
       [10, 20, 30, 40] → pop(0) → [20, 30, 40]
       (elements shifted left ⬅️)

⏱️ Time & Space:
   Operation           Time       Space
   --------------------------------------
   Create Queue        O(1)       O(1)
   Enqueue             O(1)*avg   O(1)
   Dequeue             ❌ O(n)    O(1)
   Peek                O(1)       O(1)
   isEmpty             O(1)       O(1)
   isFull              ❌ N/A     -
   Delete Queue        O(1)       O(1)

📉 Conclusion:
   - Simple, but **inefficient for large queues**.
   - Suitable only for **small, temporary queues**.
"""

# ---------------------------------------------------------------
# 🌀 QUEUE TYPE 2 — Circular Queue (Fixed Capacity)
# ---------------------------------------------------------------
"""
✅ Description:
   - Uses Python list of fixed size.
   - Two pointers: `start` (front) and `top` (rear).
   - Wraps around using modular arithmetic (circular behavior).

⚙️ Mechanism:
   Enqueue → insert at `(top + 1) % maxSize`
   Dequeue → move `start` forward `(start + 1) % maxSize`

🧠 Visualization:

   Initial (size=6):
       [None, None, None, None, None, None]
       start = -1, top = -1

   After enqueue(5), enqueue(6), enqueue(7):
       [5, 6, 7, None, None, None]
       start = 0, top = 2

   After dequeue():
       [None, 6, 7, None, None, None]
       start = 1, top = 2

   Circular Insert (wrap around):
       when top reaches end → top = 0

⏱️ Time & Space:
   Operation           Time       Space
   --------------------------------------
   Create Queue        O(1)       O(n)
   Enqueue             O(1)       O(1)
   Dequeue             O(1)       O(1)
   Peek                O(1)       O(1)
   isEmpty             O(1)       O(1)
   isFull              O(1)       O(1)
   Delete Queue        O(1)       O(1)

📈 Conclusion:
   - **Much faster** than simple list-based queue.
   - Slightly higher space usage due to preallocated list.
   - Ideal for **fixed-size applications** (e.g. CPU scheduling, buffering, streaming).
"""

# ---------------------------------------------------------------
# 🔗 QUEUE TYPE 3 — Linked List Queue
# ---------------------------------------------------------------
"""
✅ Description:
   - Implemented using singly linked list nodes.
   - No fixed capacity → dynamic size.
   - Uses two pointers: `head` (front) and `tail` (rear).

⚙️ Mechanism:
   Enqueue → attach new node at tail  
   Dequeue → remove node from head  

🧠 Visualization:

   Initial:
       Head → None
       Tail → None

   After enqueue(10), enqueue(20), enqueue(30):
       Head → [10|•] → [20|•] → [30|/]
       Tail ---------------------^

   After dequeue():
       Head → [20|•] → [30|/]
       Tail -----------^

   Delete:
       Head = None, Tail = None

⏱️ Time & Space:
   Operation           Time       Space
   --------------------------------------
   Create Queue        O(1)       O(1)
   Enqueue             O(1)       O(1)
   Dequeue             O(1)       O(1)
   Peek                O(1)       O(1)
   isEmpty             O(1)       O(1)
   isFull              ❌ N/A     -
   Delete Queue        O(1)       O(1)

📗 Conclusion:
   - Most **efficient overall** (O(1) everywhere).
   - Grows dynamically (no memory reallocation).
   - Slightly more complex to implement.
   - Ideal for large-scale or dynamic data processing.
"""

# ---------------------------------------------------------------
# 📊 COMPARISON TABLE — Time & Space Complexity
# (Refer to Fig. 1: Time and Space complexity Queue)
# ---------------------------------------------------------------

queue_complexity = {
    "List (No Capacity Limit)": {
        "Create":    "O(1)",
        "Enqueue":   "O(1)*avg",
        "Dequeue":   "O(n)",
        "Peek":      "O(1)",
        "isEmpty":   "O(1)",
        "isFull":    "N/A",
        "Delete":    "O(1)",
        "Space":     "O(1)"
    },
    "List (Circular Queue)": {
        "Create":    "O(1)",
        "Enqueue":   "O(1)",
        "Dequeue":   "O(1)",
        "Peek":      "O(1)",
        "isEmpty":   "O(1)",
        "isFull":    "O(1)",
        "Delete":    "O(1)",
        "Space":     "O(n)"
    },
    "Linked List Queue": {
        "Create":    "O(1)",
        "Enqueue":   "O(1)",
        "Dequeue":   "O(1)",
        "Peek":      "O(1)",
        "isEmpty":   "O(1)",
        "isFull":    "N/A",
        "Delete":    "O(1)",
        "Space":     "O(1)"
    }
}

if __name__ == "__main__":
    from pprint import pprint
    print("🧮 Queue Time and Space Complexity Comparison:\n")
    pprint(queue_complexity)

# ---------------------------------------------------------------
# 🧠 FINAL COMPARISON SUMMARY
# ---------------------------------------------------------------
"""
Queue Type                Advantages                                 Disadvantages                        Best For
----------------------------------------------------------------------------------------------------------------------------
List (No Capacity)        ✅ Simple, built-in                        ❌ Slow dequeue (O(n))                Small/temporary queues
Circular Queue            ✅ Fast O(1) operations                    ❌ Fixed capacity, O(n) space         Limited-size systems (buffers)
Linked List Queue         ✅ O(1) for all ops, dynamic size          ❌ More complex implementation         Large dynamic workloads

💡 Recommendation:
- For small data → Simple List Queue
- For performance-critical fixed-size tasks → Circular Queue
- For dynamic and scalable systems → Linked List Queue
"""
