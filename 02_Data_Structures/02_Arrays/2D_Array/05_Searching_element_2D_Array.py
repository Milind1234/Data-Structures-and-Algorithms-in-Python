# searching_elements_in_2D_Array.py
# This script demonstrates how to search for a specific element in a 2D NumPy array
# Includes element search logic, break optimization, and complexity analysis

import numpy as np

# ---------------------------------------------
# SECTION: Creating a 2D NumPy Array
# ---------------------------------------------
# Time Complexity: O(mn), Space Complexity: O(mn)
# m = number of rows, n = number of columns
arr_1 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

print("Original 2D Array:")
print(arr_1)
# Output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# ---------------------------------------------
# SECTION: Searching for an Element in 2D Array
# ---------------------------------------------
# Time Complexity: O(mn) in the worst case (element not found)
# Space Complexity: O(1)
def Search_element(array, target_value):
    """
    Search for a target value in the 2D array.
    If found, prints its row and column index.
    """
    found = False  # 🔍 Initialize a flag to track if the element is found
    
    for i in range(array.shape[0]):              # Loop over rows
        for j in range(array.shape[1]):          # Loop over columns
            if target_value == array[i][j]:
                print(f"✅ Target element {target_value} found at row {i} and column {j}")
                found = True
                break  # Exit the inner loop if element is found
        if found:
            break      # Exit the outer loop if element is found

    if not found:
        print("❌ Element not found")

# Example Call
Search_element(arr_1, 14)
# Output:
# ✅ Target element 14 found at row 2 and column 3

# ---------------------------------------------
# Additional Notes:
# ---------------------------------------------
# If the element is not in the array, it prints "Element not found"
# This approach avoids printing multiple unnecessary messages.

# ✨ Complexity Explanation:
# Outer loop runs 'm' times (rows)
# Inner loop runs 'n' times (columns)
# Total operations = m * n  -> O(mn)
# If the array is square (m = n),
# Then complexity = O(n^2)
# 

# Row\Col   0   1   2   3   4
#       ---------------------
#  0  |   1   2   3   4   5
#  1  |   6   7   8   9  10
#  2  |  11  12  13  14  15  <- ✅ Found here
#  3  |  16  17  18  19  20
