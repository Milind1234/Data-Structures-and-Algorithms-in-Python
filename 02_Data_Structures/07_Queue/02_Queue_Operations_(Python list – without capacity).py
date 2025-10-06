# =====================================================
# 📘 INFORMATION ABOUT QUEUE OPERATIONS (Notes File)
# =====================================================
"""
In the previous notes, we learned what a **Queue** is and why it is used.  
Now, in this, we’ll discuss the **standard operations** that can be performed on a queue data structure.

---------------------------------------------------------
🔹 STANDARD OPERATIONS IN QUEUE
---------------------------------------------------------
A total of **7 operations** can be performed on a queue:

1️⃣ createQueue() — Create a new queue  
2️⃣ enqueue() — Insert an element (at the rear)  
3️⃣ dequeue() — Remove element (from the front)  
4️⃣ peek() — View the first element (without removing)  
5️⃣ isEmpty() — Check if the queue is empty  
6️⃣ isFull() — Check if the queue is full (for fixed capacity)  
7️⃣ deleteQueue() — Delete the entire queue

Each operation plays a key role in how queue behaves and performs in applications.
Let’s explore them one by one.

---------------------------------------------------------
🔹 IMPLEMENTATION OPTIONS
---------------------------------------------------------
A Queue in Python can be implemented in two major ways:
1. Using **Python List**
2. Using **Linked List**

Depending on the implementation type:
- The **method definitions** and **time complexities** can differ.
- Example: In **linked list queues**, `isFull()` is not needed (dynamic size).
- In **list-based queues**, inserting/removing from the beginning takes **O(n)** time (because of shifting).

✅ So, in Python list-based implementation:
- Enqueue = append() at the end.
- Dequeue = pop(0) from the front.
- If we set a **max capacity**, the queue behaves as a **circular queue**.

---------------------------------------------------------
🔹 1️⃣ CREATE QUEUE
---------------------------------------------------------
In Python list (without capacity):
    queue = []

This creates an empty queue in memory.

🧠 Note:
- We can insert unlimited elements (limited only by memory).
- But large queues can become **slow** due to internal resizing (relocation) operations.

---------------------------------------------------------
🔹 2️⃣ ENQUEUE (INSERT ELEMENT)
---------------------------------------------------------
Enqueue means inserting a new element at the **end (rear)** of the queue.

Example:
    queue = []
    enqueue(1)
    enqueue(2)
    enqueue(3)

Now the queue looks like:
    FRONT → [1, 2, 3] ← REAR

Visual representation:
    enqueue(1) → [1]
    enqueue(2) → [1, 2]
    enqueue(3) → [1, 2, 3]

🧠 Note:
- Insertion always happens **at the rear**.
- You **cannot insert** in the middle or front.
- In Python lists, `append()` provides this enqueue behavior.
- However, resizing (when list grows) may take **O(n)** occasionally.

---------------------------------------------------------
🔹 3️⃣ DEQUEUE (REMOVE ELEMENT)
---------------------------------------------------------
Dequeue means removing the **front element** of the queue.

Example:
    queue = [1, 2, 3, 4]
    dequeue() → returns 1  (and removes it)
    queue = [2, 3, 4]

Next dequeue:
    dequeue() → returns 2
    queue = [3, 4]

And so on...

⚠️ If we try to dequeue from an empty queue:
    → Error: "Queue Underflow" or "Queue is empty"

🧠 Note:
- This demonstrates **FIFO (First In, First Out)** behavior.
- Dequeue always removes the element that came earliest.
- In Python lists, this is done using `pop(0)` (which is O(n)).

---------------------------------------------------------
🔹 4️⃣ PEEK (VIEW FRONT ELEMENT)
---------------------------------------------------------
Peek allows checking the **front element** without removing it.

Example:
    queue = [1, 2, 3]
    peek() → returns 1  (but queue remains [1, 2, 3])

Even after multiple peeks:
    peek() → always returns 1
until we perform a dequeue:
    dequeue() → removes 1
    peek() → now returns 2

🧠 Use Case:
- Peek is useful when we just want to **check the next element** to be processed,
  without modifying the queue.

---------------------------------------------------------
🔹 5️⃣ ISEMPTY
---------------------------------------------------------
This method checks whether the queue has any elements.

Example:
    queue = [1, 2, 3]
    isEmpty() → False

    queue = []
    isEmpty() → True

🧠 Importance:
- Used inside `dequeue()` or `peek()` to prevent errors.
- If queue is empty, these operations should not execute.

---------------------------------------------------------
🔹 6️⃣ ISFULL
---------------------------------------------------------
Used only when queue has a **fixed capacity** (like circular queues).

Example:
    max_size = 5
    queue = [1, 2, 3, 4, 5]
    isFull() → True

    enqueue(6) → Error: "Queue is Full"

🧠 Note:
- Not required for dynamic queues (list/linked list without capacity).
- Commonly used in array-based or circular queue implementations.

---------------------------------------------------------
🔹 7️⃣ DELETE QUEUE
---------------------------------------------------------
Used to remove **all elements** from the queue.

Example:
    queue = [1, 2, 3, 4]
    deleteQueue() → queue = []

🧠 Implementation:
- In Python, simply reassign the list:
      queue = []

---------------------------------------------------------
✅ SUMMARY
---------------------------------------------------------
- Queue follows FIFO (First In, First Out) rule.
- Basic operations: enqueue, dequeue, peek, isEmpty, size.
- Optional operations: isFull, deleteQueue.
- Implemented using:
    - Python list (simple but slower for front removals)
    - Linked list (faster O(1) enqueue/dequeue)
- Used in systems that process data **in order of arrival**.
"""

# =====================================================
# 🔹 CLASS-BASED QUEUE IMPLEMENTATION (USING LIST)
# =====================================================

class Queue:
    def __init__(self):
        """Create an empty queue (Python list)"""
        self.items = []

    def enqueue(self, element):
        """Insert an element at the rear of the queue"""
        self.items.append(element)

    def dequeue(self):
        """Remove and return the element from the front of the queue"""
        if self.is_empty():
            raise IndexError("Queue Underflow! Cannot dequeue from empty queue.")
        return self.items.pop(0)  # O(n) due to shifting

    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot peek.")
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the queue"""
        return len(self.items)

    def delete_queue(self):
        """Delete all elements from the queue"""
        self.items = []


# =====================================================
# 🔹 DEMONSTRATION
# =====================================================
if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("Queue after enqueues:", queue.items)  # [1, 2, 3, 4]

    # Peek
    print("Front element (peek):", queue.peek())  # 1

    # Dequeue operations
    print("Dequeued:", queue.dequeue())  # 1
    print("Dequeued:", queue.dequeue())  # 2
    print("Queue after dequeues:", queue.items)  # [3, 4]

    # Is empty?
    print("Is queue empty?", queue.is_empty())  # False

    # Delete the entire queue
    queue.delete_queue()
    print("Queue deleted, now empty?", queue.is_empty())  # True
