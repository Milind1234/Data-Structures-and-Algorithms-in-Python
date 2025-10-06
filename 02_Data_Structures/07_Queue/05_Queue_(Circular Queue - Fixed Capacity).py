# note.py
# ------------------------------------------------------
# 📘 Queue (Circular Queue - Fixed Capacity)
# ✅ Topic: Implementation, step-by-step visual examples, Time/Space Complexity
# ------------------------------------------------------

"""
📌 INTRODUCTION

This file shows a Circular Queue implemented on a fixed-size Python list.
It includes:
 - Implementation (class)
 - Time & space complexities
 - STEP-BY-STEP VISUAL EXAMPLES (ASCII) that mirror the lecture slides.

We use:
 - items: fixed-size list (None-filled)
 - start: index of front element (-1 when empty)
 - top:   index of rear element (-1 when empty)

Size used in visuals: 6 (indices 0..5).
"""

# ---------------------------------------------------------------
# 🧩 HOW WE WILL VISUALIZE THE QUEUE
# ---------------------------------------------------------------
"""
Notation used in visuals:

  Index row:    [0]  [1]  [2]  [3]  [4]  [5]
  Value row:   [ _ | _ | _ | _ | _ | _ ]   (underscore = None)
  Pointers show which element is front (start) and rear (top)

Example label:
  start = 0, top = 2
  Front (start) -> value at index 0
  Rear  (top)   -> value at index 2

We will show the queue state after each operation exactly like in your slides.
"""

# ---------------------------------------------------------------
# 🏗️ CREATE QUEUE (empty)
# ---------------------------------------------------------------
"""
Operation: Create queue with maxSize = 6

State:
Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [_]  [_]  [_]  [_]  [_]  [_]
Pointers: start = -1, top = -1

(Empty queue — nothing to dequeue/peek)
"""

# ---------------------------------------------------------------
# ⚙️ ENQUEUE SEQUENCE (step-by-step visuals)
# ---------------------------------------------------------------
"""
We perform: enqueue(5), enqueue(6), enqueue(7), enqueue(8), enqueue(3), enqueue(1)

Start from empty. maxSize = 6

1) enqueue(5)
- Since empty: start = 0
- top = ( -1 + 1 ) % 6 = 0

Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [5]  [_]  [_]  [_]  [_]  [_]
Pointers: start = 0, top = 0

2) enqueue(6)
- top = (0 + 1) % 6 = 1

Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [5]  [6]  [_]  [_]  [_]  [_]
Pointers: start = 0, top = 1

3) enqueue(7)
- top = 2

Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [5]  [6]  [7]  [_]  [_]  [_]
Pointers: start = 0, top = 2

4) enqueue(8)
- top = 3

Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [5]  [6]  [7]  [8]  [_]  [_]
Pointers: start = 0, top = 3

5) enqueue(3)
- top = 4

Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [5]  [6]  [7]  [8]  [3]  [_]
Pointers: start = 0, top = 4

6) enqueue(1)
- top = 5  (queue now filled end→start)
Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [5]  [6]  [7]  [8]  [3]  [1]
Pointers: start = 0, top = 5
(At this point, isFull() = True because (top+1)%6 == start)
"""

# ---------------------------------------------------------------
# ⚙️ DEQUEUE SEQUENCE (step-by-step visuals)
# ---------------------------------------------------------------
"""
We will dequeue twice, as in the slides.

Start state before dequeues:
Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [5]  [6]  [7]  [8]  [3]  [1]
Pointers: start = 0, top = 5

1) dequeue() -> removes item at start (index 0 -> 5)
 - Clear or ignore index 0 (we set to None)
 - Since more elements remain, set start = (0 + 1) % 6 = 1

Index:   [0]   [1]  [2]  [3]  [4]  [5]
Value:   [_]   [6]  [7]  [8]  [3]  [1]
Pointers: start = 1, top = 5

2) dequeue() -> removes item at start (index 1 -> 6)
 - Set index 1 = None
 - start = (1 + 1) % 6 = 2

Index:   [0]   [1]   [2]  [3]  [4]  [5]
Value:   [_]   [_]   [7]  [8]  [3]  [1]
Pointers: start = 2, top = 5

Notes:
 - No shifting of remaining items occurred.
 - Indices 0 and 1 are available for future enqueues (wrap-around).
"""

# ---------------------------------------------------------------
# ⚙️ WRAP-AROUND ENQUEUE (showing circular nature)
# ---------------------------------------------------------------
"""
Now enqueue(9). top currently = 5, start = 2, maxSize = 6.

Compute new top:
 top = (5 + 1) % 6 = 0  ← wraps to index 0 (which is free)

After enqueue(9):
Index:   [0]  [1]   [2]  [3]  [4]  [5]
Value:   [9]  [_]   [7]  [8]  [3]  [1]
Pointers: start = 2, top = 0

Continue enqueues could fill index 1 next, then queue becomes full again when
(top+1)%6 == start.
"""

# ---------------------------------------------------------------
# 👁️ PEEK
# ---------------------------------------------------------------
"""
Peek returns value at start without removing it.

Example (after previous operations, start = 2):
Index:   [0]  [1]   [2]  [3]  [4]  [5]
Value:   [9]  [_]   [7]  [8]  [3]  [1]
Pointers: start = 2, top = 0

peek() -> returns items[2] -> 7
Queue remains unchanged.
"""

# ---------------------------------------------------------------
# 🔒 isFull() and isEmpty() (visual checks)
# ---------------------------------------------------------------
"""
isFull() condition:
  (top + 1) % maxSize == start

Examples:
 - When start=0, top=5:
    (5 + 1) % 6 == 0 → True (queue full)

 - When start=2, top=0 (after wrap enqueue(9) above):
    (0 + 1) % 6 == 2 → 1 == 2 → False (not full)

isEmpty() condition:
  start == -1 (or top == -1 in this implementation)

Example (empty initial state):
 Index:   [0]  [1]  [2]  [3]  [4]  [5]
 Value:   [_]  [_]  [_]  [_]  [_]  [_]
 Pointers: start = -1, top = -1
 isEmpty() -> True
"""

# ---------------------------------------------------------------
# 🗑️ DELETE
# ---------------------------------------------------------------
"""
delete() resets the queue entirely:

After delete:
Index:   [0]  [1]  [2]  [3]  [4]  [5]
Value:   [_]  [_]  [_]  [_]  [_]  [_]
Pointers: start = -1, top = -1
"""

# ---------------------------------------------------------------
# ✅ CIRCULAR QUEUE CLASS (Implementation)
# ---------------------------------------------------------------
class CircularQueue:
    def __init__(self, maxSize):
        """
        Initialize circular queue with fixed size.
        """
        self.maxSize = maxSize
        self.items = [None] * maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        """
        Single-line visualization: underscore (_) for None.
        """
        return "[" + ", ".join(str(x) if x is not None else "_" for x in self.items) + "]"

    # Check if Full
    def isFull(self):
        return (self.top + 1) % self.maxSize == self.start

    # Check if Empty
    def isEmpty(self):
        return self.top == -1

    # Enqueue
    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full"
        if self.isEmpty():
            self.start = 0
        self.top = (self.top + 1) % self.maxSize
        self.items[self.top] = value
        return f"Enqueued {value}"

    # Dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        firstElement = self.items[self.start]
        self.items[self.start] = None
        if self.start == self.top:  # queue became empty
            self.start = -1
            self.top = -1
        else:
            self.start = (self.start + 1) % self.maxSize
        return firstElement

    # Peek
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.items[self.start]

    # Delete
    def delete(self):
        self.items = [None] * self.maxSize
        self.start = -1
        self.top = -1
        return "Circular Queue Deleted"

# ---------------------------------------------------------------
# ▶️ DEMONSTRATION (runs when executed directly)
# ---------------------------------------------------------------
if __name__ == "__main__":
    cq = CircularQueue(6)
    print("Create:", cq, "start=", cq.start, "top=", cq.top)
    print(cq.enqueue(5));  print("State:", cq, "start=", cq.start, "top=", cq.top)
    print(cq.enqueue(6));  print("State:", cq, "start=", cq.start, "top=", cq.top)
    print(cq.enqueue(7));  print("State:", cq, "start=", cq.start, "top=", cq.top)
    print(cq.enqueue(8));  print("State:", cq, "start=", cq.start, "top=", cq.top)
    print(cq.enqueue(3));  print("State:", cq, "start=", cq.start, "top=", cq.top)
    print(cq.enqueue(1));  print("State:", cq, "start=", cq.start, "top=", cq.top)

    print("dequeue ->", cq.dequeue()); print("State:", cq, "start=", cq.start, "top=", cq.top)
    print("dequeue ->", cq.dequeue()); print("State:", cq, "start=", cq.start, "top=", cq.top)

    print(cq.enqueue(9)); print("State:", cq, "start=", cq.start, "top=", cq.top)
    print("peek ->", cq.peek())
    print("isFull?", cq.isFull())
    print("isEmpty?", cq.isEmpty())

    print(cq.delete()); print("State after delete:", cq, "start=", cq.start, "top=", cq.top)

# ---------------------------------------------------------------
# 📊 SUMMARY OF TIME & SPACE COMPLEXITIES
# ---------------------------------------------------------------
"""
Operation       | Time Complexity | Space Complexity | Notes
-----------------------------------------------------------------
Create Queue    | O(1)            | O(n)             | allocate list of size n
Enqueue         | O(1)            | O(1)             | index arithmetic, no shifting
Dequeue         | O(1)            | O(1)             | index arithmetic, no shifting
Peek            | O(1)            | O(1)             |
isFull          | O(1)            | O(1)             |
isEmpty         | O(1)            | O(1)             |
Delete Queue    | O(1)            | O(1)             | reassign list reference
"""



# ---------------------------------------------------------------
# 🧩 STRUCTURE & POINTERS
# ---------------------------------------------------------------
"""
Each queue cell visualized as a fixed box layout:

    +----+----+----+----+----+----+
    | 0  | 1  | 2  | 3  | 4  | 5  |  ← Index positions
    +----+----+----+----+----+----+
    |    |    |    |    |    |    |  ← Stored values (None or numbers)
    +----+----+----+----+----+----+
      ↑                     ↑
    start                 top
"""

# ---------------------------------------------------------------
# 🏗️ CREATE QUEUE
# ---------------------------------------------------------------
"""
Step 0️⃣ - Initialization

start = -1 , top = -1 , size = 6

    +----+----+----+----+----+----+
    | _  | _  | _  | _  | _  | _  |
    +----+----+----+----+----+----+
     Empty Queue (all None)
"""

# ---------------------------------------------------------------
# ⚙️ ENQUEUE STEPS
# ---------------------------------------------------------------
"""
Step 1️⃣ - enqueue(5)
start = 0 , top = 0

    +----+----+----+----+----+----+
    | 5  | _  | _  | _  | _  | _  |
    +----+----+----+----+----+----+
     S=0  T=0

Step 2️⃣ - enqueue(6)
start = 0 , top = 1

    +----+----+----+----+----+----+
    | 5  | 6  | _  | _  | _  | _  |
    +----+----+----+----+----+----+
     S=0      T=1

Step 3️⃣ - enqueue(7)
start = 0 , top = 2

    +----+----+----+----+----+----+
    | 5  | 6  | 7  | _  | _  | _  |
    +----+----+----+----+----+----+
     S=0           T=2

Step 4️⃣ - enqueue(8)
start = 0 , top = 3

    +----+----+----+----+----+----+
    | 5  | 6  | 7  | 8  | _  | _  |
    +----+----+----+----+----+----+
     S=0                T=3

Step 5️⃣ - enqueue(3)
start = 0 , top = 4

    +----+----+----+----+----+----+
    | 5  | 6  | 7  | 8  | 3  | _  |
    +----+----+----+----+----+----+
     S=0                     T=4

Step 6️⃣ - enqueue(1)
start = 0 , top = 5

    +----+----+----+----+----+----+
    | 5  | 6  | 7  | 8  | 3  | 1  |
    +----+----+----+----+----+----+
     S=0                          T=5
Queue full: (top+1) % size == start  → (5+1)%6 == 0 ✅
"""

# ---------------------------------------------------------------
# ⚙️ DEQUEUE STEPS
# ---------------------------------------------------------------
"""
Start: start=0 , top=5

1️⃣ dequeue() → removes 5
start moves to 1

    +----+----+----+----+----+----+
    | _  | 6  | 7  | 8  | 3  | 1  |
    +----+----+----+----+----+----+
        S=1                    T=5

2️⃣ dequeue() → removes 6
start moves to 2

    +----+----+----+----+----+----+
    | _  | _  | 7  | 8  | 3  | 1  |
    +----+----+----+----+----+----+
             S=2               T=5
"""

# ---------------------------------------------------------------
# 🔁 WRAP-AROUND ENQUEUE (CIRCULAR MOTION)
# ---------------------------------------------------------------
"""
Now enqueue(9)
top = (5+1) % 6 = 0

    +----+----+----+----+----+----+
    | 9  | _  | 7  | 8  | 3  | 1  |
    +----+----+----+----+----+----+
             S=2               T=0

Next enqueue(10)
top = (0+1)%6 = 1

    +----+----+----+----+----+----+
    | 9  | 10 | 7  | 8  | 3  | 1  |
    +----+----+----+----+----+----+
             S=2               T=1

Now the queue is again FULL because:
 (T+1)%6 == S → (1+1)%6 == 2 ✅
"""

# ---------------------------------------------------------------
# 👁️ PEEK
# ---------------------------------------------------------------
"""
Peek returns the element at `start` (front of queue).

Current queue:
    +----+----+----+----+----+----+
    | 9  | 10 | 7  | 8  | 3  | 1  |
    +----+----+----+----+----+----+
             ↑
            start=2

peek() → returns 7
"""