# ================================
# Differences Between Dictionary and List
# ================================

# 1. ORDER OF ELEMENTS
# ------------------------------
# Dictionary (before Python 3.7) → Unordered collection (keys may not follow insertion order)
# Python 3.7+ maintains insertion order but still behaves differently from a list.
# List → Ordered collection (elements remain in the same order as inserted)

# Example:
my_dict = {"b": 2, "a": 1, "c": 3}
my_list = [2, 1, 3]

print("Dictionary:", my_dict)   # Might not follow declared order (in Python 3.7+ it does)
print("List:", my_list)         # Always follows declared order
# Output:
# Dictionary: {'b': 2, 'a': 1, 'c': 3}
# List: [2, 1, 3]

# ------------------------------

# 2. ACCESSING ELEMENTS
# ------------------------------
# Dictionary → Access values using KEYS
# List → Access values using INDEX
print(my_dict["a"])   # Access using key → Output: 1
print(my_list[1])     # Access using index → Output: 1

# ------------------------------

# 3. DATA STORAGE STRUCTURE
# ------------------------------
# Dictionary → Key-Value Pairs
# List → Single elements only

# Dictionary Example:
student = {"name": "Alex", "age": 20}
# List Example:
marks = [85, 90, 78]

print("Dictionary Example:", student)
print("List Example:", marks)
# Output:
# Dictionary Example: {'name': 'Alex', 'age': 20}
# List Example: [85, 90, 78]

# ------------------------------

# 4. UNIQUENESS OF ELEMENTS
# ------------------------------
# Dictionary → Keys must be UNIQUE (no duplicate keys allowed)
# List → Allows duplicate elements

# Example:
my_dict = {"a": 1, "b": 2, "a": 3}   # Last duplicate key "a" overwrites previous value
my_list = [1, 2, 2, 3, 1]            # Duplicates allowed
print("Dictionary with duplicate key:", my_dict)  # {'a': 3, 'b': 2}
print("List with duplicate elements:", my_list)   # [1, 2, 2, 3, 1]

# ------------------------------

# SUMMARY:
# - Dictionary: Unordered (pre-3.7), Key-Value pairs, Access via keys, No duplicate keys
# - List: Ordered, Single values, Access via index, Allows duplicates
