# note.py
# ------------------------------------------------------
# 📘 QUEUE (Python list implementation — without capacity)
# ✅ All Core Methods: enqueue(), dequeue(), peek(), is_empty(), delete(), __str__()
# ------------------------------------------------------

"""
📌 INTRODUCTION

In this lecture, we’ll implement a **Queue** using Python’s built-in **list**,
without setting a maximum capacity.

This queue will follow the **FIFO (First In, First Out)** principle:
➡️ The first element added will be the first one removed.

We will:
- Create a Queue class.
- Implement all basic methods:
  createQueue, isEmpty, enqueue, dequeue, peek, and delete.
- Analyze **time and space complexity** for each.

---------------------------------------------------------
🧩 INTERNAL REPRESENTATION
---------------------------------------------------------
In this implementation:
- The **front** of the queue is at index 0.
- The **rear** of the queue is at the end of the list.

Hence:
    enqueue()  → list.append(x)  → adds to end (rear)
    dequeue()  → list.pop(0)     → removes from start (front)

Visual Example:
    Initially: []
    enqueue(1) → [1]
    enqueue(2) → [1, 2]
    enqueue(3) → [1, 2, 3]
    dequeue()  → removes 1 → [2, 3]

---------------------------------------------------------
🧠 WHY THIS IMPLEMENTATION?
---------------------------------------------------------
- Simple to understand.
- Demonstrates FIFO behavior clearly.
- Great for learning queue concepts.

⚠️ However, pop(0) operation in Python lists is **O(n)**,
since all remaining elements shift left.

For high-performance queues → use `collections.deque` (O(1) operations on both ends).
"""

# ---------------------------------------------------------------
# 🟩 QUEUE CLASS (List-Based Implementation)
# ---------------------------------------------------------------
class Queue:
    """
    A simple Queue implemented using Python list.
    Front = index 0, Rear = last index.
    """

    # -----------------------------------------------------------
    # 1️⃣ CREATE QUEUE
    # -----------------------------------------------------------
    def __init__(self):
        """
        PURPOSE:
        Initialize an empty queue.

        IMPLEMENTATION IDEA:
        Create an empty Python list and assign it to self.items.

        COMPLEXITY:
            Time: O(1)
            Space: O(1)
        """
        self.items = []

    # -----------------------------------------------------------
    # 2️⃣ __STR__ METHOD (visualization)
    # -----------------------------------------------------------
    def __str__(self):
        """
        PURPOSE:
        Return queue elements as a space-separated string for easy visualization.

        VISUAL OUTPUT:
            FRONT → 1 2 3 ← REAR

        COMPLEXITY:
            Time: O(n)
            Space: O(n)
        """
        if self.items is None or len(self.items) == 0:
            return "Queue is Empty"
        values = [str(x) for x in self.items]
        return "FRONT → " + " ".join(values) + " ← REAR"

    # -----------------------------------------------------------
    # 3️⃣ ISEMPTY
    # -----------------------------------------------------------
    def isEmpty(self):
        """
        PURPOSE:
        Check whether the queue is empty or not.

        IMPLEMENTATION IDEA:
        Return True if the list is empty, else False.

        VISUAL:
            [] → True
            [10,20] → False

        COMPLEXITY:
            Time: O(1)
            Space: O(1)
        """
        if self.items == []:
            return True
        else:
            return False

    # -----------------------------------------------------------
    # 4️⃣ ENQUEUE (add to rear)
    # -----------------------------------------------------------
    def enqueue(self, value):
        """
        PURPOSE:
        Insert an element at the rear of the queue.

        IMPLEMENTATION IDEA:
        Use Python list's append() to add element at the end.

        VISUAL:
            [] → enqueue(1) → [1]
            [1] → enqueue(2) → [1, 2]

        COMPLEXITY:
            Time: Amortized O(1), but may take O(n) or O(n²) during reallocation
            Space: O(1)
        """
        self.items.append(value)
        return f"✅ Element '{value}' inserted at end of Queue"

    # -----------------------------------------------------------
    # 5️⃣ DEQUEUE (remove from front)
    # -----------------------------------------------------------
    def dequeue(self):
        """
        PURPOSE:
        Remove and return the front element from the queue.

        IMPLEMENTATION IDEA:
        Use list.pop(0) to remove element from index 0.

        VISUAL:
            [1, 2, 3] → dequeue() → returns 1 → [2, 3]

        NOTE:
        Removing from front is O(n) because elements shift left.

        COMPLEXITY:
            Time: O(n)
            Space: O(1)
        """
        if self.isEmpty():
            return "⚠️ Queue is Empty — cannot dequeue."
        return self.items.pop(0)

    # -----------------------------------------------------------
    # 6️⃣ PEEK (view front element)
    # -----------------------------------------------------------
    def peek(self):
        """
        PURPOSE:
        Return the front element without removing it.

        IMPLEMENTATION IDEA:
        Access element at index 0.

        VISUAL:
            [10, 20, 30] → peek() => 10 (queue unchanged)

        COMPLEXITY:
            Time: O(1)
            Space: O(1)
        """
        if self.isEmpty():
            return "⚠️ Queue is Empty — nothing to peek."
        return self.items[0]

    # -----------------------------------------------------------
    # 7️⃣ DELETE (clear entire queue)
    # -----------------------------------------------------------
    def delete(self):
        """
        PURPOSE:
        Delete all elements from the queue (free memory).

        IMPLEMENTATION IDEA:
        Set the list reference to None → allows garbage collection.

        VISUAL:
            [10,20,30] → delete() → None

        COMPLEXITY:
            Time: O(1)
            Space: O(1)
        """
        self.items = None
        return "🗑️ All items deleted from Queue."


# ---------------------------------------------------------------
# ✅ DEMONSTRATION & DRY RUN
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("✅ QUEUE (Python list, no capacity) — DEMO\n")

    new_Queue = Queue()

    # Test isEmpty()
    print("Is Empty?", new_Queue.isEmpty())  # True

    # Enqueue elements
    print(new_Queue.enqueue(0))
    print(new_Queue.enqueue(1))
    print(new_Queue.enqueue(2))
    print(new_Queue.enqueue(3))
    print(new_Queue.enqueue(4))

    # Display queue
    print("\nCurrent Queue:")
    print(new_Queue)  # FRONT → 0 1 2 3 4 ← REAR

    # Dequeue
    print("\nDequeued Element:", new_Queue.dequeue())  # 0
    print("Queue after dequeue:")
    print(new_Queue)  # FRONT → 1 2 3 4 ← REAR

    # Peek
    print("\nFront Element (peek):", new_Queue.peek())  # 1

    # Delete all items
    print("\nDeleting Queue:")
    print(new_Queue.delete())  # All items deleted

    # Try printing after delete
    print(new_Queue)  # Queue is Empty


# ---------------------------------------------------------------
# 📊 SUMMARY OF TIME & SPACE COMPLEXITIES
# ---------------------------------------------------------------
"""
Operation        | Time Complexity        | Space Complexity | Explanation
---------------------------------------------------------------------------
createQueue      | O(1)                  | O(1)             | Empty list initialization
enqueue()        | Amortized O(1)        | O(1)             | Append at end; may reallocate
dequeue()        | O(n)                  | O(1)             | pop(0) shifts all elements left
peek()           | O(1)                  | O(1)             | Access first element
isEmpty()        | O(1)                  | O(1)             | Simple check
delete()         | O(1)                  | O(1)             | Reset reference to None
__str__()        | O(n)                  | O(n)             | Joins all elements into string

⚙️ NOTES:
- Queue follows FIFO → first element inserted is the first removed.
- Removing from front in Python list is slow (O(n)).
- For better performance, use `collections.deque` for O(1) enqueue/dequeue.
- This implementation is best for learning queue logic and behavior.
"""
