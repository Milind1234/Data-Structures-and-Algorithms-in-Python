"""
📘 STACK OPERATIONS (Notes File)

In this lecture, we study the **common operations of Stack**.

A stack works in **LIFO (Last In, First Out)** order.  
That means → The element inserted **last** will be the element removed **first**.

We can implement these operations:
    1. Push
    2. Pop
    3. Peek (Top)
    4. isEmpty
    5. Size
    6. Clear/Delete All
    (Optionally: isFull → for fixed-size stacks)

---------------------------------------------------------
🔹 1. PUSH Operation (Insert element at top)
---------------------------------------------------------
📖 Definition:
Push = Insert a new element onto the top of the stack.

Visualization (Empty → Push sequence):

Initially (empty stack):
    [   ]

push(10):
    [ 10 ]  ← top

push(20):
    [ 20 ]  ← top
    [ 10 ]

push(30):
    [ 30 ]  ← top
    [ 20 ]
    [ 10 ]

💡 Note:
Every new element always goes **on top of the previous one**.

Example (Python list simulation):
    stack = []
    stack.append(10)  # push 10
    stack.append(20)  # push 20
    stack.append(30)  # push 30

---------------------------------------------------------
🔹 2. POP Operation (Remove top element)
---------------------------------------------------------
📖 Definition:
Pop = Remove and return the top element of the stack.

Visualization (Pop sequence from [30,20,10]):

Current stack:
    [ 30 ]  ← top
    [ 20 ]
    [ 10 ]

pop() → removes 30:
    [ 20 ]  ← top
    [ 10 ]

pop() → removes 20:
    [ 10 ]  ← top

pop() → removes 10:
    [   ]   ← empty stack

💡 Note:
We can only remove the **top element**, never from the middle.

Example (Python list simulation):
    top = stack.pop()  # removes last element

---------------------------------------------------------
🔹 3. PEEK Operation (View top element without removing)
---------------------------------------------------------
📖 Definition:
Peek = Look at the top element but don’t remove it.

Visualization:

Stack:
    [ 40 ]  ← top
    [ 30 ]
    [ 20 ]
    [ 10 ]

peek() → returns 40  
Stack remains unchanged:
    [ 40 ]  ← top
    [ 30 ]
    [ 20 ]
    [ 10 ]

💡 Why needed?
Sometimes, we just need to check the top element (like “what page am I on?” in a browser) without removing it.

Example:
    top = stack[-1]   # peek in Python list

---------------------------------------------------------
🔹 4. isEmpty Operation (Check if stack is empty)
---------------------------------------------------------
📖 Definition:
Returns True if stack has no elements, else False.

Visualization:

Case 1 (Empty):
    [   ]
    isEmpty() → True

Case 2 (Non-empty):
    [ 25 ]
    [ 10 ]
    isEmpty() → False

Example:
    len(stack) == 0  # True if empty

---------------------------------------------------------
🔹 5. SIZE Operation (Count elements in stack)
---------------------------------------------------------
📖 Definition:
Returns the number of elements currently in the stack.

Visualization:

Stack:
    [ 70 ]  ← top
    [ 50 ]
    [ 30 ]
    [ 10 ]

size() → 4

Example:
    size = len(stack)

---------------------------------------------------------
🔹 6. CLEAR / DELETE ALL Operation
---------------------------------------------------------
📖 Definition:
Removes all elements, making the stack empty.

Visualization:

Before clear():
    [ 90 ]  ← top
    [ 60 ]
    [ 30 ]

After clear():
    [   ]

Example:
    stack.clear()

---------------------------------------------------------
💡 Optional Operation: isFull()
---------------------------------------------------------
📖 Only applies to fixed-size stacks (e.g., array-based implementation with max capacity).

Example:
    capacity = 5
    if len(stack) == capacity:
        return True

---------------------------------------------------------
✅ SUMMARY
---------------------------------------------------------
- **Push** → Add element at top.  
- **Pop** → Remove & return top element.  
- **Peek** → Return top element without removing.  
- **isEmpty** → Check if stack has no elements.  
- **Size** → Number of elements in stack.  
- **Clear/Delete All** → Remove all elements.  
- **isFull** (only for fixed-size) → Check if stack is at capacity.  

All main operations run in **O(1)** time.
"""
