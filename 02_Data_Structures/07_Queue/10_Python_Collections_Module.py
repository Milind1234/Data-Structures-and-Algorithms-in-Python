# note.py
# ------------------------------------------------------
# 📘 Queue Using Collections Module (deque)
# ✅ Topic: Implementation, Working, and Time/Space Complexity
# ------------------------------------------------------

"""
📌 INTRODUCTION

In previous Notes, we implemented queues using:
   - Python List (no capacity)
   - Python List (Circular Queue with fixed capacity)
   - Linked List

Now in this note, we will learn how to create a Queue using Python’s
**collections module** — specifically, the **deque class**.

In Python, we can create a queue using three modules:
   1️⃣ `collections`  → deque class
   2️⃣ `queue`         → for multithreading (thread-safe)
   3️⃣ `multiprocessing` → for inter-process communication

Here, we focus on `collections.deque` because:
   🔹 It’s simple
   🔹 Very fast (O(1) for enqueue & dequeue)
   🔹 Built into the standard library
"""

# ---------------------------------------------------------------
# 🧠 WHAT IS deque?
# ---------------------------------------------------------------
"""
✅ The `deque` (pronounced “deck”) stands for **Double-Ended Queue**.
   It allows insertion and deletion from **both ends** — left and right — in O(1) time.

✅ Internally implemented as a **Doubly Linked List**:
   - Each element has links to both previous and next nodes.
   - This structure avoids shifting and resizing overhead.

✅ Because it supports fast append and pop operations on both ends,
   it can be used as:
      → Queue (FIFO)
      → Stack (LIFO)

📗 In this note, we use `deque` for a **FIFO Queue** (First In, First Out).
"""

# ---------------------------------------------------------------
# 🧩 deque METHODS FOR QUEUE OPERATIONS
# ---------------------------------------------------------------
"""
1️⃣ deque(maxlen = N)
   → Creates a deque object (queue)
   → Optional maxlen sets capacity (like circular queue)
   → If maxlen = None → queue can grow infinitely (unbounded queue)

2️⃣ append(value)
   → Adds an element to the **right end** (like enqueue)
   → Equivalent to adding to the rear in a normal queue.

3️⃣ popleft()
   → Removes and returns an element from the **left end** (like dequeue)
   → Equivalent to removing from the front of a queue.

4️⃣ clear()
   → Removes all elements from the queue.

5️⃣ maxlen
   → Property that shows the maximum size of the queue.
   → If full, adding a new item discards an element from the opposite end automatically.
"""

# ---------------------------------------------------------------
# ⚙️ IMPLEMENTATION EXAMPLE
# ---------------------------------------------------------------
from collections import deque

# Create a queue with capacity 3
new_Queue = deque(maxlen=3)
print("Initial Queue:", new_Queue)

# Enqueue operations (append)
new_Queue.append(1)
new_Queue.append(2)
new_Queue.append(3)
print("Queue after enqueue:", new_Queue)

# Try to enqueue when queue is full
new_Queue.append(4)
print("Queue after enqueue(4):", new_Queue)

# Dequeue (popleft)
print("Dequeued element:", new_Queue.popleft())
print("Queue after dequeue:", new_Queue)

# Clear the queue
new_Queue.clear()
print("Queue after clear:", new_Queue)

# ---------------------------------------------------------------
# 🧠 STEP-BY-STEP EXPLANATION (With Visualization)
# ---------------------------------------------------------------
"""
🧩 Step 1️⃣: Create Queue
   new_Queue = deque(maxlen=3)
   → []

   Queue created successfully but empty.

🧩 Step 2️⃣: Enqueue 3 elements (1, 2, 3)
   new_Queue.append(1)
   new_Queue.append(2)
   new_Queue.append(3)
   → [1, 2, 3]
   ✅ Adds elements at the right end in FIFO order.

🧩 Step 3️⃣: Enqueue one more element (4)
   Since maxlen = 3 → queue is full.
   🔁 Behavior:
       - The oldest element (leftmost, 1) is automatically removed.
       - New element (4) is added to the right.
   🧠 Result: [2, 3, 4]
   ⚠️ Unlike circular queue, deque does NOT raise an error.
       It silently discards from the opposite end!

🧩 Step 4️⃣: Dequeue element using popleft()
   → Removes and returns leftmost element (2)
   Queue becomes [3, 4]
   Returned: 2

🧩 Step 5️⃣: Clear entire queue
   → new_Queue.clear()
   Queue becomes []
   ✅ Deletes all elements.
"""

# ---------------------------------------------------------------
# 🧾 KEY BEHAVIOR (VERY IMPORTANT)
# ---------------------------------------------------------------
"""
🔸 If `maxlen` is set and queue is full:
      Adding a new element automatically discards the oldest one.
      (It behaves like a circular buffer)
      Example:
         deque([1, 2, 3], maxlen=3)
         append(4) → deque([2, 3, 4])

🔸 If `maxlen` is not set (None):
      Queue grows indefinitely (like normal linked queue).

🔸 append() ↔ enqueue
🔸 popleft() ↔ dequeue
🔸 clear() ↔ delete
🔸 len(queue) == 0 ↔ isEmpty
🔸 len(queue) == maxlen ↔ isFull (manual check)
"""

# ---------------------------------------------------------------
# 📊 TIME & SPACE COMPLEXITY
# ---------------------------------------------------------------
"""
Operation       | Time Complexity | Space Complexity | Description
-----------------------------------------------------------------
Create Queue    | O(1)            | O(n)             | Initialize deque (fixed or dynamic)
Enqueue (append)| O(1)            | O(1)             | Add element at rear
Dequeue (popleft)| O(1)           | O(1)             | Remove element from front
Peek            | O(1)            | O(1)             | Access front element (queue[0])
isEmpty         | O(1)            | O(1)             | len(queue) == 0
Delete Queue    | O(1)            | O(1)             | clear() all elements
"""

# ---------------------------------------------------------------
# 🧩 VISUAL UNDERSTANDING
# ---------------------------------------------------------------
"""
Initial:
   [  ]                (Empty Queue)

After enqueue(1), enqueue(2), enqueue(3):
   [1, 2, 3]           (Full queue)

After enqueue(4) with maxlen=3:
   [2, 3, 4]           (1 discarded ❌)

After dequeue():
   [3, 4]              (Front removed ✅)

After clear():
   [  ]                (All cleared)
"""

# ---------------------------------------------------------------
# ⚖️ COMPARISON WITH OTHER QUEUES
# ---------------------------------------------------------------
"""
Queue Type               | Capacity  | Overflow Behavior           | Implementation       | Performance
---------------------------------------------------------------------------------------------------------
List (No Capacity)       | Unlimited | Grows dynamically           | Python list          | enqueue O(1)*, dequeue O(n)
Circular Queue (List)    | Fixed     | Raises “Queue Full”         | Python list (modulo) | enqueue/dequeue O(1)
Linked List Queue        | Unlimited | Dynamic growth              | Linked List          | enqueue/dequeue O(1)
Deque (collections)      | Fixed/∞   | Discards oldest element ⚠️  | Doubly Linked List   | enqueue/dequeue O(1)
"""

# ---------------------------------------------------------------
# 💡 SUMMARY AND TAKEAWAYS
# ---------------------------------------------------------------
"""
✅ `deque` is part of the **collections module** (no installation required).
✅ Implements queue efficiently using doubly linked list.
✅ append() → enqueue, popleft() → dequeue.
✅ O(1) performance for all major operations.
✅ Can be used as both Queue and Stack.
✅ Great for real-world problems:
   - Task Scheduling
   - Data Stream Buffering
   - Caching (Fixed window)
   - Producer–Consumer patterns

⚠️ Be careful:
   - When maxlen is set, **oldest elements get overwritten silently.**
   - No built-in “isFull” → must manually check with len(queue) == queue.maxlen.

🧠 Best Use Case:
   - When you need a **fast, built-in queue**.
   - When you want a **fixed-size buffer** (like in data streams).
   - When you want **simple FIFO behavior without custom classes**.
"""

# ---------------------------------------------------------------
# 📘 REFERENCE SUMMARY (From note Slides)
# ---------------------------------------------------------------
"""
Fig. 1 — Time & Space Complexity Summary (List vs Circular Queue vs Linked List vs Deque)

Operation        | List(NoCap) | CircularQueue | LinkedList | Deque
---------------------------------------------------------------------
Create Queue     | O(1)        | O(1)          | O(1)       | O(1)
Enqueue          | O(1)*avg    | O(1)          | O(1)       | O(1)
Dequeue          | O(n)        | O(1)          | O(1)       | O(1)
Peek             | O(1)        | O(1)          | O(1)       | O(1)
isEmpty          | O(1)        | O(1)          | O(1)       | O(1)
isFull           | ❌ N/A      | O(1)          | ❌ N/A     | Manual check
Delete Queue     | O(1)        | O(1)          | O(1)       | O(1)
Space Complexity | O(1)        | O(n)          | O(1)       | O(n)
---------------------------------------------------------------------
✅ Deque (collections) provides the best built-in queue option in Python.
"""
