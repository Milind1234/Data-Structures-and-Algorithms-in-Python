"""
===============================
     PYTHON LIST vs LINKED LIST
===============================

Q1) How are Python Lists stored in memory?
------------------------------------------
Answer:
- Python list elements are stored **contiguously** in memory.
- Each element is placed next to the previous one.
- Allows **random access**:
    - Access any element by index: O(1) time complexity
    - Example:
        my_list = [10, 20, 30, 40]
        Access element at index 2 → my_list[2] = 30

ASCII Representation (Python List):
------------------------------------
Memory Layout (contiguous):
 [10] [20] [30] [40]
 Index: 0    1    2    3

Access Example:
 my_list[0] → 10
 my_list[3] → 40

---------------------------
Q2) How are Linked Lists stored in memory?
------------------------------------------
Answer:
- Linked list nodes are **NOT stored contiguously** in memory.
- Each node contains:
    1) Data (value)
    2) Reference (address) of the next node.
- Nodes can be anywhere in memory, but are connected via links.

ASCII Representation (Linked List):
------------------------------------
Memory Layout (non-contiguous):
 Node1: [10|Ref(Addr2)]
 Node2: [20|Ref(Addr3)]
 Node3: [30|Ref(Addr4)]
 Node4: [40|NULL]

 Links:
  10 → 20 → 30 → 40 → NULL

---------------------------
Q3) Complexity Difference:
---------------------------
- Python List:
    - Direct index access → O(1)
    - Insertion at the end (usually amortized O(1))
    - Insertion in middle → O(n) (shifting elements)

- Linked List:
    - No index-based random access.
    - Must traverse from Head node sequentially → O(n)
    - Easy insertion/deletion if node reference is known → O(1)

---------------------------
Q4) Summary (Python List vs Linked List)
----------------------------------------
1) Memory:
   - List → contiguous memory
   - Linked List → scattered memory (non-contiguous)
   
2) Access:
   - List → O(1) random access via index
   - Linked List → sequential access only (O(n))

3) Data Connection:
   - List → no explicit links
   - Linked List → each node has link (pointer) to next node

4) Use Cases:
   - List → best for index-based access, static size
   - Linked List → best for dynamic size, frequent insert/delete
"""
