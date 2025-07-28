# ================================
# Reverse Key-Value Pairs in Dictionary
# ================================

# Problem:
# --------
# Given a dictionary, reverse the key-value pairs such that
# keys become values and values become keys.
#
# Example:
# --------
# Input:  {'a': 1, 'b': 2, 'c': 3}
# Output: {1: 'a', 2: 'b', 3: 'c'}
#
# Edge Cases:
# -----------
# 1) Duplicate values -> Last key with that value will overwrite previous ones.
# 2) Empty dictionary -> Should return an empty dictionary.
# ================================


# -----------------------
# Approach 1: Basic Loop
# -----------------------
# Steps:
# 1. Create an empty dictionary
# 2. Loop through original dictionary items
# 3. Swap key and value and insert into new dictionary
# Time Complexity: O(n) -> iterate all items once
# Space Complexity: O(n) -> new dictionary of same size

def reverse_dict_basic(my_dict):
    reversed_dict = {}
    for key, value in my_dict.items():
        reversed_dict[value] = key
    return reversed_dict


# -------------------------------
# Approach 2: Dictionary Comprehension
# -------------------------------
# Pythonic way using one-liner
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_dict_comprehension(my_dict):
    return {value: key for key, value in my_dict.items()}


# ================
# Example Run
# ================
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original:", my_dict)
print("Reversed (Basic):", reverse_dict_basic(my_dict))
print("Reversed (Comprehension):", reverse_dict_comprehension(my_dict))
