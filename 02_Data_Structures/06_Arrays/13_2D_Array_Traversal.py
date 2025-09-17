# 🔍 demonstrates how to traverse a 2D NumPy array row by row.
# 📌 It prints each element along with its position using nested loops.
# 🧠 Time Complexity: O(mn) | Space Complexity: O(1)
# Where m = number of rows, n = number of columns

import numpy as np

# ✅ Create a 2D NumPy array (4 rows x 5 columns)
arr_1 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

print("📦 Original Array:")
print(arr_1)
# Output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# 🔄 Function to traverse 2D array and print every element
def Array_Traversal(array):
    """
    🛠️ Traverses a 2D array and prints the position and value of each element.
    Parameters:
        array (np.array): 2D NumPy array
    """
    print("\\n🚀 Traversing the 2D array:")
    for i in range(array.shape[0]):  # loop through rows
        for j in range(array.shape[1]):  # loop through columns
            print(f"📍 Element at row {i}, column {j} ➡️   {array[i][j]}")
        print("🔚 End of row", i)

# 🧪 Call the function
Array_Traversal(arr_1)

# 🧮 Time Complexity: O(m * n) – every element is visited once
# 🗃️ Space Complexity: O(1) – no extra space used besides loop counters
# ------------------------------------------
# ✨ Complexity Explanation:
# Outer loop runs 'm' times (rows)
# Inner loop runs 'n' times (columns)
# Total operations = m * n  -> O(mn)
# If the array is square (m = n),
# Then complexity = O(n^2)
# 
# ✅ Space Complexity remains O(1) as we use no extra space.
# ------------------------------------------