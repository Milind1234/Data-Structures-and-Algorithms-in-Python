# ========================
# Tuple Notes (Complete)
# ========================

# --- 1. Creating Tuples ---
# Tuples are immutable sequences in Python.
# Syntax: values separated by commas, usually enclosed in parentheses.

# Examples of tuple creation:
t1 = ("a", "b", "c", "d", "e")       # Normal tuple
t2 = ("a",)                            # Single-element tuple (comma is required)
t3 = tuple()                            # Empty tuple using tuple() function
t4 = tuple("abcde")                     # Converts iterable (string) to tuple

# Time Complexity (Creation): O(1)
# Space Complexity: O(n) where n = number of elements

# --- 2. Memory Layout & Accessing Elements ---
# Tuples store elements in contiguous memory.
# Elements accessed using indices (positive & negative) and slicing.

tuple_sample = ("a", "b", "c", "d", "e")
print(tuple_sample[1])       # Output: 'b' (Indexing)
print(tuple_sample[-1])      # Output: 'e' (Negative Index)
print(tuple_sample[1:4])     # Output: ('b','c','d') (Slicing)
# Time Complexity (Indexing): O(1)
# Time Complexity (Slicing): O(k) where k = slice length

# --- 3. Traversing Tuples ---
# Method 1: Direct iteration
for item in tuple_sample:
    print(item)

# Method 2: Using range and index
for i in range(len(tuple_sample)):
    print(tuple_sample[i])
# Time Complexity: O(n) | Space Complexity: O(1)

# --- 4. Searching Elements ---
# Method 1: Using 'in' operator
print('a' in tuple_sample)       # Output: True

# Method 2: Using index() method
print(tuple_sample.index('c'))   # Output: 2
# Raises ValueError if not found

# Method 3: Custom function with message
def search_tuple(t, element):
    for i in range(len(t)):
        if t[i] == element:
            return f"Element '{element}' found at index {i}"
    return "Element not found"

print(search_tuple(tuple_sample, 'b'))
print(search_tuple(tuple_sample, 'z'))
# Time Complexity: O(n) | Space Complexity: O(1)

# --- 5. Tuple Operations ---
t1 = (1, 2, 3)
t2 = (4, 5, 6)
# Concatenation (+)
print(t1 + t2)           # (1, 2, 3, 4, 5, 6)
# Repetition (*)
print(t1 * 3)            # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# Membership (in)
print(2 in t1)           # True

# --- 6. Tuple Methods ---
t3 = (1, 2, 2, 3, 4)
print(t3.count(2))       # Output: 2
print(t3.index(3))       # Output: 3
# Time Complexity: count() -> O(n), index() -> O(n)

# --- 7. Useful Built-in Functions ---
t4 = (3, 1, 4, 2, 5)
print(len(t4))           # 5 (O(1))
print(max(t4))           # 5 (O(n))
print(min(t4))           # 1 (O(n))
print(sum(t4))           # 15 (O(n))
print(sorted(t4))        # [1, 2, 3, 4, 5] (O(n log n))
print(any(t4))           # True (O(n))
print(all(t4))           # False (O(n))
print(list(enumerate(t4)))   # [(0,3), (1,1), ...] (O(n))
print(tuple(reversed(t4)))   # (5, 2, 4, 1, 3) (O(n))
t5 = ("a", "b", "c")
t6 = (1, 2, 3)
print(list(zip(t5, t6)))     # [('a',1), ('b',2), ('c',3)] (O(n))

# --- 7. Useful Built-in Functions (with join) ---
t5 = ("Hello", "World", "from", "Python")
print(" ".join(t5))   # Output: 'Hello World from Python'
# Time Complexity of join -> O(n) where n = total length of all strings
# Space Complexity -> O(n) (creates a new string)


# --- 8. Conversion ---
list_data = [10, 20, 30]
converted_tuple = tuple(list_data)
print(converted_tuple)       # (10, 20, 30)

# --- Time & Space Complexity Summary ---
# Access by index -> O(1)
# Traversal -> O(n)
# Searching (in, index, count) -> O(n)
# Concatenation -> O(n+m)
# Repetition -> O(n*k)
# Built-in functions:
#    len -> O(1), max/min -> O(n), sum -> O(n), sorted -> O(n log n)
# Space Complexity for tuples -> O(n)
