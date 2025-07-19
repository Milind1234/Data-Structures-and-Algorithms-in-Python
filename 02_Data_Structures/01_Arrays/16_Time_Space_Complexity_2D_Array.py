# array_2d_complexity.py
"""
📘 2D Array Operations - Time and Space Complexity Summary
This file provides an overview of time and space complexity for common operations on 2D arrays.
Each operation includes:
✅ Description
✅ Time Complexity
✅ Space Complexity

Assuming the array has dimensions m x n (m rows and n columns)
"""

# ----------------------------------------------------------------------------
# 1️⃣ Creating an Empty 2D Array
# ----------------------------------------------------------------------------
# Time Complexity: O(1) — No elements initialized
# Space Complexity: O(1) — No memory reserved for values

# Example (empty array)
empty_array = []

# ----------------------------------------------------------------------------
# 2️⃣ Creating a 2D Array with Elements
# ----------------------------------------------------------------------------
# Time Complexity: O(mn) — Each value is initialized
# Space Complexity: O(mn) — Space allocated for m * n elements

import numpy as np
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# ----------------------------------------------------------------------------
# 3️⃣ Inserting a Row/Column into a 2D Array
# ----------------------------------------------------------------------------
# Time Complexity: O(mn) — Every element may need to be shifted/copied
# Space Complexity: O(mn) — New array of updated size is created

# Example: insert a row
new_row = [10, 11, 12]
inserted = np.insert(array_2d, 1, new_row, axis=0)  # Insert at row index 1

# ----------------------------------------------------------------------------
# 4️⃣ Traversing a 2D Array
# ----------------------------------------------------------------------------
# Time Complexity: O(mn) — Each element visited once
# Space Complexity: O(1) — No extra space used

def traverse_array(arr):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            print(arr[i][j], end=' ')
        print()

# ----------------------------------------------------------------------------
# 5️⃣ Accessing a Given Cell
# ----------------------------------------------------------------------------
# Time Complexity: O(1) — Direct indexing
# Space Complexity: O(1)

cell = array_2d[1][2]  # Accessing element at row=1, col=2 => value = 6

# ----------------------------------------------------------------------------
# 6️⃣ Searching for a Given Value
# ----------------------------------------------------------------------------
# Time Complexity: O(mn) — Worst-case: scan entire array
# Space Complexity: O(1)

def search_element(arr, target):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i][j] == target:
                return f"Found at ({i},{j})"
    return "Not found"

# ----------------------------------------------------------------------------
# 7️⃣ Deleting a Row/Column from a 2D Array
# ----------------------------------------------------------------------------
# Time Complexity: O(mn) — Elements must be copied over
# Space Complexity: O(mn) — New array created after deletion

# Example: delete row at index 1
deleted = np.delete(array_2d, 1, axis=0)

# ----------------------------------------------------------------------------
# 📌 Summary Table (for reference)
#
# Operation                        Time Complexity     Space Complexity
# ----------------------------------------------------------------------
# Creating an empty array         O(1)                O(1)
# Creating with elements          O(mn)               O(mn)
# Inserting column/row            O(mn)               O(mn)
# Traversing the array            O(mn)               O(1)
# Accessing a given cell          O(1)                O(1)
# Searching a given value         O(mn)               O(1)
# Deleting a column/row           O(mn)               O(mn)
# ----------------------------------------------------------------------
