"""
📘 INFORMATION ABOUT STACK (Notes File)

A **stack** is a **linear abstract data structure (ADT)** that follows the **LIFO (Last In, First Out)** principle.  
This means the **last element pushed (inserted)** into the stack will be the **first one popped (removed)**.

Think of a stack like a vertical pile of objects:
- You can only add (push) to the **top**.
- You can only remove (pop) from the **top**.
- You cannot directly access elements in the middle or bottom.

---------------------------------------------------------
🔹 REAL-LIFE EXAMPLES OF STACK
---------------------------------------------------------
1. 🍽️ Pile of plates  
   - You put a plate on top, you remove the top plate first.

2. 📚 Stack of books  
   - Last book placed is the first one you pick up.

3. 🎾 Can of tennis balls  
   Example visualization:
       [ Ball 3 ]  ← Top (last in, first out)
       [ Ball 2 ]
       [ Ball 1 ]  ← Bottom

   Removing balls → Ball 3 → Ball 2 → Ball 1

4. 🌐 Browser Back Button  
   Suppose visit order: Udemy → LinkedIn → Gmail → AppMiller  
   Stack holds pages in this order:
   
       [ Gmail     ]  ← top
       [ LinkedIn  ]
       [ Google     ]

   Clicking back pops → Gmail → LinkedIn → Google .

---------------------------------------------------------
🔹 KEY CHARACTERISTICS & PROPERTIES
---------------------------------------------------------
- Stack is an **Abstract Data Type (ADT)** → defines operations, not internal representation.
- Implementation choices:
  - **Array / fixed-size** stack (capacity needed).
  - **Linked-list** stack (dynamic growth).
  
- Time complexity (typical):
  - `push`, `pop`, `peek` → O(1)
  - `isEmpty`, `size` → O(1)
  
- Additional operations:
  - `isFull()` (for array-based).
  - `clear()` (reset stack).
  - Advanced variations: min-stack (O(1) min), two stacks in one array, stack using queues, etc.
  
- Uses in computing:
  - Function call stack & recursion.
  - Undo/redo in editors.
  - Expression evaluation (postfix/prefix).
  - Matching parentheses/brackets.
  - DFS & backtracking algorithms.
  - Browser navigation history.

---------------------------------------------------------
🔹 CORE OPERATIONS (with PSEUDOCODE)
---------------------------------------------------------

push(element):
    if isFull():
        error "Stack Overflow"
    else:
        increment top
        stack[top] = element

pop():
    if isEmpty():
        error "Stack Underflow"
    else:
        element = stack[top]
        decrement top
        return element

peek():
    if isEmpty():
        return None or error
    else:
        return stack[top]

isEmpty():
    return (top == -1)

isFull():   # only for fixed size
    return (top == capacity-1)

size():
    return (top + 1)

clear():
    top = -1

---------------------------------------------------------
🔹 VISUALIZATION OF PUSH & POP
---------------------------------------------------------
Empty stack:
    [   ]

push(5):
    [ 5 ]

push(10):
    [ 10 ]  ← top
    [  5 ]

push(15):
    [ 15 ]  ← top
    [ 10 ]
    [  5 ]

pop():
    → removes 15
    [ 10 ]  ← top
    [  5 ]

---------------------------------------------------------
✅ SUMMARY
---------------------------------------------------------
- Stack = LIFO structure.
- Core ops = push, pop, peek, isEmpty, size (+ isFull for arrays).
- All operations are O(1).
- Can be implemented via arrays, linked lists, or even queues.
- Widely used in compilers, OS, algorithms, and real-life systems.
"""

# =====================================================
# 🔹 Minimal CLASS-Based STACK Implementation
# =====================================================

class Stack:
    def __init__(self):
        """Initialize an empty stack using Python list"""
        self._data = []

    def push(self, x):
        """Push element x onto the stack (top)"""
        self._data.append(x)

    def pop(self):
        """Remove and return the top element (LIFO)"""
        if not self._data:
            raise IndexError("Stack Underflow! (pop from empty stack)")
        return self._data.pop()

    def peek(self):
        """Return the top element without removing"""
        if not self._data:
            raise IndexError("Peek on empty stack")
        return self._data[-1]

    def is_empty(self):
        """Check if the stack has no elements"""
        return len(self._data) == 0

    def size(self):
        """Return the number of elements"""
        return len(self._data)

    def clear(self):
        """Remove everything from the stack"""
        self._data.clear()


# =====================================================
# 🔹 DEMONSTRATION
# =====================================================
if __name__ == "__main__":
    stack = Stack()

    # Push elements
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print("After pushes: size =", stack.size())   # 3

    # Peek at top
    print("Top element is:", stack.peek())        # 15

    # Pop element
    print("Popped:", stack.pop())                 # 15

    # Current top after pop
    print("Top element now:", stack.peek())       # 10

    # Is stack empty?
    print("Is empty?", stack.is_empty())          # False

    # Clear the stack
    stack.clear()
    print("Stack cleared, is empty?", stack.is_empty())  # True