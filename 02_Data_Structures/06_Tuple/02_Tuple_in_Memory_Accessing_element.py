# ==============================================================
# Tuples in Memory & Accessing Elements
# ==============================================================

# -------------------------------
# How Tuples are Stored in Memory?
# -------------------------------
# - Tuples are stored in **contiguous memory blocks** (like lists & arrays).
# - This makes element access **extremely fast** (O(1)).
# - Tuples are **immutable**, meaning values cannot be modified once created.
# - They are hashable → can be used as dictionary keys.

# ==============================================================
# Accessing Tuple Elements
# ==============================================================

# Sample Tuple
sample_tuple = ('a', 'b', 'c', 'd', 'e')
print("Sample Tuple:", sample_tuple)  # Output: ('a', 'b', 'c', 'd', 'e')

# -------------------------------
# 1. Index Access (Positive Index)
# -------------------------------
# Syntax: tuple_name[index]
# Index starts at 0
second_element = sample_tuple[1]
print("Second element (index 1):", second_element)  # Output: b

# -------------------------------
# 2. Index Access (Negative Index)
# -------------------------------
# - Negative indices start from the end
# - -1 → last element, -2 → second last
last_element = sample_tuple[-1]
print("Last element (index -1):", last_element)    # Output: e
second_last = sample_tuple[-2]
print("Second last (index -2):", second_last)      # Output: d

# ==============================================================
# Tuple Slicing
# ==============================================================
# Syntax: tuple_name[start:end]
# - Returns elements from 'start' index up to, but not including, 'end'.
# - Works same as lists.
slice_1_to_3 = sample_tuple[1:3]   # Index 1 and 2 only
print("Slice (1:3):", slice_1_to_3)  # Output: ('b', 'c')

slice_start_to_3 = sample_tuple[:3]  # From index 0 to 2
print("Slice (:3):", slice_start_to_3)  # Output: ('a', 'b', 'c')

slice_1_to_end = sample_tuple[1:]     # From index 1 till end
print("Slice (1:):", slice_1_to_end)  # Output: ('b', 'c', 'd', 'e')

full_slice = sample_tuple[:]          # All elements
print("Full Slice [:]:", full_slice)  # Output: ('a', 'b', 'c', 'd', 'e')

# ==============================================================
# Tuples are Immutable
# ==============================================================
# Attempting to modify an element raises an error:
# sample_tuple[0] = 'F'  # ❌ Raises TypeError

# ==============================================================
# Complexity:
# - Access element by index: O(1)
# - Slice operation: O(k) (k = length of slice)
# - Space Complexity: O(n) (n = tuple length)
# ==============================================================

