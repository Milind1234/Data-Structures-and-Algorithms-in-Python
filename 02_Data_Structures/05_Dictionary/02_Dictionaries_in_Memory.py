"""
==========================================================
Topic: Dictionaries in Memory (Python)
==========================================================

🔹 What is a Dictionary?
- A Python dictionary is a key-value data structure.
- Implemented internally using **Hash Tables**.
- Provides fast lookup, insertion, and deletion (Average O(1)).

----------------------------------------------------------
How Does Python Store Dictionary in Memory?
----------------------------------------------------------
1) **Keys & Hash Function**
   - Each dictionary key is passed to Python’s built-in hash() function.
   - hash(key) → produces an integer hash value.

2) **Index Calculation**
   - index = hash(key) % size_of_internal_array
   - Determines where the key-value pair will be stored.

3) **Internal Array**
   - Python maintains an internal array (buckets) to store key-value pairs.

4) **Collisions**
   - Collision occurs when two different keys map to the same index.
   - Python handles this using:
        a) **Chaining** (like Linked List)
        b) **Open Addressing** (for optimization)

----------------------------------------------------------
Example Dictionary:
----------------------------------------------------------
engToSp = {"one": "uno", "two": "dos", "three": "tres"}

Step 1: Key = "one"
        hash("one") → index = 3
        stored → index[3] = ("one", "uno")

Step 2: Key = "two"
        hash("two") → index = 1
        stored → index[1] = ("two", "dos")

Step 3: Key = "three"
        hash("three") → index = 4
        stored → index[4] = ("three", "tres")

----------------------------------------------------------
ASCII Diagram (Hash Table Representation)
----------------------------------------------------------
Index | Key      | Value
--------------------------
0     |          | 
1     | two      | dos
2     |          | 
3     | one      | uno
4     | three    | tres
--------------------------

----------------------------------------------------------
Collision Example:
----------------------------------------------------------
Suppose we add a new key "neo" → hash("neo") = index 1 (same as "two")
- Collision detected at index 1.

Solution:
- Python stores ("neo", "xxx") in the same index using a **linked list**.

ASCII Representation After Collision:
----------------------------------------------------------
Index | Keys-Values
--------------------------
0     | 
1     | two → dos → neo → xxx
2     | 
3     | one → uno
4     | three → tres
--------------------------

----------------------------------------------------------
Python Code Demonstrating Collision (Educational Purpose)
----------------------------------------------------------
# Note: Python hash values change on every run for security (hash randomization)
# This code is only for demonstrating how two keys can hash to the same index
# in a controlled way (forcing hash collision with custom keys).

class AlwaysHashOne:
    def __init__(self, name):
        self.name = name
    def __hash__(self):
        return 1
    def __eq__(self, other):
        return isinstance(other, AlwaysHashOne) and self.name == other.name
    def __repr__(self):
        return self.name

# Creating keys that always hash to 1 → collision guaranteed
key1 = AlwaysHashOne("KeyA")
key2 = AlwaysHashOne("KeyB")

collision_dict = {key1: "Value1", key2: "Value2"}
print("Collision Dictionary:", collision_dict)

# Output: Both keys stored even though they have the same hash value
# Python internally resolves this by checking equality and handling collisions.

----------------------------------------------------------
Performance:
----------------------------------------------------------
- Lookup → O(1) average, O(n) worst (all keys in one index)
- Insertion → O(1) average
- Deletion → O(1) average
- Space Complexity → O(n) (depends on number of keys)

----------------------------------------------------------
Summary Table
----------------------------------------------------------
Operation       Average Time   Worst Time
------------------------------------------
Insertion       O(1)           O(n)
Lookup          O(1)           O(n)
Deletion        O(1)           O(n)
Space           O(n)           O(n)
------------------------------------------

Key Takeaways:
- Python dictionary is highly optimized due to hash tables.
- Collisions are inevitable but handled efficiently.
- Provides constant-time complexity in average cases.
==========================================================
"""
