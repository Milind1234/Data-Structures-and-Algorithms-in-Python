# Insert at the Beginning of a Tuple
"""
Question:
---------
Write a function that takes a tuple and a value, and returns a new tuple 
with the value inserted at the beginning of the original tuple.

Example:
--------
input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_at_beginning(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)
"""

# ----------------------------- #
# Solution 1: Using concatenation
# ----------------------------- #
def insert_value_front(input_tuple, value_to_insert):
    """Insert value at the beginning using concatenation."""
    return (value_to_insert,) + input_tuple


# ----------------------------- #
# Solution 2: Using tuple unpacking (Pythonic)
# ----------------------------- #
def insert_value_unpacking(input_tuple, value_to_insert):
    """Insert value at the beginning using tuple unpacking."""
    return (value_to_insert, *input_tuple)


# ----------------------------- #
# Explanation:
# ----------------------------- #
"""
1. (value_to_insert,) creates a single-element tuple.
2. Concatenation (+) creates a new tuple by copying elements (Solution 1).
3. Tuple unpacking (*input_tuple) expands existing tuple elements inline (Solution 2).
4. Both approaches return a new tuple because tuples are immutable.
"""

# ----------------------------- #
# Time & Space Complexity:
# ----------------------------- #
"""
Time Complexity: O(n)
- Each element of the original tuple is copied once.

Space Complexity: O(n)
- A new tuple with n+1 elements is created.
"""

# ----------------------------- #
# Example Usage:
# ----------------------------- #
if __name__ == "__main__":
    input_tuple = (2, 3, 4)
    value_to_insert = 1
    print(insert_value_front(input_tuple, value_to_insert))   # (1, 2, 3, 4)
    print(insert_value_unpacking(input_tuple, value_to_insert))  # (1, 2, 3, 4)
