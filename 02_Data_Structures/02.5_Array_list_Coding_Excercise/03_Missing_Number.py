# 🧩 Missing Number

"""
Problem Statement:
Write a function to find the missing number in a given integer array of 1 to n.
The function takes two parameters:
1. The array (or list) with one number missing
2. The total count of numbers expected (from 1 to n)

Example:
missing_number([1, 2, 3, 4, 6], 6)  # Output: 5
"""

# ✅ Optimal Steps to Solve:
# 1. Calculate the expected sum of numbers from 1 to n using the formula: n*(n+1)//2
# 2. Calculate the actual sum of the given array or list.
# 3. Subtract actual sum from expected sum to find the missing number.
# 4. Practice using both arrays (using `array` module) and lists.

# ------------------ Using array ------------------

import array as arr

# Step 1: Create an array from 1 to 100
my_array = arr.array('i', [i for i in range(1, 101)])

# Step 2: Remove a specific number (e.g., 73) using remove
my_array.remove(73)

# Step 3: Display the modified array
print("Using array — array after removing one element:")
print(my_array.tolist())

# Step 4: Define the missing number function (for array)
def missing_number_array(array, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(array)
    return expected_sum - actual_sum

# Step 5: Call the function and print result
print(f"Missing number (using array): {missing_number_array(my_array, 100)}")

# ------------------ Using list ------------------

# Step 1: Create a list from 1 to 100
my_list = [i for i in range(1, 101)]

# Step 2: Remove one number (e.g., number 73)
my_list.remove(73)

# Step 3: Display the modified list
print("\nUsing list — list after removing one element:")
print(my_list)

# Step 4: Define the missing number function (for list)
def missing_number_list(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

# Step 5: Call the function and print result
print(f"Missing number (using list): {missing_number_list(my_list, 100)}")
