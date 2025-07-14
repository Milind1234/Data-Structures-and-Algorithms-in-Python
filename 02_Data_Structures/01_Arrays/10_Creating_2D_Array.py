# two_dimensional_array_intro.py
# Complete introduction to 2D arrays in Python with examples, explanation, and complexity

# -------------------------------
# ✅ What is a 2D Array?
# -------------------------------
# A 2D array is a grid/matrix of elements arranged in rows and columns.
# Each element is accessed via two indices: a[i][j] where:
#   - i = row index
#   - j = column index

# Example Layout:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# -------------------------------
# ✅ Why use a 2D Array?
# -------------------------------
# - Representing matrix operations
# - Game board grids (e.g. Tic Tac Toe)
# - Image pixels (rows x columns)
# - Storing tabular data (e.g. temperature, student marks)

# -------------------------------
# ✅ Creating a 2D Array in Python
# -------------------------------

# 🔸 Method 1: Using Native Python Lists
matrix_native = [
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
]
print("\n2D Array using native lists:")
for row in matrix_native:
    print(row)

# 🔸 Method 2: Using NumPy (Recommended for numerical tasks)
import numpy as np

matrix_numpy = np.array([
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
])

print("\n2D Array using NumPy:")
print(matrix_numpy)

# -------------------------------
# ✅ Accessing Elements
# -------------------------------
print("\nAccess element at row 1, column 2:", matrix_numpy[1][2])  # Output: 11

# -------------------------------
# ✅ Time and Space Complexity
# -------------------------------
# If m = number of rows, n = number of columns
#
# Creating a 2D array:
#   Time Complexity  => O(m * n)
#   Space Complexity => O(m * n)
#
# Accessing an element:
#   Time Complexity  => O(1)
#
# Traversing all elements:
#   Time Complexity  => O(m * n)

# -------------------------------
# ✅ Use Case Example: Temperature Recording
# -------------------------------
# Scenario: Temperature is recorded 4 times per day for 4 days.
# So we store this data in a 4x4 2D array.

temps = np.array([
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
])

print("\nTemperature grid (4x4):")
print(temps)

# -------------------------------
# ✅ Summary
# -------------------------------
# - A 2D array is a powerful way to represent structured tabular data
# - Use native lists for simple cases; NumPy for numerical/matrix operations
# - Time and space complexity is typically O(m * n) for creation and traversal
