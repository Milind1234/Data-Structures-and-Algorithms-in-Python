# 📘 Searching Elements in Python List

# ----------------------------------------
# 🔢 Sample List and Target
# ----------------------------------------
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

# ----------------------------------------
# ✅ Method 1: Using "in" Operator
# ----------------------------------------

# Python's built-in "in" operator performs a linear search under the hood
if target in my_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

"""
🕒 Time Complexity: O(n)
🧠 Space Complexity: O(1)
- n = number of elements in the list
- Python loops through each element to check for the match
"""

# ----------------------------------------
# 🔍 Method 2: Custom Linear Search Function
# ----------------------------------------

def linear_search(l1, t1):
    """
    Perform a linear search to find the index of target `t1` in list `l1`.
    Returns:
        Index of target if found, else -1.
    """
    for idx, value in enumerate(l1):  # Loop with both index and value
        if value == t1:               # Check if current value matches target
            return idx                # Return the index if found
    return -1                         # Return -1 if not found

# 🔧 Call the function
result = linear_search(my_list, target)

# 🖨 Output the result
if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list")

"""
🧠 LINEAR SEARCH EXPLAINED:

- Traverse the list from left to right.
- For each element, check if it equals the target.
- Stop when found; else return -1.

🕒 Time Complexity: 
- Best Case: O(1) → target is at the start
- Average/Worst Case: O(n) → target is at the end or not present

🧠 Space Complexity: O(1)
- No extra space is used except a few variables
"""

# ----------------------------------------
# ✅ Summary
# ----------------------------------------
"""
✔ Use `in` for quick readability when only existence matters.
✔ Use custom linear search if:
   - You need the index of the element
   - You want more control over matching logic
"""
