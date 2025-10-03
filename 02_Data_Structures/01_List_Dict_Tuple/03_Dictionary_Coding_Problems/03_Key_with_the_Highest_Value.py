# ===============================================
# Problem: Key with the Highest Value in Dictionary
# ===============================================

"""
Given a dictionary, return the key that has the highest value.

Example:
---------
my_dict = {'a': 5, 'b': 9, 'c': 2}
Output: 'b'
"""

# ==================================================
# 1. Basic Approach (Manual Tracking)
# ==================================================
# Steps:
#   - Initialize max_value = -∞ and max_key = None
#   - Iterate over dictionary key, value pairs
#   - If current value > max_value → update max_value & max_key
#   - Return max_key
#
# Time Complexity: O(n) → One pass through dictionary
# Space Complexity: O(1) → No extra data structures used
#
def max_value_key_basic(my_dict):
    max_value = float('-inf')
    max_key = None
    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

# Example Test
my_dict = {'a': 5, 'b': 9, 'c': 2}
print("Basic Approach Output:", max_value_key_basic(my_dict))  # Output: b


# ==================================================
# 2. Pythonic Approach using max() and key parameter
# ==================================================
# Steps:
#   - Use built-in max() function
#   - key=my_dict.get ensures comparison is based on dictionary values
#
# Time Complexity: O(n) → Internally max() still checks all items
# Space Complexity: O(1)
#
def max_value_key_pythonic(my_dict):
    return max(my_dict, key=my_dict.get)

# Example Test
print("Pythonic Approach Output:", max_value_key_pythonic(my_dict))  # Output: b


# ==================================================
# 3. Handling Edge Cases
# ==================================================
#   - Empty dictionary → return None
#   - All equal values → returns first maximum key encountered
#
def max_value_key_safe(my_dict):
    if not my_dict:
        return None
    return max(my_dict, key=my_dict.get)

print("Safe Approach (Empty Dict):", max_value_key_safe({}))  # Output: None


# ==================================================
# Summary of Approaches
# ==================================================
# 1. Basic Manual Tracking:
#       - Pros: Easy to explain, works everywhere
#       - Cons: Slightly longer code
#
# 2. Pythonic max() Approach:
#       - Pros: Clean, one-liner, Python best practice
#       - Cons: May look “magical” to beginners
#
# Time Complexity for all approaches: O(n)
# Space Complexity for all approaches: O(1)
