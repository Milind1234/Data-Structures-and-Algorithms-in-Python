# note.py
# ------------------------------------------------------
# 📘 Queue Using multiprocessing Module
# ✅ Topic: Inter-Process FIFO Queue Implementation
# ------------------------------------------------------

"""
📌 INTRODUCTION

In the previous notes, we implemented queues using:
   - Python list (with & without capacity)
   - Linked List
   - collections.deque
   - queue module (for multithreading)

Now in this note, we will use Python’s **multiprocessing module**
to implement a **FIFO Queue** that can be shared **between multiple processes**.

🧠 Key Idea:
   - Similar to the `queue` module, but designed for **multi-processing** instead of **multi-threading**.
   - Enables data sharing between processes running in **parallel**.
   - All items stored must be **picklable objects** (i.e., serializable).
"""

# ---------------------------------------------------------------
# 🧩 WHY multiprocessing.Queue ?
# ---------------------------------------------------------------
"""
✅ `multiprocessing.Queue` allows processes to communicate safely.
✅ Data placed in the queue can be accessed by multiple worker processes.
✅ Each process gets its own Python memory space, so normal variables can’t be shared.
   But this Queue acts as a **shared bridge** between them.

🚀 Example Use Case:
   - Producer process puts data into the queue.
   - Consumer process retrieves and processes it.
   - Useful in **parallel processing pipelines** and **task distribution**.
"""

# ---------------------------------------------------------------
# 🧩 CREATING A MULTIPROCESSING QUEUE
# ---------------------------------------------------------------
"""
We import the `Queue` class from the multiprocessing module:

   ➤ from multiprocessing import Queue

Then we initialize it:
   ➤ q = Queue(maxsize = 3)

📗 Parameters:
   - maxsize: Maximum number of elements the queue can hold.
              If maxsize <= 0 → queue size is unlimited.

✅ Similar to queue.Queue, but it’s process-safe (uses inter-process locks).
"""

# ---------------------------------------------------------------
# ⚙️ IMPLEMENTATION EXAMPLE
# ---------------------------------------------------------------
from multiprocessing import Queue

# Create a queue with capacity 3
custom_queue = Queue(maxsize=3)

# Enqueue elements
custom_queue.put(1)
custom_queue.put(2)
custom_queue.put(3)

# Dequeue (FIFO order)
print("Dequeued Element:", custom_queue.get())

# ---------------------------------------------------------------
# 🧠 STEP-BY-STEP VISUALIZATION
# ---------------------------------------------------------------
"""
🧩 Step 1️⃣ — Create Queue
   custom_queue = Queue(maxsize=3)
   → []

   ✅ An inter-process communication queue is created.
   ✅ Can safely pass data between processes.

🧩 Step 2️⃣ — Enqueue Elements
   put(1), put(2), put(3)
   → [1, 2, 3]
   ✅ Inserts data into the shared queue (process-safe).

🧩 Step 3️⃣ — Dequeue Elements
   get() → Removes & returns the first inserted element.
   → [2, 3]
   Returned value: 1
   ✅ FIFO order maintained.
"""

# ---------------------------------------------------------------
# 🔍 METHODS AVAILABLE (Same as queue.Queue)
# ---------------------------------------------------------------
"""
✅ put(item)
   → Adds an element to the end of queue (blocks if full).

✅ get()
   → Removes and returns element from front of queue (blocks if empty).

✅ qsize()
   → Returns approximate number of items in the queue.

✅ empty()
   → Returns True if queue empty, else False.

✅ full()
   → Returns True if queue full, else False.

⚠️ Unlike queue.Queue:
   ❌ No task_done()
   ❌ No join()
   These methods are not supported in multiprocessing.Queue.
"""

# ---------------------------------------------------------------
# ⚙️ BEHIND THE SCENES — HOW IT WORKS
# ---------------------------------------------------------------
"""
🔸 The `multiprocessing.Queue` uses **pipes and locks** internally.
🔸 Data is serialized using the `pickle` module when transferred between processes.
🔸 Each process runs in its own memory space — so this queue acts as a bridge.
🔸 Safe to use with multiple producers and consumers.

🧠 Conceptually:
   ┌──────────────┐     ┌──────────────┐
   │ Producer #1  │     │ Consumer #1  │
   │  put(data)   │ --> │  get(data)   │
   └──────────────┘     └──────────────┘
   ┌──────────────┐     ┌──────────────┐
   │ Producer #2  │     │ Consumer #2  │
   │  put(data)   │ --> │  get(data)   │
   └──────────────┘     └──────────────┘

✅ Data flows through this queue — safely and in FIFO order.
"""

# ---------------------------------------------------------------
# 📊 TIME & SPACE COMPLEXITY
# ---------------------------------------------------------------
"""
Operation       | Time Complexity | Space Complexity | Description
-----------------------------------------------------------------
Create Queue    | O(1)            | O(n)             | Create shared memory queue
Enqueue (put)   | O(1)            | O(1)             | Add element at rear
Dequeue (get)   | O(1)            | O(1)             | Remove element from front
isEmpty (empty) | O(1)            | O(1)             | Check if queue empty
isFull (full)   | O(1)            | O(1)             | Check if queue full
Delete Queue    | O(1)            | O(1)             | Implicit garbage collection
"""

# ---------------------------------------------------------------
# ⚖️ COMPARISON: queue.Queue vs multiprocessing.Queue
# ---------------------------------------------------------------
"""
Feature                  | queue.Queue (Threading) | multiprocessing.Queue (Processes)
---------------------------------------------------------------------------------------
Use Case                 | Multi-threading         | Multi-processing
Data Sharing             | Between threads         | Between processes
Synchronization          | Thread-safe locks       | Process-safe locks
Data Type Support        | Any object              | Picklable objects only
task_done / join         | ✅ Supported
"""