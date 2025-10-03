# =====================================================
# 🔍 Linear Search on Arrays using Python & NumPy
# =====================================================

# ---------------------------------------------
# 📘 Accessing Elements in an Array using Linear Search (using array module)
# ---------------------------------------------

import array as arr

# ✅ Step 1: Create an array of integers
arr_1 = arr.array('i', [1, 2, 3, 4, 5])

# ✅ Step 2: Define a function for linear search
def linear_search_array(array, target_value):
    for i in range(len(array)):
        if array[i] == target_value:
            return f"✅ Element {target_value} found at index {i}"
    return "❌ Element not present in array"

# ✅ Step 3: Take input from user
try:
    element = int(input("Enter the element you want to search in the array: "))
    result = linear_search_array(arr_1, element)
    print(result)
except ValueError:
    print("❌ Please enter a valid integer.")

# ---------------------------------------------
# 🧠 Time and Space Complexity for array module
# ---------------------------------------------
# Time Complexity: O(n)
#   - In the worst case, we may need to traverse the entire array.
#
# Space Complexity: O(1)
#   - No extra space is used except a few variables.

print("\n" + "="*52 + "\n")

# ---------------------------------------------
# 📘 Accessing Elements using Linear Search (using NumPy)
# ---------------------------------------------

import numpy as np

# ✅ Step 1: Create a NumPy array
myarr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

# ✅ Step 2: Define a function for linear search using NumPy
def linear_search_numpy(array, target):
    for idx, value in enumerate(array):
        if value == target:
            print(f"✅ Element {target} found at index {idx}")
            return
    print("❌ Element not present in array")

# ✅ Step 3: Call the function with a fixed value
linear_search_numpy(myarr, 14)

# ---------------------------------------------
# 🧠 Time and Space Complexity for NumPy array
# ---------------------------------------------
# Time Complexity: O(n)
#   - Same logic applies: worst case requires scanning entire array.
#
# Space Complexity: O(1)
#   - Constant extra space used.
