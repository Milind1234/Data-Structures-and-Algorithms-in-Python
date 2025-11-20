"""
===============================================================================
📘 01_Hashing_Introduction_Notes.py — Introduction to Hashing (Full Explanation)
===============================================================================

Purpose
-------
This notes file explains the *core fundamentals of Hashing*:

  ✔ What is Hashing?  
  ✔ Why hashing is fast for search  
  ✔ How keys are converted to numbers  
  ✔ Hash Function  
  ✔ Key  
  ✔ Hash Value  
  ✔ Hash Table  
  ✔ Collision (with diagrams)  
  ✔ Real-world examples  
  ✔ Comparison with other data structures  
  ✔ Python-style diagrams (ASCII)

This file is purely educational — NO code execution required.
===============================================================================
"""


# =============================================================================
#                            WHAT IS HASHING?
# =============================================================================
"""
Hashing is a technique used to **store and retrieve data extremely fast**, usually in O(1) time.

Definition:
-----------
Hashing is a method of mapping data of arbitrary size (strings, numbers, objects)
to data of fixed size (usually an integer index).

The mapping is performed by a **Hash Function**.

Real-world meaning:
-------------------
You provide a value → hash function converts it → gives back a number →  
that number becomes an **index in an array**.

Example:
--------
Let’s say we have three strings:

    "Apple"
    "Application"
    "AppStore"

We pass them into a hash function (think of it as a “magic function” for now):

        "Apple"        --> 18
        "Application"  --> 20
        "AppStore"     --> 22

These returned numbers are called **hash values**.

Now we store the strings in an array (hash table):

Index:   0 ... 18 19 20 21 22 23 ...
Value:            Apple  Application  AppStore

Searching:
----------
To search for “Apple”:
    → Compute hash("Apple") → 18  
    → Directly jump to index 18 (O(1) time)
"""


# =============================================================================
#                        WHY HASHING IS SUPER FAST?
# =============================================================================
"""
Searching with other data structures:
--------------------------------------
Array (unsorted)       → O(n)
Array (sorted)         → O(log n)
Linked List            → O(n)
Binary Search Tree     → O(log n)
AVL Tree / Red-Black   → O(log n)

Hash Table             → O(1) average case !!!

How?
----
Because instead of scanning, we JUMP DIRECTLY to the index using hash function.
"""


# =============================================================================
#                           HASHING TERMINOLOGY
# =============================================================================
"""
1️⃣ Hash Function
-----------------
A function that converts input data (string, number, etc.) into a fixed-size integer.

Example:
    h("Apple") → 18

Required properties:
    - Same input MUST always produce same output.
    - Should distribute values uniformly.
    - Should minimize collisions.

ASCII Visualization:

    ┌──────────────┐
    │  "Apple"     │  Key
    └──────┬───────┘
           │
           ▼
      ┌──────────┐
      │ Hash     │
      │ Function │
      └────┬─────┘
           ▼
         (18)   <--- Hash Value


2️⃣ Key
-------
The original value provided by user.

Examples:
    "Apple"
    "Application"
    "AppStore"

Keys are what we INSERT and SEARCH.


3️⃣ Hash Value
---------------
Output of the hash function — ALWAYS an integer.

Example:
    h("AppStore") = 22


4️⃣ Hash Table
---------------
A data structure (usually an array) that stores values using **hash values as indexes**.

ASCII:

Index:   0 1 ... 18 19 20 21 22 23
Value:           Apple   Application   AppStore


5️⃣ Collision
--------------
A collision occurs when **two different keys** produce the **same hash value**.

Example:

    h("ABCD")   = 20
    h("ABCDEF") = 20   ← COLLISION

ASCII Diagram:

    "ABCD" ------\
                   >--- Hash Function --> 20
    "ABCDEF" ----/

    Hash Table:
    Index 20 already has "ABCD". Inserting "ABCDEF" causes collision.

We will learn collision resolution methods (chaining, linear probing,
quadratic probing, double hashing) in next lectures.
"""


# =============================================================================
#                 SIMPLE ASCII DIAGRAM OF COMPLETE HASHING FLOW
# =============================================================================
"""
Example Keys:
    Apple
    Application
    AppStore

Step 1 — Apply Hash Function
----------------------------

  Apple       →   18
  Application →   20
  AppStore    →   22

Step 2 — Insert into Hash Table
-------------------------------

 Index : 0 ... 18  19  20       21  22         23 ...
 Value :       Apple   Application   (empty)   AppStore


Step 3 — Search (Example: "Apple")
-----------------------------------

   hash("Apple") → 18
   Access table[18] → "Apple"   ---> O(1)

"""


# =============================================================================
#                    WHY HASHING IS IMPORTANT (REAL USE CASES)
# =============================================================================
"""
✔ Dictionary / HashMap Implementation (Python dict uses hashing)  
✔ Database indexing  
✔ Caching (fast lookup)  
✔ Password hashing  
✔ File integrity (hash signatures)  
✔ Compilers (symbol tables)  
✔ Network routing tables  
"""


# =============================================================================
#                  TIME & SPACE COMPLEXITY (OVERVIEW)
# =============================================================================
"""
Operation     Average Case     Worst Case (many collisions)
------------------------------------------------------------
Search         O(1)             O(n)
Insert         O(1)             O(n)
Delete         O(1)             O(n)

Space:         O(n)  (size of hash table)

Goal of a GOOD hash function:
    → keep collisions low → keep operations close to O(1)
"""


# =============================================================================
#                                SUMMARY
# =============================================================================
"""
✔ Hashing converts keys to numbers using a hash function  
✔ Hash values index into a hash table  
✔ Searching becomes O(1)  
✔ Collisions happen when two keys map to same index  
✔ Hash tables are extremely powerful for fast lookup  
✔ Dictionaries in Python internally use hashing  
"""


# End of Notes
