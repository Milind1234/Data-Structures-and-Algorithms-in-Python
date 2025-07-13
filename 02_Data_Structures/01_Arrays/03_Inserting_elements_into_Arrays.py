# -----------------------------------------
# Inserting Elements into Arrays in Python
# -----------------------------------------

# ✅ 1. Using the built-in array module

import array

# Create an array of integers
arr = array.array('i', [1, 2, 3])

# Append an element at the end (O(1) time)
arr.append(4)         # [1, 2, 3, 4]

# Insert an element at index 1 (O(n) time, due to shifting)
arr.insert(1, 10)     # [1, 10, 2, 3, 4]

# Extend array with multiple values (O(k), where k is number of elements)
arr.extend([5, 6])    # [1, 10, 2, 3, 4, 5, 6]

# Print the final array as a list
print("Built-in array after operations:", arr.tolist())

# Time and Space Complexity:
# append()  -> Time: O(1), Space: O(1)
# insert()  -> Time: O(n), Space: O(1)
# extend()  -> Time: O(k), Space: O(k)


# ✅ 2. Using NumPy array

import numpy as np

# Create a NumPy array
arr_np = np.array([1, 2, 3, 4, 5])

# Insert value 99 at index 2 (creates a new array)
new_arr_np = np.insert(arr_np, 2, 99)

# Original and modified arrays
print("Original NumPy array:", arr_np)
print("NumPy array after insertion:", new_arr_np)

# Time Complexity of np.insert() is O(n)
# Space Complexity is also O(n) as a new array is created

# Note:
# NumPy does not modify the array in place during insertion.
# It returns a new array with the inserted value.

# ✅ Summary of Time & Space Complexities:

# | Operation Type    | Method              | Time Complexity | Space Complexity |
# |-------------------|---------------------|------------------|------------------|
# | Insert at end     | arr.append(x)       | O(1)             | O(1)             |
# | Insert at index i | arr.insert(i, x)    | O(n)             | O(1)             |
# | Extend array      | arr.extend(iter)    | O(k)             | O(k)             |
# | NumPy insert      | np.insert(arr, i, x)| O(n)             | O(n)             |


