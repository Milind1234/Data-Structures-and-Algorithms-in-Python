# =============================================================================
#                  PROS & CONS OF COLLISION RESOLUTION TECHNIQUES
# =============================================================================

"""
We compare:
    - Direct Chaining
    - Open Addressing
And we determine WHICH TECHNIQUE is better in which scenario.
"""

# =============================================================================
#                             1. DIRECT CHAINING
# =============================================================================
"""
✔ Advantages:
    - Hash table never gets full
    - Deletion is easy (just remove from linked list)
    - Good when frequent deletion is required

✘ Disadvantages:
    - Linked list becomes long if too many collisions
    - Worst-case search time becomes O(n)
    - Uses extra memory (nodes + pointers)
"""

# When to use Direct Chaining?
"""
👉 Use when:
    - Frequent DELETE operations
    - Unpredictable number of items
"""

# =============================================================================
#                           2. OPEN ADDRESSING
# =============================================================================
"""
✔ Advantages:
    - Uses only array → memory efficient
    - Fast cache performance
    - Implementation is simple (no linked list)

✘ Disadvantages:
    - Table becomes FULL
    - Need resizing → O(N) rehashing
    - Deletion creates empty holes → PROBE FAILURES

Deletion Example Problem:
-------------------------
Index: 1  2  3  4
       K  L  _  M

Searching M:
    - Hash(M) = 2
    - Check index 2 → L
    - Check index 3 → EMPTY → stops → returns NOT FOUND ❌
    But M actually exists at index 4.
"""

# When to use Open Addressing?
"""
👉 Use when:
    - Input size is known beforehand
    - Few deletions
    - Memory efficiency is important
"""


# =============================================================================
#                            PROS & CONS OF HASHING
# =============================================================================

"""
Goal of hashing:
    Perform SEARCH, INSERT, DELETE in O(1) time.
"""

# =============================================================================
#                                 ADVANTAGES
# =============================================================================
"""
✔ Extremely fast operations (O(1)) IF collisions are low
✔ Ideal for search-heavy systems (databases, compilers, caching)
✔ Hash table provides direct indexing using hash function
"""

# =============================================================================
#                                 DISADVANTAGES
# =============================================================================
"""
✘ Depends heavily on hash function
✘ Collisions degrade performance → worst case O(n)
✘ Needs resizing (in open addressing)
✘ Potential memory overhead (in chaining)
"""

# =============================================================================
#                     HASHING vs OTHER DATA STRUCTURES
# =============================================================================

comparison = {
    "Array": {
        "Search": "O(n)",
        "Insert": "O(n)",
        "Delete": "O(n)"
    },
    "Linked List": {
        "Search": "O(n)",
        "Insert": "O(1)",
        "Delete": "O(1)"
    },
    "Tree (Balanced BST)": {
        "Search": "O(log n)",
        "Insert": "O(log n)",
        "Delete": "O(log n)"
    },
    "Hash Table": {
        "Search": "O(1) average",
        "Insert": "O(1) average",
        "Delete": "O(1) average",
        "Worst Case": "O(n)"
    }
}

"""
Conclusion:
    Hashing wins in average cases.
    But requires a GOOD hash function to avoid collisions.
"""


