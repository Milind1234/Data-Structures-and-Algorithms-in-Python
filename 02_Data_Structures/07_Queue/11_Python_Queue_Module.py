# note.py
# ------------------------------------------------------
# 📘 Queue Using Python's queue Module
# ✅ Topic: Thread-Safe FIFO Queue Implementation
# ------------------------------------------------------

"""
📌 INTRODUCTION

In the previous notes, we used `collections.deque` to create a simple FIFO queue.
Now, we will use Python’s **queue module** to create a **thread-safe FIFO queue**.

🧠 What makes it special?
   - The `queue` module implements **multi-producer, multi-consumer queues**.
   - It is designed for **threaded programming**, where data needs to be shared safely between threads.
   - It uses internal **locking semantics** to prevent race conditions.
   - All operations (put/get) are safe across multiple threads.

⚙️ Key Feature: Thread-safety
   Unlike `deque`, this queue automatically handles synchronization between threads.
"""

# ---------------------------------------------------------------
# 🧩 TYPES OF QUEUES IN queue MODULE
# ---------------------------------------------------------------
"""
The `queue` module supports 3 types of queues:

1️⃣ FIFO Queue → `queue.Queue`
   - First-In, First-Out
   - Elements are retrieved in the same order as inserted.

2️⃣ LIFO Queue → `queue.LifoQueue`
   - Last-In, First-Out (similar to a Stack)
   - Most recently added element is retrieved first.

3️⃣ Priority Queue → `queue.PriorityQueue`
   - Elements are retrieved based on priority.
   - The lowest value has the highest priority (retrieved first).

In this note, we focus on the **FIFO Queue**.
"""

# ---------------------------------------------------------------
# 🧱 CREATING A FIFO QUEUE
# ---------------------------------------------------------------
"""
We use the `Queue` class constructor:

   ➤ queue.Queue(maxsize)

🔹 `maxsize`: integer specifying the maximum number of items.
   - If maxsize ≤ 0 → queue size is infinite.
   - If maxsize > 0 → queue has a fixed capacity.

🧠 Behavior:
   - If queue is full and a new item is added → the `put()` operation will block (wait)
     until an item is removed.
   - If queue is empty and `get()` is called → it will block until an item is available.
"""

# ---------------------------------------------------------------
# 🧩 IMPORTANT METHODS
# ---------------------------------------------------------------
"""
1️⃣ qsize()
   ➤ Returns the **approximate** size of the queue.
   ⚠️ Approximate because items may be added/removed by other threads.

2️⃣ empty()
   ➤ Returns True if the queue is empty, else False.
   (Equivalent to `isEmpty()` method)

3️⃣ full()
   ➤ Returns True if the queue is full, else False.
   (Equivalent to `isFull()` method)

4️⃣ put(item)
   ➤ Adds (enqueues) an item at the end of the queue.
   (Equivalent to `enqueue()`)

   🔸 If the queue is full, this operation will block until space is available.

5️⃣ get()
   ➤ Removes (dequeues) and returns an item from the front of the queue.
   (Equivalent to `dequeue()`)

   🔸 If the queue is empty, it will block until an item becomes available.

6️⃣ task_done()
   ➤ Indicates that a formerly enqueued task is complete.
   Used by consumer threads to signal completion.

7️⃣ join()
   ➤ Blocks until all items in the queue have been processed.
   Works with `task_done()` to coordinate multi-threaded workloads.
"""

# ---------------------------------------------------------------
# ⚙️ IMPLEMENTATION EXAMPLE
# ---------------------------------------------------------------
import queue as q

# Create a queue with capacity 3
new_Queue = q.Queue(maxsize=3)
print("Initial Queue Size:", new_Queue.qsize())  # Expected 0 (empty)

# Enqueue elements using put()
new_Queue.put(1)
new_Queue.put(2)
new_Queue.put(3)

print("Is Queue Full? :", new_Queue.full())  # Expected True (capacity reached)

# Dequeue first element using get()
print("Dequeued Element:", new_Queue.get())

# Check remaining size
print("Current Queue Size:", new_Queue.qsize())

# ---------------------------------------------------------------
# 🧠 STEP-BY-STEP EXPLANATION (Visualization)
# ---------------------------------------------------------------
"""
🧩 Step 1️⃣ — Create Queue
   new_Queue = q.Queue(maxsize=3)
   → []

   ✅ A thread-safe FIFO queue is created.
   ✅ Capacity = 3 elements.

🧩 Step 2️⃣ — Enqueue Elements (put)
   put(1), put(2), put(3)
   → [1, 2, 3]

   ✅ Elements are added at the end (FIFO).
   ✅ Now, queue is full → full() returns True.

🧩 Step 3️⃣ — Dequeue Element (get)
   get() removes the first element.
   → [2, 3]
   Returned: 1
   ✅ The queue size decreases by 1.

🧩 Step 4️⃣ — Check Size
   qsize() = 2
   ✅ Returns the approximate current number of items.
"""

# ---------------------------------------------------------------
# ⚠️ IMPORTANT CONCURRENCY NOTES
# ---------------------------------------------------------------
"""
🔒 The `queue` module is **thread-safe**:
   - No two threads can modify the queue simultaneously.
   - All operations acquire internal locks automatically.

🧵 Multi-threading use case:
   - One thread produces data using `put()`.
   - Another thread consumes data using `get()`.
   - `task_done()` and `join()` help synchronize the completion of all tasks.

⚙️ Example Workflow (Producer–Consumer):
   Producer Thread:
       queue.put(item)
   Consumer Thread:
       item = queue.get()
       process(item)
       queue.task_done()
   Main Thread:
       queue.join()  → waits until all items are processed.
"""

# ---------------------------------------------------------------
# 📊 TIME & SPACE COMPLEXITY
# ---------------------------------------------------------------
"""
Operation       | Time Complexity | Space Complexity | Description
-----------------------------------------------------------------
Create Queue    | O(1)            | O(n)             | Initializes queue buffer
Enqueue (put)   | O(1)            | O(1)             | Add element at end
Dequeue (get)   | O(1)            | O(1)             | Remove element from front
Peek (via get+putback)* | O(1)   | O(1)             | Not directly supported
isEmpty         | O(1)            | O(1)             | Check queue empty
isFull          | O(1)            | O(1)             | Check queue full
Delete Queue    | O(1)            | O(1)             | Implicit garbage collection
task_done/join  | O(1)            | O(1)             | Synchronization helpers

🧠 *Note:
There is no direct "peek" method — you must get() and then re-put() if you want to preview.
"""

# ---------------------------------------------------------------
# ⚖️ COMPARISON WITH PREVIOUS QUEUE TYPES
# ---------------------------------------------------------------
"""
Queue Type                | Thread-Safe | Capacity | Behavior on Full     | Implementation   | Performance
---------------------------------------------------------------------------------------------------------
List (No Capacity)        | ❌ No       | Infinite | Grows dynamically     | Python List      | enqueue O(1)*, dequeue O(n)
Circular Queue (List)     | ❌ No       | Fixed    | Raises Queue Full     | Python List      | O(1)
Linked List Queue         | ❌ No       | Dynamic  | Dynamic growth        | Linked List      | O(1)
Deque (collections)       | ❌ No       | Fixed/∞  | Overwrites oldest ⚠️  | Doubly LinkedList| O(1)
Queue (queue module)      | ✅ Yes      | Fixed/∞  | Blocks until space 🧵 | Thread-safe Lock | O(1)
"""

# ---------------------------------------------------------------
# 🧠 KEY TAKEAWAYS
# ---------------------------------------------------------------
"""
✅ The `queue` module provides a **thread-safe queue** for concurrent programs.
✅ Ideal for **Producer–Consumer** or **Task Scheduling** problems.
✅ Supports FIFO, LIFO, and Priority Queues.
✅ Built-in methods like `task_done()` and `join()` simplify thread synchronization.

⚠️ Points to Remember:
   - `put()` and `get()` can **block** the thread if queue is full/empty.
   - `qsize()` is approximate (not exact when used by multiple threads).
   - No direct `peek()` method.
   - For non-threaded applications, prefer `deque` (simpler and faster).

💡 Use Case Examples:
   - Threaded web crawlers
   - Asynchronous task queues
   - Data pipelines with background workers
   - Producer–Consumer job handling
"""

# ---------------------------------------------------------------
# 📘 SUMMARY TABLE (From note Slide)
# ---------------------------------------------------------------
"""
Fig. 1 → Queue Module (FIFO Queue)

Operation    | Description                        | Equivalent To
---------------------------------------------------------------
Queue()      | Create FIFO Queue (thread-safe)    | Constructor
put(x)       | Add to end (waits if full)         | enqueue()
get()        | Remove from front (waits if empty) | dequeue()
qsize()      | Returns approximate queue size      | length()
empty()      | Returns True if queue empty         | isEmpty()
full()       | Returns True if queue full          | isFull()
task_done()  | Mark a task as complete             | (thread sync)
join()       | Wait until all tasks complete       | (thread sync)

✅ All operations are O(1) and thread-safe.
"""
