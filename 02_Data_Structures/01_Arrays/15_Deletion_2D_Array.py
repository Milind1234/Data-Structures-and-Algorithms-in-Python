# deletion_2D_array.py
# 🧹 Deleting rows and columns in 2D NumPy arrays
# Note: NumPy does NOT support deleting individual elements (cells)
# Time Complexity: O(mn), Space Complexity: O(mn)

import numpy as np

# ---------------------------------------------------------
# Creating a sample 2D array (3x3)
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original 2D Array:")
print(arr)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# ---------------------------------------------------------
# ❌ Cannot delete a single element in NumPy 2D array
# It must remain rectangular (same number of columns in every row)

# ---------------------------------------------------------
# ✅ Deleting a ROW using np.delete
# Syntax: np.delete(array, row_index, axis=0)
row_deleted = np.delete(arr, 1, axis=0)  # Delete 2nd row (index 1)
print("\nArray after deleting row at index 1:")
print(row_deleted)
# Output:
# [[1 2 3]
#  [7 8 9]]

# ---------------------------------------------------------
# ✅ Deleting a COLUMN using np.delete
# Syntax: np.delete(array, col_index, axis=1)
col_deleted = np.delete(arr, 0, axis=1)  # Delete 1st column (index 0)
print("\nArray after deleting column at index 0:")
print(col_deleted)
# Output:
# [[2 3]
#  [5 6]
#  [8 9]]

# ---------------------------------------------------------
# 📈 Complexity Analysis:
# Time Complexity: O(mn) - because a new array is created
# Space Complexity: O(mn) - same reason, due to copying data

# ---------------------------------------------------------
# 📝 Summary:
# - Deletion of rows and columns is possible using np.delete()
# - Cannot delete a single cell
# - Always results in a new array (not in-place)
