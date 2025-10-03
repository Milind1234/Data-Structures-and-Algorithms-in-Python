# Tuple vs List vs Dictionary Comparisons with Code Examples

"""
1. Tuple vs List
-----------------
Similarities:
- Both are sequence data types.
- Both support indexing and slicing.
- Both support iteration and built-in functions like len(), max(), min(), sum().

Differences:
- Mutability:
    Tuple -> Immutable (cannot change after creation).
    List  -> Mutable (can add, remove, modify elements).
- Syntax:
    Tuple -> (1, 2, 3)
    List  -> [1, 2, 3]
- Methods:
    Tuple -> Only count(), index()
    List  -> append(), extend(), insert(), remove(), pop(), clear(), sort(), reverse()
- Performance:
    Tuple -> Faster due to immutability.
    List  -> Slightly slower because of mutability overhead.
- Memory:
    Tuple -> Uses less memory.
    List  -> Uses more memory (stores additional references for dynamic resizing).

Time Complexity Impact:
- Tuple creation: O(1)
- List dynamic operations (append/remove): Amortized O(1) but can trigger resizing.

Use Case:
- Tuple: When data should not change (coordinates, fixed config).
- List: When frequent updates are required.
"""

# --- Code Example (Tuple vs List) ---
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

# Accessing elements
print(my_tuple[1])  # Output: 2
print(my_list[1])   # Output: 2

# Attempt to modify
# my_tuple[0] = 10  # ❌ Will raise TypeError (Immutable)
my_list[0] = 10     # ✅ Allowed
print(my_list)      # Output: [10, 2, 3]

# Methods
tuple_count = my_tuple.count(2)
list_count = my_list.count(2)
print(tuple_count, list_count)  # Output: 1 1

"""
2. Tuple vs Dictionary
-----------------------
Similarities:
- Both can store heterogeneous data types.
- Both support iteration.

Differences:
- Structure:
    Tuple -> Ordered sequence (indexed by integers).
    Dictionary -> Key-value pairs (indexed by unique keys).
- Mutability:
    Tuple -> Immutable.
    Dictionary -> Mutable (keys and values can be added/removed/updated).
- Syntax:
    Tuple -> (1, 2, 3)
    Dictionary -> {"a": 1, "b": 2}
- Hashability:
    Tuple -> Hashable (if elements are hashable) -> can be used as dictionary keys.
    Dictionary -> Not hashable (cannot be used as dictionary keys).
- Methods:
    Tuple -> count(), index().
    Dictionary -> keys(), values(), items(), update(), get(), pop(), popitem(), clear().

Time Complexity Impact:
- Tuple lookup: O(1) by index.
- Dictionary lookup: O(1) average (hashing).

Use Case:
- Tuple: Fixed ordered data.
- Dictionary: Key-value mapping for fast lookups.
"""

# --- Code Example (Tuple vs Dictionary) ---
my_tuple = ("apple", "banana", "cherry")
my_dict = {"a": "apple", "b": "banana", "c": "cherry"}

# Accessing elements
print(my_tuple[1])    # Output: banana
print(my_dict["b"])  # Output: banana

# Tuple as dictionary key
location = {(10, 20): "Point A", (30, 40): "Point B"}
print(location[(10, 20)])  # Output: Point A

# Dictionary operations
my_dict["d"] = "dragonfruit"  # Adding key-value pair
print(my_dict)

# Checking membership
print("apple" in my_tuple)   # Output: True
print("b" in my_dict)        # Output: True
