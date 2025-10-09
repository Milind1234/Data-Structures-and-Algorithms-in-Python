# note.py
# ------------------------------------------------------
# 📘 Queue (Linked List Implementation)
# ✅ Topic: Theory, Working Process & Visualization
# ------------------------------------------------------

"""
📌 INTRODUCTION

In the previous Notes, we learned about the Circular Queue using a fixed-size Python list.
In this Note, we explore how to implement a **Queue using a Linked List**.

Unlike array-based queues, this queue:
    ✅ Does NOT have a fixed capacity.
    ✅ Dynamically grows as we add elements.
    ✅ Does NOT need index-based shifting or wrapping.
    ❌ But requires slightly more memory (due to node pointers).

Each element (node) in the queue contains:
    - value (data)
    - reference (pointer) to the next node
"""

# ---------------------------------------------------------------
# 🧱 VISUAL OVERVIEW: Queue using Linked List
# ---------------------------------------------------------------
"""
Initial empty queue:

   head → None
   tail → None

There are no nodes yet.

   +-------+      +-------+
   | Head  | ---> | None  |
   +-------+      +-------+
   | Tail  | ---> | None  |
   +-------+      +-------+

Each new node will be added at the tail end.
Each dequeue removes a node from the head end.
"""

# ---------------------------------------------------------------
# ⚙️ CREATION OF QUEUE (Using Linked List)
# ---------------------------------------------------------------
"""
1️⃣ Create an object of SinglyLinkedList class.
   - It creates blank `head` and `tail` references.
   - Initially, both head and tail point to None.

   head = None
   tail = None

   Queue is empty.
"""

# ---------------------------------------------------------------
# 🟩 ENQUEUE OPERATION (Insert Element)
# ---------------------------------------------------------------
"""
Purpose:
   Insert (enqueue) a new element at the **end** of the queue.

Steps:
1️⃣ Create a new node with given value.
2️⃣ If queue is empty:
      - set head = newNode
      - set tail = newNode
3️⃣ If not empty:
      - link the old tail’s `next` pointer to newNode
      - update tail to point to newNode

-------------------------------------------------------------
🧩 VISUALIZATION EXAMPLE
-------------------------------------------------------------

Step 1: Enqueue(1)
   Create node(value=1)
   head → 111 (Node1)
   tail → 111 (Node1)

   +-------+      +----------+
   | head  | ---> | value=1  | ---> None
   +-------+      +----------+
   | tail  | -----^

Step 2: Enqueue(2)
   Create node(value=2)
   Node1.next → 222
   tail → 222

   +-------+      +----------+      +----------+
   | head  | ---> | value=1  | ---> | value=2  | ---> None
   +-------+      +----------+      +----------+
                      |                  ^
                      |__________________|
                          (updated tail)

Step 3: Enqueue(3)
   Create node(value=3)
   Node2.next → 333
   tail → 333

   +-------+      +----------+      +----------+      +----------+
   | head  | ---> | value=1  | ---> | value=2  | ---> | value=3  | ---> None
   +-------+      +----------+      +----------+      +----------+
"""

# ---------------------------------------------------------------
# 🟥 DEQUEUE OPERATION (Remove Element)
# ---------------------------------------------------------------
"""
Purpose:
   Remove (dequeue) the element from the **front** of the queue.

Steps:
1️⃣ Check if queue is empty.
     - If head is None → return "Queue is Empty"
2️⃣ Store head node temporarily (firstNode)
3️⃣ Move head to head.next
4️⃣ If head becomes None → set tail = None
5️⃣ Return value of firstNode (dequeued element)

-------------------------------------------------------------
🧩 VISUALIZATION EXAMPLE
-------------------------------------------------------------

Before Dequeue:
   +-------+      +----------+      +----------+      +----------+
   | head  | ---> | value=1  | ---> | value=2  | ---> | value=3  | ---> None
   +-------+      +----------+      +----------+      +----------+
   | tail  | --------------------------------------->^

Step 1: Dequeue()
   - Remove node 1
   - Move head → 222 (Node2)
   - Return node 1

After Dequeue:
   +-------+      +----------+      +----------+
   | head  | ---> | value=2  | ---> | value=3  | ---> None
   +-------+      +----------+      +----------+
   | tail  | --------------------->^

Garbage Collector removes the first node (1).
"""

# ---------------------------------------------------------------
# 🟨 PEEK OPERATION (View Front Element)
# ---------------------------------------------------------------
"""
Purpose:
   Return the first element in the queue without removing it.

Logic:
   - Return value of head node.
   - Do NOT modify head or tail pointers.

Example:
   Queue:  [1] -> [2] -> [3]
   head points to [1]

   peek() → returns 1
   (queue remains unchanged)

-------------------------------------------------------------
🧩 VISUALIZATION
-------------------------------------------------------------
   +-------+      +----------+      +----------+      +----------+
   | head  | ---> | value=1  | ---> | value=2  | ---> | value=3  |
   +-------+      +----------+      +----------+      +----------+
   | tail  | --------------------------------------->^

   peek() → returns 1
   (head and tail remain unchanged)
"""

# ---------------------------------------------------------------
# 🟦 ISEMPTY METHOD
# ---------------------------------------------------------------
"""
Purpose:
   Check if the queue has any elements.

Logic:
   - If head is None → queue is empty → return True
   - Else → return False

-------------------------------------------------------------
🧩 VISUALIZATION
-------------------------------------------------------------

Case 1: Empty queue
   head = None
   tail = None
   → isEmpty() = True

Case 2: Non-empty queue
   head → node(111)
   → isEmpty() = False
"""

# ---------------------------------------------------------------
# 🟧 NOTE — No isFull() Method in Linked List Queue
# ---------------------------------------------------------------
"""
⚠️ Important:
In linked list-based queues, we do NOT define a `maxSize`.
Hence, the queue **never becomes full** (until system memory runs out).

So, `isFull()` is not applicable here.
"""

# ---------------------------------------------------------------
# 🗑️ DELETE METHOD
# ---------------------------------------------------------------
"""
Purpose:
   Delete all elements in the queue.

Logic:
   - Set head = None
   - Set tail = None

Effect:
   - Breaks all node references.
   - Makes all nodes eligible for garbage collection.

-------------------------------------------------------------
🧩 VISUALIZATION
-------------------------------------------------------------

Before Delete:
   +-------+      +----------+      +----------+      +----------+
   | head  | ---> | value=1  | ---> | value=2  | ---> | value=3  | ---> None
   +-------+      +----------+      +----------+      +----------+
   | tail  | --------------------------------------->^

After Delete:
   head → None
   tail → None

   All nodes are garbage collected.
"""

# ---------------------------------------------------------------
# 📊 TIME & SPACE COMPLEXITY TABLE
# ---------------------------------------------------------------
"""
Operation        | Time Complexity | Space Complexity | Explanation
-------------------------------------------------------------------
Create Queue     | O(1)            | O(1)             | Initialize empty head/tail
Enqueue          | O(1)            | O(1)             | Insert at tail
Dequeue          | O(1)            | O(1)             | Remove from head
Peek             | O(1)            | O(1)             | Access head node
isEmpty          | O(1)            | O(1)             | Check if head == None
Delete           | O(1)            | O(1)             | Reset head and tail
isFull           | ❌ Not Applicable | -               | No capacity limit

✅ Key Insights:
- Linked List Queue avoids shifting or wrapping logic.
- Can grow dynamically (unlike fixed-size circular queue).
- Every operation takes constant time.
"""

# ---------------------------------------------------------------
# 🧾 SUMMARY
# ---------------------------------------------------------------
"""
🔹 Queue using Linked List works on FIFO principle.
🔹 `enqueue()` adds new nodes at the tail.
🔹 `dequeue()` removes nodes from the head.
🔹 No capacity → no isFull().
🔹 Uses dynamic memory allocation → flexible but more memory overhead.
🔹 All operations (enqueue, dequeue, peek, isEmpty, delete) = O(1).

🧩 Real-world Uses:
- Task Scheduling (Dynamic jobs)
- CPU Queue Management
- Print Queue systems
- Message Queues in Networking

In the next Note → we’ll write the **practical implementation**
of this logic in Python and test all queue operations using a Linked List.
"""
