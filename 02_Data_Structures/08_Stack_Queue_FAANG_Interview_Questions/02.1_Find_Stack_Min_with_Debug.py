# min_stack_note.py
# ------------------------------------------------------
# 📘 Min Stack — Stack with O(1) min() (Note-style, Debug Version)
# ✅ Shows both main stack and minNode stack after each push/pop
# ------------------------------------------------------

"""
OVERVIEW

This version of the Min Stack note adds **debug visuals** for learning:
After every push() and pop(), the program prints both:
  - The main stack (top)
  - The min-tracking stack (minNode)

This helps you see how the minNode mirrors the state of the stack.
"""

# ---------------------------------------------------------------
# Node class — basic linked node
# ---------------------------------------------------------------
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        s = str(self.value)
        if self.next:
            s += "," + str(self.next)
        return s


# ---------------------------------------------------------------
# Stack class — with min tracking & debug printing
# ---------------------------------------------------------------
class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    # -----------------------------------------------------------
    # Helper: Convert linked list to string (for printing)
    # -----------------------------------------------------------
    def _stringify(self, node):
        if not node:
            return "[Empty]"
        current = node
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)

    def __str__(self):
        return (
            f"Stack:   {self._stringify(self.top)}\n"
            f"MinList: {self._stringify(self.minNode)}"
        )

    # -----------------------------------------------------------
    # 1️⃣ min() — Get current minimum value
    # -----------------------------------------------------------
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value

    # -----------------------------------------------------------
    # 2️⃣ push() — Push item and update minNode
    # -----------------------------------------------------------
    def push(self, item):
        if self.minNode is not None and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)

        self.top = Node(value=item, next=self.top)

        # Debug print
        print(f"Pushed: {item}")
        print(self)
        print("-" * 40)

    # -----------------------------------------------------------
    # 3️⃣ pop() — Pop item and update minNode
    # -----------------------------------------------------------
    def pop(self):
        if not self.top:
            print("Stack is empty! Nothing to pop.")
            return None

        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next

        # Debug print
        print(f"Popped: {item}")
        print(self)
        print("-" * 40)
        return item

# ---------------------------------------------------------------
# ▶️ DEMONSTRATION
# ---------------------------------------------------------------
if __name__ == '__main__':
    s = Stack()

    s.push(5)
    s.push(3)
    s.push(1)
    s.push(4)

    s.pop()
    s.pop()

# ---------------------------------------------------------------
# 📊 TIME & SPACE COMPLEXITY
# ---------------------------------------------------------------
"""
Operation | Time | Space | Description
---------------------------------------
push      | O(1) | O(1) | Insert element & update minNode
pop       | O(1) | O(1) | Remove element & sync minNode
min       | O(1) | O(1) | Get current minimum instantly

All operations are constant time — and now you can visually trace how
minNode mirrors the stack after every operation.
"""