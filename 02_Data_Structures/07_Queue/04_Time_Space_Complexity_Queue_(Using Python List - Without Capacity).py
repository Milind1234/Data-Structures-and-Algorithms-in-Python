# note.py
# ------------------------------------------------------
# 📘 Queue - Notes File
# ✅ Topic: Time and Space Complexity of Queue (Using Python List - Without Capacity)
# ------------------------------------------------------

"""
📌 Problem: Time and Space Complexity of Queue (Python List)

This file summarizes the **time complexity** and **space complexity**
for the most common operations on a queue implemented using a Python list
(without setting a size limit).

✅ Queue follows **FIFO (First In, First Out)** principle.
✅ In Python list:
   - enqueue() uses append() → O(1) amortized
   - dequeue() uses pop(0) → O(n) (due to element shifting)
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
Queue → Linear data structure that follows **FIFO** rule.
- Insertions (enqueue) happen at the **rear**.
- Deletions (dequeue) happen at the **front**.
- Implemented here using Python list (no fixed capacity).

⚙️ Internal Representation:
    FRONT → [10, 20, 30] ← REAR
    - enqueue(40) → append(40)
    - dequeue()   → pop(0)

🧩 Important Notes:
- list.append() → O(1) amortized (fast)
- list.pop(0)   → O(n) (slow due to left shift)
"""

# ---------------------------------------------------------------
# 📝 Time & Space Complexities
# ---------------------------------------------------------------
"""
Operation           Time Complexity        Space Complexity
------------------------------------------------------------
Create              O(1)                   O(1)
Enqueue             O(1)*                  O(1)
Dequeue             O(n)                   O(1)
Peek                O(1)                   O(1)
isEmpty             O(1)                   O(1)
Size                O(1)                   O(1)
Delete              O(1)                   O(1)
__str__ (print)     O(n)                   O(n)

* enqueue() is amortized O(1); resizing may take O(n) occasionally.
"""

# ---------------------------------------------------------------
# ✅ Explanation of Each Operation
# ---------------------------------------------------------------
"""
1. Create
   - Initialize an empty Python list.
   - Time = O(1), Space = O(1)

2. Enqueue
   - Append element at end of list (rear of queue).
   - Time = Amortized O(1), Space = O(1)
   - Worst case O(n) if internal resizing occurs.

3. Dequeue
   - Remove element from front using pop(0).
   - Time = O(n), Space = O(1)
   - Because each element shifts one step left.

4. Peek
   - Return element at index 0 (front) without removing it.
   - Time = O(1), Space = O(1)

5. isEmpty
   - Check if list is empty (len(list) == 0).
   - Time = O(1), Space = O(1)

6. Size
   - Return len(list).
   - Time = O(1), Space = O(1)

7. Delete
   - Set list reference to None (delete all elements).
   - Time = O(1), Space = O(1)

8. __str__
   - Convert all elements to strings and join.
   - Time = O(n), Space = O(n)
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example for Operations
# ---------------------------------------------------------------
"""
Queue (using list): []

1. Enqueue(10):
   [10]
   Time = O(1)

2. Enqueue(20):
   [10, 20]
   Time = O(1)

3. Enqueue(30):
   [10, 20, 30]
   Time = O(1)

4. Peek():
   Returns 10 (queue unchanged)
   Time = O(1)

5. Dequeue():
   Removes 10
   Result: [20, 30]
   Time = O(n)

6. Size():
   Returns 2
   Time = O(1)

7. Delete():
   Queue = None
   Time = O(1)
"""

# ---------------------------------------------------------------
# 📊 Summary Table (as Python dict)
# ---------------------------------------------------------------
queue_complexities = {
    "Create":    {"time": "O(1)", "space": "O(1)"},
    "Enqueue":   {"time": "O(1)*", "space": "O(1)"},
    "Dequeue":   {"time": "O(n)", "space": "O(1)"},
    "Peek":      {"time": "O(1)", "space": "O(1)"},
    "isEmpty":   {"time": "O(1)", "space": "O(1)"},
    "Size":      {"time": "O(1)", "space": "O(1)"},
    "Delete":    {"time": "O(1)", "space": "O(1)"},
    "__str__":   {"time": "O(n)", "space": "O(n)"}
}

# ---------------------------------------------------------------
# ▶️ DEMO (Optional)
# ---------------------------------------------------------------
if __name__ == "__main__":
    from pprint import pprint
    print("Time and Space Complexity of Queue (Python List) Operations:\n")
    pprint(queue_complexities)

"""
✅ SUMMARY:
- Queue uses Python list for internal storage.
- Follows FIFO rule.
- enqueue() → O(1) amortized using append()
- dequeue() → O(n) due to shifting.
- All other operations → O(1).
- Best used for learning; use collections.deque for O(1) dequeue.
"""
