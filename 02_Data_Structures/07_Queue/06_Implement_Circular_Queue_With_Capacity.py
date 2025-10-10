# note.py
# ------------------------------------------------------
# 📘 Queue (Circular Queue using Python List with Fixed Capacity)
# ✅ Topic: Implementation, Visual Explanation, and Time/Space Complexity
# ------------------------------------------------------

"""
📌 INTRODUCTION

This file demonstrates the implementation of a **Circular Queue**
using a fixed-size Python list (array-based queue with capacity).

Circular Queue solves two major issues of a normal list-based queue:
    ❌ No left shifting (O(n))
    ❌ No dynamic list reallocation
    ✅ Fixed-size → memory-efficient
    ✅ Wrap-around → reuses freed cells

It follows **FIFO (First In, First Out)** principle.

We maintain two pointers:
    - `start` → front of the queue
    - `top`   → rear (end) of the queue
    
# ---------------------------------------------------------------
# 🧠 CONCEPT SUMMARY
# ---------------------------------------------------------------

Representation:
  [None, None, None, None, None]   ← initially empty (maxSize = 5)
   ↑start=-1         ↑top=-1

Rules:
  1️⃣ Empty queue  → start = top = -1
  2️⃣ Enqueue (Insert)
      - Increment `top` pointer (wrap to 0 if at end)
      - If inserting first element → set start = 0
      - Insert element at `top`
  3️⃣ Dequeue (Remove)
      - Remove element at `start`
      - Increment `start` pointer (wrap to 0 if at end)
      - If last element removed → reset start = top = -1
  4️⃣ Full queue
      - When (top + 1 == start) OR (start == 0 and top + 1 == maxSize)

"""

# ---------------------------------------------------------------
# 🧱 VISUAL OVERVIEW (Queue Structure)
# ---------------------------------------------------------------
"""
Visual (size = 6):

Initial:
+----+----+----+----+----+----+
| __ | __ | __ | __ | __ | __ |
+----+----+----+----+----+----+
  start=-1   top=-1   (empty)

Enqueue(5):
+----+----+----+----+----+----+
| 5  | __ | __ | __ | __ | __ |
+----+----+----+----+----+----+
  start=0   top=0

Enqueue(6):
+----+----+----+----+----+----+
| 5  | 6  | __ | __ | __ | __ |
+----+----+----+----+----+----+
  start=0   top=1

Enqueue(7):
+----+----+----+----+----+----+
| 5  | 6  | 7  | __ | __ | __ |
+----+----+----+----+----+----+
  start=0   top=2

Dequeue() → removes 5:
+----+----+----+----+----+----+
| __ | 6  | 7  | __ | __ | __ |
+----+----+----+----+----+----+
  start=1   top=2

Enqueue(8):
+----+----+----+----+----+----+
| __ | 6  | 7  | 8  | __ | __ |
+----+----+----+----+----+----+
  start=1   top=3

Enqueue(9):
+----+----+----+----+----+----+
| __ | 6  | 7  | 8  | 9  | __ |
+----+----+----+----+----+----+
  start=1   top=4

Dequeue() twice:
+----+----+----+----+----+----+
| __ | __ | __ | 8  | 9  | __ |
+----+----+----+----+----+----+
  start=3   top=4

Enqueue(10) → wraps around:
+----+----+----+----+----+----+
| 10 | __ | __ | 8  | 9  | __ |
+----+----+----+----+----+----+
  start=3   top=0
"""


# ---------------------------------------------------------------
# 🧩 CLASS IMPLEMENTATION
# ---------------------------------------------------------------
class Queue:
    def __init__(self, maxSize):
        """
        Initialize the circular queue with fixed capacity.

        Args:
            maxSize (int): maximum capacity of the queue

        Complexity:
            ⏱️ Time  -> O(1)
            💾 Space -> O(n)
        """
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        """
        Return string representation of queue.

        Example:
            [1, 2, None, None]
        """
        values = [str(x) if x is not None else "__" for x in self.items]
        return " | ".join(values)

    # -----------------------------------------------------------
    # 1️⃣ isFull()
    # -----------------------------------------------------------
    def isFull(self):
        """
        Check if the queue is full.

        Conditions:
            (top + 1 == start)
            OR (start == 0 and top + 1 == maxSize)

        Complexity:
            ⏱️ O(1)
            💾 O(1)
        """
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    # -----------------------------------------------------------
    # 2️⃣ isEmpty()
    # -----------------------------------------------------------
    def isEmpty(self):
        """
        Check if the queue is empty.

        Condition:
            top == -1

        Complexity:
            ⏱️ O(1)
            💾 O(1)
        """
        if self.top == -1:
            return True
        else:
            return False

    # -----------------------------------------------------------
    # 3️⃣ enqueue(value)
    # -----------------------------------------------------------
    def enqueue(self, value):
        """
        Insert an element into the queue.
        
         Steps:
          1. Check if full → return message
          2. If top is at last index → wrap to 0
          3. Else → increment top
          4. If inserting first element → set start = 0
          5. Assign new value at top position

        Example Iteration:
            maxSize = 3
            enqueue(1) -> [1, None, None]  start=0, top=0
            enqueue(2) -> [1, 2, None]     start=0, top=1
            enqueue(3) -> [1, 2, 3]        start=0, top=2 (full)
            dequeue()   -> removes 1 → [None, 2, 3] start=1
            enqueue(4)  -> wraps to index 0 → [4, 2, 3]

        Visual:
            Before enqueue(5):
                +----+----+
                | __ | __ |
                +----+----+
                start=-1 top=-1
            After enqueue(5):
                +----+----+
                | 5  | __ |
                +----+----+
                start=0 top=0

        Complexity:
            ⏱️ O(1)
            💾 O(1)
        """
        if self.isFull():
            return "Queue Is Full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return f"Enqueued {value}"

    # -----------------------------------------------------------
    # 4️⃣ dequeue()
    # -----------------------------------------------------------
    def dequeue(self):
        """
        Remove and return front element from queue.

        Steps:
          1. Check if empty → return message
          2. Store front element
          3. If only one element left → reset queue (start=top=-1)
          4. Else if start at end → wrap to 0
          5. Else → increment start by 1
          6. Set removed position to None

        Example:
            Queue = [1, 2, None]
            dequeue() → returns 1
            Queue = [None, 2, None]
            
        Visual:
            Before dequeue():
                +----+----+
                | 1  | 2  |
                +----+----+
                start=0 top=1
            After dequeue():
                +----+----+
                | __ | 2  |
                +----+----+
                start=1 top=1

        Complexity:
            ⏱️ O(1)
            💾 O(1)
        """
        if self.isEmpty():
            return "Queue is Empty"
        else:
            firstelement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return f"Dequeued {firstelement}"

    # -----------------------------------------------------------
    # 5️⃣ peek()
    # -----------------------------------------------------------
    def peek(self):
        """
        Return the front element without removing it.

        Visual:
            Queue: [None, 4, 5]
            peek() -> 4

        ⏱️ O(1) | 💾 O(1)
        """
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return f"Element at Start of the Queue : {self.items[self.start]}"

    # -----------------------------------------------------------
    # 6️⃣ delete()
    # -----------------------------------------------------------
    def delete(self):
        """
         Delete all elements and reset the queue.

        Steps:
          - Reset all cells to None
          - Set start = top = -1

        Visual:
            Before delete:
                +----+----+
                | 1  | 2  |
                +----+----+
            After delete:
                +----+----+
                | __ | __ |
                +----+----+

        Complexity:
            ⏱️ O(1)
            💾 O(1)
        """
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1
        return "All Elements are deleted"


# ---------------------------------------------------------------
# ▶️ DEMONSTRATION (Step-by-Step Execution)
# ---------------------------------------------------------------
if __name__ == "__main__":
    q = Queue(3)
    print("Initial Queue: ", q)
    print("Is Queue Full?", q.isFull())
    print("Is Queue Empty?", q.isEmpty())

    print("\n▶ Enqueue Operations")
    print(q.enqueue(1), "|", q)
    print(q.enqueue(2), "|", q)
    print(q.enqueue(3), "|", q)
    print(q.enqueue(4), "|", q)

    print("\n▶ Peek Front Element")
    print(q.peek())

    print("\n▶ Dequeue Operations")
    print(q.dequeue(), "|", q)
    print(q.dequeue(), "|", q)
    print(q.dequeue(), "|", q)
    print(q.dequeue(), "|", q)

    print("\n▶ Reusing Queue (Wrap Around)")
    print(q.enqueue(9), "|", q)
    print(q.enqueue(10), "|", q)
    print(q.enqueue(11), "|", q)
    print(q.dequeue(), "|", q)
    print(q.enqueue(12), "|", q)

    print("\n▶ Delete Queue")
    print(q.delete(), "|", q)


# ---------------------------------------------------------------
# 📊 SUMMARY OF TIME & SPACE COMPLEXITY
# ---------------------------------------------------------------
"""
Operation       | Time Complexity | Space Complexity | Description
-----------------------------------------------------------------
Create Queue    | O(1)            | O(n)             | Initialize list of size n
isFull          | O(1)            | O(1)             | Pointer comparison
isEmpty         | O(1)            | O(1)             | top == -1
Enqueue         | O(1)            | O(1)             | Insert rear (with wrap)
Dequeue         | O(1)            | O(1)             | Remove front (with wrap)
Peek            | O(1)            | O(1)             | Access front value
Delete          | O(1)            | O(1)             | Reset all cells to None

🌀 **Key Advantage:**
Circular queue removes the need for shifting elements after dequeue
and avoids Python list resizing overhead — constant-time operations throughout.
"""
