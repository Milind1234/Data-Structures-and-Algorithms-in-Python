# accessing_elements_2d_array.py
# demonstrates how to access elements from a 2D array using NumPy

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

print("Original Array:")
print(arr_1)
# Output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# ---------------------------------------------
# SECTION: Accessing Elements from a 2D Array
# ---------------------------------------------
# Function to access a specific element using row and column index
# Time Complexity: O(1), Space Complexity: O(1)
def Access_Elements(array, row_idx, col_idx):
    """
    Access and print the element at the given row and column index.
    Parameters:
        array (np.array): The 2D NumPy array.
        row_idx (int): Row index to access.
        col_idx (int): Column index to access.
    """
    # Validate indices
    if row_idx >= array.shape[0] or col_idx >= array.shape[1]:
        print("Please provide a correct index.")
    else:
        print(f"Element at ({row_idx},{col_idx}):", array[row_idx][col_idx])
        # Output: Element at (2,3): 14

# Call the function to access element at row 2 and column 3
Access_Elements(arr_1, 2, 3)

# ASCII Visualization:
# Array Layout:
# Row\Col   0   1   2   3   4
#       ---------------------
#  0  |   1   2   3   4   5
#  1  |   6   7   8   9  10
#  2  |  11  12  13  14  15
#  3  |  16  17  18  19  20
# Accessing element at row 2 and column 3 gives value 14
