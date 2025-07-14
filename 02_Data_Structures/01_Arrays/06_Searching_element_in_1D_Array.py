# ---------------------------------------------
# 📘 Accessing Elements in an Array using Linear Search
# ---------------------------------------------

import array as arr

# ✅ Step 1: Create an array of integers
arr_1 = arr.array('i', [1, 2, 3, 4, 5])

# ✅ Step 2: Define a function for linear search
def linear_search(array, target_value):
    for i in range(len(array)):
        if array[i] == target_value:
            return f"✅ Element {target_value} found at index {i}"
    return "❌ Element not present in array"

# ✅ Step 3: Take input from user
try:
    element = int(input("Enter the element you want to search in the array: "))
    result = linear_search(arr_1, element)
    print(result)
except ValueError:
    print("❌ Please enter a valid integer.")

# ---------------------------------------------
# 🧠 Time and Space Complexity
# ---------------------------------------------
# Time Complexity: O(n)
#   - In the worst case, we may need to traverse the entire array.
#
# Space Complexity: O(1)
#   - No extra space is used except a few variables.
