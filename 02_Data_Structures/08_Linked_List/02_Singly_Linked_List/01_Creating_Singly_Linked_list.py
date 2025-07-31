"""
======================================================
🚀 LINKED LIST CLASS CREATION (using Node class)
======================================================

----------------------------------------------
1️⃣ NODE CLASS (RECAP)
----------------------------------------------
"""
class Node:
    def __init__(self, value):
        self.value = value   # 🟢 data part
        self.next = None     # 🔗 pointer to next node
"""
📌 Each Node consists of:
- value → stores actual data
- next  → reference (address) of the next node

----------------------------------------------
2️⃣ LINKED LIST CLASS (Single Initial Node)
----------------------------------------------
"""
class LinkedList:
    def __init__(self, value):
        # 1) Create a new node
        new_node = Node(value)

        # 2) Head → points to the first node
        self.head = new_node

        # 3) Tail → also points to same node (only one node initially)
        self.tail = new_node

        # 4) Length of Linked List
        self.length = 1
"""
----------------------------------------------
3️⃣ VISUALIZATION (Linked List with one node)
----------------------------------------------
head → [ value=10 | next=None ] ← tail
Length = 1

----------------------------------------------
4️⃣ EMPTY LINKED LIST (Alternative)
----------------------------------------------
"""
class LinkedListEmpty:
    def __init__(self):
        self.head = None    # 🚫 no head initially
        self.tail = None    # 🚫 no tail initially
        self.length = 0     # 📏 length = 0
"""
----------------------------------------------
5️⃣ OBJECT CREATION & ATTRIBUTE ACCESS
----------------------------------------------
"""
# Linked list with one node
new_list = LinkedList(10)
print(new_list.head.value)  # → 10
print(new_list.tail.value)  # → 10
print(new_list.length)      # → 1

# Empty linked list
empty_list = LinkedListEmpty()
print(empty_list.length)    # → 0

"""
----------------------------------------------
6️⃣ DETAILED EXPLANATION OF CODE FLOW
----------------------------------------------
1) new_node = Node(value) 
   - Creates a node (value, next=None) → O(1)

2) self.head = new_node
   - Points head to new node → O(1)

3) self.tail = new_node
   - Points tail to new node → O(1)

4) self.length = 1
   - Initializes linked list length → O(1)
   
----------------------------------------------
7️⃣ COMPLEXITY ANALYSIS
----------------------------------------------
⏳ TIME COMPLEXITY:
- Node creation → O(1)
- Head, Tail, Length assignment → O(1)
- **Overall → O(1)**

💾 SPACE COMPLEXITY:
- Node object → 2 attributes (value, next) → O(1)
- LinkedList object → 3 attributes (head, tail, length) → O(1)
- **Overall → O(1)**

----------------------------------------------
8️⃣ ADVANTAGES OF THIS DESIGN
----------------------------------------------
1) 🟢 Head & Tail references allow O(1) insertion at both ends.
2) 🟢 Length attribute gives O(1) size retrieval.
3) 🟢 Flexible: supports empty or one-node initialization.

----------------------------------------------
9️⃣ DISADVANTAGES
----------------------------------------------
1) 🔴 Slight memory overhead (extra tail & length attributes).
2) 🔴 Requires careful handling when adding/removing nodes.

----------------------------------------------
🔟 INTERVIEW TAKEAWAYS
----------------------------------------------
- Head = start of linked list.
- Tail = last node in linked list.
- Length = maintained for O(1) size access.
- Constructor Complexity → **Time: O(1), Space: O(1)**.
- Supports both empty & one-node initialization easily.
"""
