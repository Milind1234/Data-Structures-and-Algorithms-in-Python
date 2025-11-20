# =============================================================================
#                         WHAT IF THE HASH TABLE IS FULL?
# =============================================================================
"""
This note explains what happens when the hash table becomes full and how
different collision resolution strategies behave.

We consider two scenarios:
    1. Direct Chaining
    2. Open Addressing (Linear/Quadratic/Double Hashing)
"""

# =============================================================================
#                                DIRECT CHAINING
# =============================================================================
"""
⚡ Key Point:
    Hash table NEVER becomes full.

Why?
    - Each index stores a LINKED LIST of elements.
    - If multiple elements map to same index, they are simply chained.
    - Therefore, unlimited inserts are possible.

Visualization:
    Table index → head of linked list

    Index 1:  A → B → C → D → None
    Index 3:  X → Y → None
    Index 5:  M → None

If new key hashes to an index already used:
    - Create new node
    - Append to linked list

Hence, "hash table full" situation NEVER occurs.
"""

# =============================================================================
#                            OPEN ADDRESSING — FULL TABLE
# =============================================================================
"""
⚡ Key Point:
    In Open Addressing, EVERY element must be stored inside the hash table.
    No linked list is used.

Therefore:
    When the table is full → NO EMPTY SLOT EXISTS → insertion fails.

So what do we do?
    🔥 Solution:
        CREATE A NEW HASH TABLE WITH DOUBLE SIZE
        and
        REHASH (reinsert) ALL ELEMENTS.
"""

# Example:
"""
Old Table (size = 4):
Index: 0  1  2  3
       A  B  C  D     <-- Table is full

Insert new key → No space → Resize

New Table (size = 8)
Recompute hash for A,B,C,D and insert again.
Then insert new key.
"""

# Complexity:
"""
Rehashing N items → O(N)
Thus resizing is expensive.
"""

