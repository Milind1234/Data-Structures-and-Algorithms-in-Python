"""
Collision Resolution Techniques - Notes
--------------------------------------
This Python file contains detailed notes explaining collision resolution
techniques in hashing. All explanations are written inside multiline strings.
"""

# ===============================
#   1. What is Collision?
# ===============================
"""
A collision happens when two different keys are hashed to the same index.
Example:
    ABCD  ---> 2
    EFGH  ---> 2
Both want to go to index 2 → collision.
"""

# ===============================
#   2. Collision Resolution Methods
# ===============================
"""
Two broad categories:
1. Direct Chaining
2. Open Addressing
   - Linear Probing
   - Quadratic Probing
   - Double Hashing
"""

# =====================================================
#   3. Direct Chaining (Linked List in each bucket)
# =====================================================
"""
In Direct Chaining, every index stores a linked list.
All colliding elements go into the same list.

Example:
    Hash values for ABCD, EFGH, IJKLM → all = 2

Insert operations:
    ABCD  inserted → at index 2 (node location 111)
    EFGH  collides → appended to linked list (location 222)
    IJKLM collides → appended to linked list (location 333)
    Miller → hash = 7 → placed at index 7 (location 444)

So the table stores only physical references:
    index 2 → 111 → 222 → 333
    index 7 → 444
"""

# =====================================================
#   4. Open Addressing
# =====================================================
"""
In Open Addressing, colliding elements are stored in other *empty* buckets.
No linked lists are used.
To find a new position, we probe (search) for the next free index.

Three probing techniques:
1. Linear Probing
2. Quadratic Probing
3. Double Hashing
"""

# =====================================================
#   4.1 Linear Probing
# =====================================================
"""
If a cell is occupied, move to the next cell (index + 1).

Example:
    Hash values for ABCD, EFGH, IJKLM → all = 2

Insert ABCD:
    index 2 empty → store at 2

Insert EFGH:
    index 2 full → go to 3 → store at 3

Insert IJKLM:
    index 2 full → 3 full → go to 4 → store at 4

Pattern: (index + i) % table_size
"""

# =====================================================
#   4.2 Quadratic Probing
# =====================================================
"""
Instead of checking next cell, we jump using squares:
    1^2, 2^2, 3^2 ...

Formula:
    new_index = (hash_value + i^2) % table_size

Example:
    For IJKLM:
        i=1: 2 + 1^2 = 3 (occupied)
        i=2: 2 + 2^2 = 6 (empty → insert)
"""

# =====================================================
#   4.3 Double Hashing
# =====================================================
"""
A second hash function determines jump size.

Formula:
    new_index = (hash1(key) + i * hash2(key)) % table_size

Example:
    First string ABCD:
        hash1 = 2 → insert at index 2

    Second string EFGH:
        hash1 = 2 full → hash2 = 4
        index = 2 + 1*4 = 6 → insert at 6

    Third string IJKLM:
        hash1 = 2 full → hash2 = 4
        i=1: 2 + 1*4 = 6 full
        i=2: 2 + 2*4 = 10 → insert
"""

# End of Notes

# Visualizations — Collision Resolution (ASCII + runnable Python)

# Below are compact visual aids and a tiny Python simulator you can run to observe how each collision resolution technique stores three colliding keys whose base hash index is `2` inside a table of size `16`.

""""

# 1) Direct chaining (bucket→linked-list)

ASCII view (each bucket stores a linked list head):

```
Index: 0 1 2  3 4 5 ... 7
Table: - - [A]->[B]->[C] - - ... -
         (111) (222) (333)
```

Explanation: when A, B, C all hash to index `2` we attach them in sequence to the bucket at 2. No other table cells are used.

---

## 2) Open addressing — Linear probing

ASCII view (probe forward to next empty):

```
Index: 0 1 2   3   4 5 ...
Table: - - A   B   C - ...
       (A) (B) (C)
```

Detailed step:
- A → index 2 (empty) → put A at 2
- B → index 2 (occupied) → try 3 → put B at 3
- C → 2 (occ), 3 (occ) → try 4 → put C at 4

---

## 3) Open addressing — Quadratic probing

ASCII view (probe using i^2 offsets):

```
Index: 0 1 2  3 4 5 6 7 ...
Table: - - A  B - - C - ...
```

Detailed step (table size = 16):
- A → 2
- B → try 2, then 2 + 1^2 = 3 → put B at 3
- C → try 2, 3 (both occ), then 2 + 2^2 = 6 → put C at 6

---

## 4) Open addressing — Double hashing

ASCII view (second hash provides step size):

```
Index: 0 1 2  3 4 5 6 7 8 9 10 ...
Table: - - A  - - - B - - -  C ...
```

Example (using h1(key)=2 and h2(key)=4):
- A → index 2 (place A)
- B → index 2 (occ) → 2 + 1*h2 = 6 → put B at 6
- C → 2 (occ) → 6 (occ) → 2 + 2*h2 = 10 → put C at 10

---

## Mini Python simulator (run locally)

This small script demonstrates all four techniques on three synthetic keys that collide to base index `2`.
"""
# ```python
# Mini simulator for collision techniques
from typing import List, Optional

TABLE_SIZE = 16
BASE_INDEX = 2            # base hash for our example keys
SECOND_HASH = 4           # used for double hashing

keys = ['A', 'B', 'C']    # pretend these all hash to BASE_INDEX

# 1) Direct chaining implementation
def direct_chaining_sim(keys):
    table = [[] for _ in range(TABLE_SIZE)]
    for k in keys:
        table[BASE_INDEX].append(k)
    return table

# 2) Linear probing
def linear_probing_sim(keys):
    table: List[Optional[str]] = [None]*TABLE_SIZE
    for k in keys:
        idx = BASE_INDEX
        while table[idx] is not None:
            idx = (idx + 1) % TABLE_SIZE
        table[idx] = k
    return table

# 3) Quadratic probing
def quadratic_probing_sim(keys):
    table: List[Optional[str]] = [None]*TABLE_SIZE
    for k in keys:
        i = 0
        while True:
            idx = (BASE_INDEX + i*i) % TABLE_SIZE
            if table[idx] is None:
                table[idx] = k
                break
            i += 1
    return table

# 4) Double hashing
def double_hashing_sim(keys):
    table: List[Optional[str]] = [None]*TABLE_SIZE
    for k in keys:
        i = 0
        while True:
            idx = (BASE_INDEX + i * SECOND_HASH) % TABLE_SIZE
            if table[idx] is None:
                table[idx] = k
                break
            i += 1
    return table

# Pretty print helper
def show_table(t):
    for i, v in enumerate(t):
        print(f"{i:2}: {v}")
    print('\n')

if __name__ == '__main__':
    print('--- Direct chaining ---')
    dc = direct_chaining_sim(keys)
    for i, bucket in enumerate(dc):
        if bucket:
            print(f"{i:2}: {bucket}")
    print('\n--- Linear probing ---')
    show_table(linear_probing_sim(keys))
    print('--- Quadratic probing ---')
    show_table(quadratic_probing_sim(keys))
    print('--- Double hashing ---')
    show_table(double_hashing_sim(keys))
"""```

Run this script in your local Python environment to see the exact positions for each technique.

---

If you'd prefer visualizations as small ASCII animations, PNG diagrams, or embedded SVG blocks, say which format you want and I will add them next. (I can also tweak the simulator to use different base hashes or table sizes.)

"""


# -------------------------------------------------------------------------
#                                OR 
# -------------------------------------------------------------------------

"""
===============================================================================
                COLLISION RESOLUTION TECHNIQUES — NOTES
===============================================================================

When multiple keys produce the same hash value → a COLLISION occurs.
To handle this, we use Collision Resolution Techniques:

    1. Direct Chaining
    2. Open Addressing
          • Linear Probing
          • Quadratic Probing
          • Double Hashing
===============================================================================
"""


# =============================================================================
# 1️⃣ DIRECT CHAINING (Using Linked List / Python List)
# =============================================================================
"""
Concept:
--------
• Every bucket in the hash table stores a LIST (chain).
• All elements that hash to the same bucket are appended to this list.

Advantages:
-----------
• Very simple
• Hash table never ‘gets full’
• Works well even with many collisions

Disadvantages:
--------------
• Requires extra memory for chains
• Lookup becomes slow if the chain becomes long (worst O(n))

Example Structure:
------------------
Index 2 → ["ABCD", "EFGH", "IJKL"]
Index 5 → ["MILLER"]
"""


class DirectChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key):
        index = self.hash(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash(key)
        return key in self.table[index]

    def __str__(self):
        return str(self.table)


# =============================================================================
# 2️⃣ OPEN ADDRESSING
# =============================================================================
"""
In Open Addressing:
-------------------
• No linked lists are used.
• If a collision occurs, we SEARCH for another empty cell.
• All keys are stored INSIDE the table.

Types:
------
1. Linear Probing → (index + i)
2. Quadratic Probing → (index + i²)
3. Double Hashing → (index + i * hash2(key))
"""


# =============================================================================
# 2.1️⃣ LINEAR PROBING
# =============================================================================

class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key):
        index = self.hash(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
        print("Hash Table Full!")

    def search(self, key):
        index = self.hash(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] == key:
                return True
        return False


# =============================================================================
# 2.2️⃣ QUADRATIC PROBING
# =============================================================================

class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key):
        index = self.hash(key)
        for i in range(self.size):
            new_index = (index + i*i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
        print("Hash Table Full!")

    def search(self, key):
        index = self.hash(key)
        for i in range(self.size):
            new_index = (index + i*i) % self.size
            if self.table[new_index] == key:
                return True
        return False


# =============================================================================
# 2.3️⃣ DOUBLE HASHING
# =============================================================================

class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):    # Main hash
        return sum(ord(ch) for ch in key) % self.size

    def hash2(self, key):    # Must NEVER return 0
        return 1 + (sum(ord(ch) for ch in key) % (self.size - 1))

    def insert(self, key):
        index1 = self.hash1(key)
        index2 = self.hash2(key)

        for i in range(self.size):
            new_index = (index1 + i * index2) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
        print("Hash Table Full!")

    def search(self, key):
        index1 = self.hash1(key)
        index2 = self.hash2(key)

        for i in range(self.size):
            new_index = (index1 + i * index2) % self.size
            if self.table[new_index] == key:
                return True
        return False


# =============================================================================
#                             SAMPLE EXECUTION
# =============================================================================
if __name__ == "__main__":

    print("\n===== Direct Chaining =====")
    dc = DirectChainingHashTable(10)
    dc.insert("ABCD")
    dc.insert("EFGH")
    dc.insert("IJKL")
    print(dc)

    print("\n===== Linear Probing =====")
    lp = LinearProbingHashTable(10)
    lp.insert("ABCD")
    lp.insert("EFGH")
    lp.insert("IJKL")
    print(lp.table)

    print("\n===== Quadratic Probing =====")
    qp = QuadraticProbingHashTable(10)
    qp.insert("ABCD")
    qp.insert("EFGH")
    qp.insert("IJKL")
    print(qp.table)

    print("\n===== Double Hashing =====")
    dh = DoubleHashingHashTable(10)
    dh.insert("ABCD")
    dh.insert("EFGH")
    dh.insert("IJKL")
    print(dh.table)

