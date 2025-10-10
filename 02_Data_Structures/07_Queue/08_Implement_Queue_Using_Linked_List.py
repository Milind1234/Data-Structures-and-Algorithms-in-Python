# note.py
# ------------------------------------------------------
# 📘 Queue (Linked List Implementation)
# ✅ Topic: Implementation, Working & Time/Space Complexity
# ------------------------------------------------------

"""
📌 INTRODUCTION

This file implements a **Queue** using a **Singly Linked List** in Python.

Unlike list-based queues or circular queues:
    ✅ There is no fixed capacity.
    ✅ The queue grows dynamically as nodes are added.
    ✅ Each enqueue and dequeue operation runs in constant time.
    ❌ Slightly higher memory overhead (due to Node objects and pointers).

Structure:
    - Each node stores `value` and a pointer `next`.
    - The Queue maintains:
        🔹 head → front of queue (for dequeue)
        🔹 tail → end of queue (for enqueue)
"""

# ---------------------------------------------------------------
# 🧱 STRUCTURE OVERVIEW
# ---------------------------------------------------------------
"""
Each Node:
    [value | next] → pointer to next node

The Queue maintains:
   head → first node (front of queue)
   tail → last node  (rear of queue)

Initially:
   head → None
   tail → None
   (Queue is empty)

Visual:
   +------+      +------+
   | Head | -->  | None |
   +------+      +------+
   | Tail | -->  | None |
   +------+      +------+
"""

# ---------------------------------------------------------------
# 🧩 CLASS DEFINITIONS
# ---------------------------------------------------------------
class Node:
    """
    Represents a single node in the linked list.
    Stores the data (value) and reference to the next node.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    """
    Singly Linked List used internally by the Queue.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        Generator to iterate through the list nodes.
        Enables easy printing of queue contents.
        """
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


# ---------------------------------------------------------------
# 🧱 QUEUE USING LINKED LIST
# ---------------------------------------------------------------
class Queue:
    def __init__(self):
        """
        Initialize an empty queue using a LinkedList.
        ⏱️ O(1) | 💾 O(1)
        """
        self.linkedlist = LinkedList()

    def __str__(self):
        """
        Return queue elements visually as '1 --> 2 --> 3'
        """
        values = [str(x) for x in self.linkedlist]
        return " --> ".join(values) if values else "Empty Queue"

    # -----------------------------------------------------------
    # 1️⃣ isEmpty()
    # -----------------------------------------------------------
    def isEmpty(self):
        """
        Check if queue has any elements.

        ⏱️ O(1) | 💾 O(1)
        """
        return self.linkedlist.head is None

    # -----------------------------------------------------------
    # 2️⃣ enqueue(value)
    # -----------------------------------------------------------
    def enqueue(self, value):
        """
        Insert element at the end (tail) of the queue.

        Steps:
          1. Create a new node with given value.
          2. If queue empty → set head and tail to new node.
          3. Else → attach new node to current tail and update tail pointer.

        VISUAL:
            Before enqueue(1):
                head → None, tail → None
            After enqueue(1):
                head → [1] (tail also points here)
            After enqueue(2):
                [1] --> [2]
            After enqueue(3):
                [1] --> [2] --> [3]
                
        VISUALIZATION:

        Step 1️⃣ — Enqueue(1)
        +------+     +----------+
        |Head  | --> |[1|•]     |
        +------+     +----------+
        |Tail  | ----^

        Step 2️⃣ — Enqueue(2)
        +------+     +----------+     +----------+
        |Head  | --> |[1|•]---->|[2|/]|
        +------+     +----------+     +----------+
        |Tail  | ----------------------^

        Step 3️⃣ — Enqueue(3)
        +------+     +----------+     +----------+     +----------+
        |Head  | --> |[1|•]---->|[2|•]---->|[3|/]|
        +------+     +----------+     +----------+     +----------+
        |Tail  | ----------------------------------------------^

        ⏱️ O(1) | 💾 O(1)
        """
        new_node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node
        return f"Enqueued {new_node}"

    # -----------------------------------------------------------
    # 3️⃣ dequeue()
    # -----------------------------------------------------------
    def dequeue(self):
        """
        Remove and return the element at the front of the queue.

        Steps:
          1. Check if queue is empty.
          2. Store the head node temporarily.
          3. Move head → head.next
          4. If head becomes None → reset tail to None (queue empty)
          5. Return dequeued node.

        VISUAL:
            Before dequeue():
                [1] --> [2] --> [3]
                head = [1]
            After dequeue():
                [2] --> [3]
                head = [2]
                
        VISUALIZATION:

        Before Dequeue:
        +------+     +----------+     +----------+     +----------+
        |Head  | --> |[1|•]---->|[2|•]---->|[3|/]|
        +------+     +----------+     +----------+     +----------+
        |Tail  | ----------------------------------------------^

        Step: Remove Head (1)
        +------+     +----------+     +----------+
        |Head  | --> |[2|•]---->|[3|/]|
        +------+     +----------+     +----------+
        |Tail  | ----------------------^

        (Node [1|•] is garbage collected)


        ⏱️ O(1) | 💾 O(1)
        """
        if self.isEmpty():
            return "Empty Queue"
        else:
            popped_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return f"Dequeued {popped_node}"

    # -----------------------------------------------------------
    # 4️⃣ peek()
    # -----------------------------------------------------------
    def peek(self):
        """
        Return the first element in the queue without removing it.

        VISUAL:
            Queue: [1] --> [2] --> [3]
            peek() → returns 1 (head node value)
        
        VISUALIZATION:
        +------+     +----------+     +----------+     +----------+
        |Head  | --> |[1|•]---->|[2|•]---->|[3|/]|
        +------+     +----------+     +----------+     +----------+
        |Tail  | ----------------------------------------------^

        peek() → returns '1' (value at head)
        
        ⏱️ O(1) | 💾 O(1)
        """
        if self.isEmpty():
            return "Empty Queue"
        else:
            return f"Element at start of Queue: {self.linkedlist.head.value}"

    # -----------------------------------------------------------
    # 5️⃣ delete()
    # -----------------------------------------------------------
    def delete(self):
        """
        Delete all elements from the queue.

        Steps:
          - Set head = None
          - Set tail = None
        Makes all nodes eligible for garbage collection.

        VISUAL:
            Before delete:
                [1] --> [2] --> [3]
            After delete:
                head = None
                tail = None
            
         VISUALIZATION:
        Before delete:
        +------+     +----------+     +----------+     +----------+
        |Head  | --> |[1|•]---->|[2|•]---->|[3|/]|
        +------+     +----------+     +----------+     +----------+
        |Tail  | ----------------------------------------------^

        After delete:
        +------+     +------+
        |Head  | --> | None |
        +------+     +------+
        |Tail  | --> | None |
        +------+     +------+

        ⏱️ O(1) | 💾 O(1)
        """
        if self.isEmpty():
            return "Empty Queue"
        else:
            self.linkedlist.head = None
            self.linkedlist.tail = None
        return "All Elements in Queue are deleted"


# ---------------------------------------------------------------
# ▶️ DEMONSTRATION (Dry Run Example)
# ---------------------------------------------------------------
if __name__ == "__main__":
    new_Queue = Queue()

    print(new_Queue.enqueue(1))
    print(new_Queue.enqueue(2))
    print(new_Queue.enqueue(3))
    print(new_Queue.enqueue(4))
    print(new_Queue.enqueue(5))

    print("\nCurrent Queue:")
    print(new_Queue)

    print("\nDequeuing first element:")
    print(new_Queue.dequeue())
    print("Queue after dequeue:", new_Queue)

    print("\nPeeking front element:")
    print(new_Queue.peek())

    print("\nDeleting all elements:")
    print(new_Queue.delete())
    print("Queue after delete:", new_Queue)


# ---------------------------------------------------------------
# 📊 SUMMARY OF TIME & SPACE COMPLEXITY
# ---------------------------------------------------------------
"""
Operation        | Time Complexity | Space Complexity | Description
-------------------------------------------------------------------
Create Queue     | O(1)            | O(1)             | Initialize empty linked list
Enqueue          | O(1)            | O(1)             | Add node at tail
Dequeue          | O(1)            | O(1)             | Remove node at head
Peek             | O(1)            | O(1)             | Access head node
isEmpty          | O(1)            | O(1)             | Check head == None
Delete Queue     | O(1)            | O(1)             | Reset head and tail
isFull           | ❌ N/A           | -                | Linked list has no fixed capacity

✅ Key Benefits:
- No shifting or resizing needed (unlike list-based queues).
- Dynamically grows in memory.
- Best choice when queue size is unpredictable.

🧩 Visual Recap:
Initial:   Empty
enqueue(1): [1]
enqueue(2): [1] --> [2]
enqueue(3): [1] --> [2] --> [3]
dequeue():  [2] --> [3]
peek():     returns 2
delete():   Queue cleared (head, tail = None)
"""
