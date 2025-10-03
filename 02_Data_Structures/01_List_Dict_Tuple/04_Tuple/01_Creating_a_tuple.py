# =========================================================
# Tuples in Python - Creation Methods
# =========================================================
# A Tuple is an ordered, immutable collection of elements.
# - Elements can be of any type (mixed types allowed).
# - Indexed by integers (similar to lists).
# - Immutable → values cannot be changed after creation.
# - Hashable → can be used as dictionary keys.
# =========================================================

# ---------------------------------------------------------
# 1. Creating Tuple Using Parentheses (Common Method)
# ---------------------------------------------------------
# Syntax:
# tuple_name = (val1, val2, val3, ...)
# Time Complexity: O(1) (elements predefined)
# Space Complexity: O(n) (n = number of elements)

tuple1 = ('a', 'b', 'c', 'd', 'e')
print("Tuple1:", tuple1)   # Output: ('a', 'b', 'c', 'd', 'e')


# ---------------------------------------------------------
# 2. Creating Tuple Without Parentheses (Tuple Packing)
# ---------------------------------------------------------
# Just use comma-separated values (parentheses optional).
# But parentheses improve readability.
# Syntax:
# tuple_name = val1, val2, val3, ...
# Time Complexity: O(1)
# Space Complexity: O(n)

tuple2 = 'a', 'b', 'c'
print("Tuple2:", tuple2)   # Output: ('a', 'b', 'c')


# ---------------------------------------------------------
# 3. Creating Single-Element Tuple
# ---------------------------------------------------------
# IMPORTANT: Need a trailing comma to make it a tuple.
# Syntax:
# single_tuple = (element,)
# Time Complexity: O(1)
# Space Complexity: O(1)

single_tuple = ('a',)
print("Single element tuple:", single_tuple)  # Output: ('a',)
not_tuple = ('a')  # This is just a string, not a tuple
print("Not tuple:", not_tuple)                # Output: a


# ---------------------------------------------------------
# 4. Creating Empty Tuple
# ---------------------------------------------------------
# Syntax:
# empty_tuple = ()
# Time Complexity: O(1)
# Space Complexity: O(1)

empty_tuple = ()
print("Empty Tuple:", empty_tuple)   # Output: ()


# ---------------------------------------------------------
# 5. Using tuple() Constructor (From Iterable)
# ---------------------------------------------------------
# Syntax:
# tuple_name = tuple(iterable)
# Converts any iterable (list, string, etc.) to a tuple.
# Time Complexity: O(n) (iterates through all elements)
# Space Complexity: O(n)

# Converting string → tuple of characters
tuple_from_string = tuple("abcde")
print("Tuple from string:", tuple_from_string)
# Output: ('a', 'b', 'c', 'd', 'e')

# Converting list → tuple
list_data = [1, 2, 3, 4]
tuple_from_list = tuple(list_data)
print("Tuple from list:", tuple_from_list)
# Output: (1, 2, 3, 4)


# =========================================================
# COMPLEXITY SUMMARY:
# - Creating a tuple with known elements → O(1)
# - Creating a tuple from iterable (tuple()) → O(n)
# - Space Complexity: O(n) for n elements
# =========================================================
