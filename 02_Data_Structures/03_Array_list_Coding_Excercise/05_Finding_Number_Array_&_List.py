"""
2. Linear Search in Array or List
Difficulty: Easy

🔍 Problem:
Given a list or array of integers, implement a function to find the **index of a given target element**.
If the element is found, print the index. If not, print a message saying it's not found.

📌 Example:
Input: array = [1, 2, 3, ..., 20], target = 14
Output: ✅ Element 14 found at index 13

🧾 Constraints:
- The array can be a Python list or NumPy array.
- Values are integers.
- Return or print the index of the first occurrence of the target.

------------------------------------------------------------

💡 Optimal Steps to Code the Solution:

1. Loop through the list or array.
2. For each element, compare it with the target.
3. If match found, print the index and return.
4. If loop ends without match, print that element wasn't found.

------------------------------------------------------------

🧠 Explanation of `enumerate()`:
`enumerate()` gives both the **index** and **value** of an element in a loop.

Example:
    for idx, val in enumerate([5, 10, 15]):
        print(idx, val)

Output:
    0 5
    1 10
    2 15

Helps when we need both element **value** and its **position**.

------------------------------------------------------------

📊 Time and Space Complexity:

Time Complexity:
    - Best Case: O(1) → Target is at the beginning
    - Worst Case: O(n) → Target is at the end or not present
    - Average Case: O(n)

Space Complexity:
    - O(1) → No extra space used, just iterating through the input array
"""

# ✅ Linear Search using NumPy Array and enumerate()

import numpy as np

# Creating NumPy array from 1 to 20
myarr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                  11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def linear_search_array(array, target):
    """
    Performs linear search on a NumPy array using enumerate.
    Prints the index if found, else a not found message.
    """
    for idx, val in enumerate(array):
        if val == target:
            print(f"✅ Element {target} found at index {idx}")
            return
    print("❌ Element not found.")

# Taking user input safely
try:
    val = int(input("Enter the number to search in NumPy array: "))
    linear_search_array(myarr, val)
except ValueError:
    print("❌ Please enter a valid integer.")

# ------------------------------------------------------------

# ✅ Linear Search using Python List and classic indexing

# Creating list from 1 to 20
mylist = list(range(1, 21))  # Same as [1, 2, ..., 20]

def linear_search_list(array, target):
    """
    Performs linear search on a Python list using index-based looping.
    Prints the index if found, else a not found message.
    """
    for i in range(len(array)):
        if array[i] == target:
            print(f"✅ Element {target} found at index {i}")
            return
    print("❌ Element not found.")

# Example call with list version
print("\n--- List Search Example ---")
linear_search_list(mylist, 14)
