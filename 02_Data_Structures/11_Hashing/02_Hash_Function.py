"""
===============================================================================
📘 Hash Functions — Mod Function + ASCII Function (with Clean Examples)
===============================================================================

Purpose
-------
This notes file explains:
  ✔ What a Hash Function is
  ✔ How integer-based hashing works (Mod Function)
  ✔ How string hashing works (ASCII-based Hashing)
  ✔ Why hashing helps achieve O(1) average search time
  ✔ Characteristics of a GOOD hash function
  ✔ Step-by-step examples (No AppMillers used)

===============================================================================
🔹 What is a Hash Function?
===============================================================================
A **hash function** maps input data (key) of any size → to a fixed range of numbers.

    Key (string/number) ──► Hash Function ──► Hash Value (index)

Hash value is used to place the data inside a **Hash Table (array/list)**.

Good hashing = FAST search → typically **O(1)**.

===============================================================================
🔹 Hash Function #1 — Mod Function (For Integer Keys)
===============================================================================
The simplest hash function for integers:

        index = number % cellSize

Where:
    number    → input integer
    cellSize  → size of hash table

This ensures the index always stays within `[0, cellSize - 1]`.

Example:
--------
cellSize = 24

    400 % 24 = 16   → store 400 at index 16
    700 % 24 = 4    → store 700 at index 4

This function reduces large values into a small usable index.

-------------------------------------------------------------------------------
# Mod Function Example
-------------------------------------------------------------------------------
def mod(number, cellNumber):
    return number % cellNumber


print(mod(400, 24))   # → 16
print(mod(700, 24))   # → 4
# Meaning: 400 goes to slot 16, 700 goes to slot 4

===============================================================================
🔹 Hash Function #2 — ASCII Function (For String Keys)
===============================================================================
For strings, we cannot use modulo directly.
So we convert each character into ASCII value using ord().

ASCII Example:
    'A' → 65
    'B' → 66
    'C' → 67

Hashing logic:
    1) Convert each character to ASCII
    2) Sum the values
    3) Apply modulo to fit into table

-------------------------------------------------------------------------------
# ASCII-based Hash Function Example
-------------------------------------------------------------------------------
def modASCII(string, cellNumber):
    total = 0
    for ch in string:
        total += ord(ch)
    return total % cellNumber


print(modASCII("ABC", 24))  # → 6

Explanation:
    A = 65
    B = 66
    C = 67
    Sum = 198
    198 % 24 = 6
→ Store "ABC" at index 6.

===============================================================================
🔹 Why These Hash Functions Work?
===============================================================================
Hashing makes SEARCH operation extremely fast:

    Convert Key → Index → Access in O(1)

Example:
    If "ABC" hashed to index 6, then:
        table[6] is directly accessed.

No loops.
No traversal.
Instant access.

===============================================================================
🔹 Characteristics of a GOOD Hash Function
===============================================================================

1) **Uniform Distribution**
---------------------------
A good hash function spreads keys across the table evenly.

BAD:
    Many keys map to same index → high collisions → slow.

GOOD:
    Keys spread out → fewer collisions → fast operations.

Example of BAD:
    "Hello" → 20
    "World" → 20
    "Laptop" → 20
All land in same slot → BAD hash function.

2) **Uses ALL Input Data**
---------------------------
Function should consider ALL characters.

BAD:
    Hash function based only on first 3 characters:
        "COMPUTER"
        "COMPOSE"
    Both → "COM" → same hash → collision

GOOD:
    Include all characters → more variety → fewer collisions.

3) **Fast to Compute**
-----------------------
Since hashing is used often (in search, insert, delete),
hashing must be O(m), where m = length of key.

4) **Deterministic**
---------------------
Same input must ALWAYS produce same output.

===============================================================================
🔹 Summary Table — Hash Functions
===============================================================================
Hash Function                 Input Type       Pros                     Cons
-------------------------     -------------    -----------------------    -------------------------
Mod (%)                       Integer          Simple, fast              Not usable for strings
ASCII Sum + Mod               String           Easy to implement         Causes collisions often
Advanced Hash (real apps)     String/Number    Very low collisions       More complex

===============================================================================
End of Notes
===============================================================================
"""
