# =====================================================
# 📘 INFORMATION ABOUT QUEUE (Notes File)
# =====================================================
"""
A **Queue** is a **linear abstract data structure (ADT)** that follows the **FIFO (First In, First Out)** principle.  
This means the **first element inserted** into the queue will be the **first one removed**.

Think of a queue like a real-life waiting line:
- You can only add (enqueue) elements **at the end (rear)**.
- You can only remove (dequeue) elements **from the front**.
- You cannot directly access elements in the middle.

---------------------------------------------------------
🔹 REAL-LIFE EXAMPLES OF QUEUE
---------------------------------------------------------
1. 🏪 Line of people at a store  
   - First person in line is served first.

2. 🖨️ Printer queue  
   - First document sent to printer is printed first.

3. ☎️ Call center waiting queue  
   - First caller is connected to the next available agent.

4. 🍔 Restaurant order system  
   - Orders are cooked in the order they are received.

---------------------------------------------------------
🔹 KEY CHARACTERISTICS & PROPERTIES
---------------------------------------------------------
- Queue is an **Abstract Data Type (ADT)** → defines operations, not implementation details.
- It strictly follows **FIFO (First In, First Out)** principle.
- New elements are **added at the REAR**.
- Elements are **removed from the FRONT**.
  
✅ Implementation choices:
- **Using Python list** (simple but inefficient for large data)
- **Using collections.deque** (double-ended queue; efficient O(1) ops)
- **Using Linked List** (dynamic queue with O(1) enqueue/dequeue)

---------------------------------------------------------
🔹 STANDARD OPERATIONS & TIME COMPLEXITY
---------------------------------------------------------
- `enqueue(item)` → Insert an element at the **rear**.         → O(1)
- `dequeue()`     → Remove and return element from **front**.  → O(1)
- `peek()` / `front()` → Return the element at the front.      → O(1)
- `is_empty()`    → Check if queue has no elements.            → O(1)
- `size()`        → Return total number of elements.           → O(1)
- `delete()` / `clear()` → Remove all elements.                → O(1)

---------------------------------------------------------
🔹 PSEUDOCODE FOR QUEUE OPERATIONS
---------------------------------------------------------

enqueue(element):
    if queue is full:
        error "Queue Overflow"
    else:
        rear = rear + 1
        queue[rear] = element

dequeue():
    if queue is empty:
        error "Queue Underflow"
    else:
        element = queue[front]
        front = front + 1
        return element

peek():
    if queue is empty:
        return None
    else:
        return queue[front]

is_empty():
    return (front > rear)

size():
    return (rear - front + 1)

clear():
    front = 0
    rear = -1

---------------------------------------------------------
🔹 VISUALIZATION OF QUEUE OPERATIONS
---------------------------------------------------------

Initial empty queue:
    FRONT → [    ] ← REAR

enqueue(10):
    FRONT → [10] ← REAR

enqueue(20):
    FRONT → [10, 20] ← REAR

enqueue(30):
    FRONT → [10, 20, 30] ← REAR

dequeue():
    Removes 10 → FRONT moves ahead
    FRONT → [20, 30] ← REAR

peek():
    FRONT element = 20

---------------------------------------------------------
🔹 WHY DO WE NEED QUEUE?
---------------------------------------------------------
We use queues when we must process data **in the order it arrives**.

Examples:
- Task scheduling in operating systems.
- Managing print jobs.
- Buffering in IO systems (network packets, streaming).
- Breadth-First Search (BFS) traversal in graphs.

---------------------------------------------------------
✅ SUMMARY
---------------------------------------------------------
- Queue = FIFO data structure.
- Core operations = enqueue, dequeue, peek, is_empty, size.
- All major operations take O(1) time (if implemented properly).
- Can be implemented using list, deque, or linked list.
- Used wherever data is processed **in order of arrival**.
"""


# =====================================================
# 🔹 Minimal CLASS-Based QUEUE Implementation
# =====================================================

class Queue:
    def __init__(self):
        """Initialize an empty queue using Python list"""
        self._data = []

    def enqueue(self, element):
        """Add an element to the rear of the queue"""
        self._data.append(element)

    def dequeue(self):
        """Remove and return the front element (FIFO)"""
        if not self._data:
            raise IndexError("Queue Underflow! (dequeue from empty queue)")
        return self._data.pop(0)   # O(n) → front removal shifts elements

    def peek(self):
        """Return the front element without removing"""
        if not self._data:
            raise IndexError("Peek on empty queue")
        return self._data[0]

    def is_empty(self):
        """Check if the queue has no elements"""
        return len(self._data) == 0

    def size(self):
        """Return number of elements in the queue"""
        return len(self._data)

    def clear(self):
        """Remove all elements from the queue"""
        self._data.clear()


# =====================================================
# 🔹 DEMONSTRATION
# =====================================================
if __name__ == "__main__":
    queue = Queue()

    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("After enqueues:", queue._data)    # [10, 20, 30]

    # Peek at front
    print("Front element is:", queue.peek())  # 10

    # Dequeue one element
    print("Dequeued:", queue.dequeue())       # 10

    # Current front after dequeue
    print("Front element now:", queue.peek()) # 20

    # Is queue empty?
    print("Is empty?", queue.is_empty())      # False

    # Clear the queue
    queue.clear()
    print("Queue cleared, is empty?", queue.is_empty())  # True
