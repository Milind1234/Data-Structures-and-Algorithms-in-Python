# ================================
# Common Elements from Two Tuples
# ================================

# --- Problem Statement ---
# Write a function that takes two tuples and returns a tuple 
# containing the common elements of the input tuples.

# Example:
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# output_tuple = common_elements(tuple1, tuple2)
# Expected output: (4, 5)

# --- Approach ---
# 1. Convert both tuples to sets (for efficient membership check).
# 2. Find intersection of these sets using '&' operator.
# 3. Convert the resulting intersection back to a tuple.
# 4. Return the tuple as result.

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

# --- Example Run ---
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Output: (4, 5)

# --- Time and Space Complexity ---
# 1. set(tuple1) -> O(n)
# 2. set(tuple2) -> O(m)
# 3. Intersection operation (&) -> O(min(n, m))
# 4. Conversion to tuple -> O(k), where k is number of common elements
# Overall:
# Time Complexity -> O(n + m)
# Space Complexity -> O(n + m)
