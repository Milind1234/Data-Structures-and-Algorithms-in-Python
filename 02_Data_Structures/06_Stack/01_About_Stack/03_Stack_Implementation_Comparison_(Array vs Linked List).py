"""
📘 STACK IMPLEMENTATION COMPARISON (Array vs Linked List)

Stack can be implemented in **two common ways**:
1. Using Arrays (or Python list)
2. Using Linked List

---------------------------------------------------------
🔹 PUSH Operation (Insert element at top)
---------------------------------------------------------

Using Array:
-------------
stack = []
stack.append(10)   # push 10
stack.append(20)   # push 20

Visualization:
    [ 20 ]  ← top
    [ 10 ]

Using Linked List:
-------------------
Each element is a Node(value, next)

push(10):
    Head -> [10] -> None

push(20):
    Head -> [20] -> [10] -> None

Visualization:
    Top -> [20] -> [10]

---------------------------------------------------------
🔹 POP Operation (Remove top element)
---------------------------------------------------------

Using Array:
-------------
stack = [10, 20, 30]
stack.pop() → removes 30

Visualization:
    Before: [30] [20] [10]
    After : [20] [10]

Using Linked List:
-------------------
Head -> [30] -> [20] -> [10]
Pop removes head node (30)

New Head:
    Head -> [20] -> [10]

Visualization:
    Top -> [20] -> [10]

---------------------------------------------------------
🔹 PEEK Operation (View top element)
---------------------------------------------------------

Using Array:
-------------
stack = [10, 20, 30]
peek → stack[-1] = 30

Using Linked List:
-------------------
Head -> [30] -> [20] -> [10]
peek → return Head.value = 30

---------------------------------------------------------
🔹 ISEMPTY Operation
---------------------------------------------------------

Using Array:
-------------
len(stack) == 0 → True if empty

Using Linked List:
-------------------
Head == None → True if empty

---------------------------------------------------------
🔹 SIZE Operation
---------------------------------------------------------

Using Array:
-------------
size = len(stack)

Using Linked List:
-------------------
Traverse from head, count nodes
size = number of nodes

---------------------------------------------------------
🔹 CLEAR Operation
---------------------------------------------------------

Using Array:
-------------
stack.clear()  # resets to empty

Using Linked List:
-------------------
Head = None    # dereference all nodes

---------------------------------------------------------
⚖️ COMPARISON SUMMARY
---------------------------------------------------------
Array Implementation:
- ✅ Direct indexing possible
- ✅ Simple (append/pop)
- ❌ May need resizing if fixed capacity
- ❌ Memory reallocation cost

Linked List Implementation:
- ✅ Dynamic size (no overflow unless memory full)
- ✅ Efficient memory usage (no resizing)
- ❌ Extra memory per node (next pointer)
- ❌ Slower random access (must traverse)

---------------------------------------------------------
✅ CONCLUSION
---------------------------------------------------------
- Use Array-based Stack → when size is predictable and operations are simple.
- Use Linked List-based Stack → when size is unknown or frequent resizing may occur.
"""
