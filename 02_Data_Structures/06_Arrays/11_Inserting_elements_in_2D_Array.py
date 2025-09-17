# Inserting_elements_into_2d_array.py
# -----------------------------------------------
# Demonstration of inserting rows and columns
# into a 2D array using NumPy in Python.
# -----------------------------------------------

import numpy as np

# ============================
# ============================
# Original 2D Array (4x5):
# +----+----+----+----+----+
# |  1 |  2 |  3 |  4 |  5 |
# |  6 |  7 |  8 |  9 | 10 |
# | 11 | 12 | 13 | 14 | 15 |
# | 16 | 17 | 18 | 19 | 20 |
# +----+----+----+----+----+

# ------------------------------------------------------------
# Creating the initial 2D array using np.array()
# Shape: (4 rows, 5 columns)
# ------------------------------------------------------------
arr_1 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])
print("Original Array:")
print(arr_1)
# Output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# =============================================================
# Insertion using np.insert(array, index, values, axis)
# =============================================================
# Parameters:
# - array: the original array
# - index: the row/column index where new data is inserted
# - values: the new row/column to insert (must match shape!)
# - axis: 0 for row-wise insertion, 1 for column-wise insertion

# -----------------------------
# Insert a new ROW at index 4
# -----------------------------
new_row = [[21, 22, 23, 24, 25]]
new_arr_1 = np.insert(arr_1, 4, new_row, axis=0)
print("\nArray after inserting new row at index 4:")
print(new_arr_1)
# Output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

# Time Complexity: O(mn) where m = columns, n = rows
# Space Complexity: O(mn) for allocating new memory

# -------------------------------
# Insert a new COLUMN at index 0
# -------------------------------
new_column = [[100], [200], [300], [400], [500]]  # Must match row count (5)
new_arr_2 = np.insert(new_arr_1, 0, new_column, axis=1)
print("\nArray after inserting new column at index 0:")
print(new_arr_2)
# Output:
# [[100   1   2   3   4   5]
#  [200   6   7   8   9  10]
#  [300  11  12  13  14  15]
#  [400  16  17  18  19  20]
#  [500  21  22  23  24  25]]

# =============================================================
# Append using np.append(array, values, axis)
# =============================================================
# - Appends values to the END along specified axis.
# - Must match dimension count along non-appended axis

# -----------------------------
# Append a new ROW at the end
# -----------------------------
arr_2 = np.array([
    [31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45],
    [46, 47, 48, 49, 50]
])
print("\nNew array before append:")
print(arr_2)
# Output:
# [[31 32 33 34 35]
#  [36 37 38 39 40]
#  [41 42 43 44 45]
#  [46 47 48 49 50]]

new_arr_3 = np.append(arr_2, [[51, 52, 53, 54, 55]], axis=0)
print("\nArray after appending a new row at end:")
print(new_arr_3)
# Output:
# [[31 32 33 34 35]
#  [36 37 38 39 40]
#  [41 42 43 44 45]
#  [46 47 48 49 50]
#  [51 52 53 54 55]]

# Time Complexity: O(mn)
# Space Complexity: O(mn)

# =============================================================
# Summary:
# - Use insert() to add row/column at specific position
# - Use append() to add row/column at the end
# - Ensure shape compatibility when using insert/append
# =============================================================
