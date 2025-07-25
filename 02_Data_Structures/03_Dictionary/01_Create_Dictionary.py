"""
==========================================================
Dictionary Creation in Python
==========================================================

What is a Dictionary?
- Dictionary in Python is a collection of key-value pairs.
- Keys are unique and immutable (strings, numbers, tuples).
- Values can be of any data type and can be duplicated.

Characteristics:
- From Python 3.7+, insertion order is preserved.
- Mutable (can add, update, remove).
- Keys must be unique.

General Time Complexity:
- Lookup (fetch value): O(1)
- Insertion: O(1)
- Deletion: O(1)
- Iteration: O(n)
Space Complexity: O(n)
==========================================================
"""

# 1) Empty Dictionary
my_dict1 = {}
print("Empty Dictionary:", my_dict1)
# Time Complexity: O(1), Space Complexity: O(1)

# 2) Using dict() Constructor with Keyword Arguments
my_dict2 = dict(one='one', two='two', three='three')
print("dict() Constructor:", my_dict2)
# Time Complexity: O(n), Space Complexity: O(n)

# 3) Using Curly Braces with Key-Value Pairs
my_dict3 = {'1': 'one', '2': 'two', '3': 'three'}
print("Curly Braces:", my_dict3)
# Time Complexity: O(n), Space Complexity: O(n)

# 4) Using List of Tuples (Convert to Dictionary)
my_dict4 = dict([('01', 'one'), ('02', 'two'), ('03', 'three')])
print("List of Tuples:", my_dict4)
# Time Complexity: O(n), Space Complexity: O(n)

# 5) Using Dictionary Comprehension
my_dict5 = {x: x**2 for x in range(1, 4)}
print("Dictionary Comprehension:", my_dict5)
# Time Complexity: O(n), Space Complexity: O(n)

# 6) Using fromkeys() Method
keys = ['a', 'b', 'c']
my_dict6 = dict.fromkeys(keys, 0)
print("fromkeys() Method:", my_dict6)
# Time Complexity: O(n), Space Complexity: O(n)

"""
Dictionary Operations (No Code – Just a List)
--------------------------------------------
1) Add a new key-value pair
2) Update an existing value
3) Remove a key-value pair (pop, del, popitem)
4) Clear dictionary
5) Get value using key (get, direct access)
6) Check if key exists (in keyword)
7) Iterate over keys, values, key-value pairs (keys(), values(), items())
8) Copy dictionary (copy())
9) Merge dictionaries (update() or | operator)
10) Dictionary length (len())
11) Set default values (setdefault())
"""

# ================= Summary Table =================
print("""
----------------------------------------------------------
Summary Table of Dictionary Creation Complexities
----------------------------------------------------------
| Method                  | Time Complexity | Space Complexity |
|-------------------------|-----------------|------------------|
| {} (empty dict)         | O(1)            | O(1)             |
| dict()                  | O(n)            | O(n)             |
| Curly braces { }        | O(n)            | O(n)             |
| List of tuples -> dict  | O(n)            | O(n)             |
| Comprehension           | O(n)            | O(n)             |
| fromkeys()              | O(n)            | O(n)             |
----------------------------------------------------------
""")
