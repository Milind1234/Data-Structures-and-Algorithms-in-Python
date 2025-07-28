# ============================================================
# Conditional Filter in Dictionary (Problem Notes)
# ============================================================

"""
PROBLEM:
--------
Define a function that takes a dictionary as input and returns a new dictionary
containing only those elements which satisfy a given condition.

Example:
--------
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
Output: {'b': 2, 'd': 4}
"""

# ============================================================
# APPROACH 1: BASIC LOOP
# ============================================================

def filter_dict_basic(my_dict, condition):
    """
    Filters dictionary using a basic loop approach.
    
    Parameters:
        my_dict (dict): Input dictionary
        condition (function): A function that takes key, value and returns True/False
    
    Returns:
        dict: New dictionary containing only items that meet the condition
    """
    filtered = {}
    for k, v in my_dict.items():
        if condition(k, v):
            filtered[k] = v
    return filtered

# Example Run
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(filter_dict_basic(my_dict, lambda k, v: v % 2 == 0))
# Output: {'b': 2, 'd': 4}

# Complexity:
# Time Complexity: O(n) → Iterates through all items once
# Space Complexity: O(n) → Stores filtered dictionary (in worst case all elements)


# ============================================================
# APPROACH 2: DICTIONARY COMPREHENSION (PYTHONIC)
# ============================================================

def filter_dict_comprehension(my_dict, condition):
    """
    Filters dictionary using dictionary comprehension.
    """
    return {k: v for k, v in my_dict.items() if condition(k, v)}

# Example Run
print(filter_dict_comprehension(my_dict, lambda k, v: v % 2 == 0))
# Output: {'b': 2, 'd': 4}

# Complexity:
# Time Complexity: O(n)
# Space Complexity: O(n)


# ============================================================
# COMPARISON OF APPROACHES
# ============================================================

"""
1) Basic Loop Approach:
   - Easy to understand for beginners.
   - Explicit and step-by-step.

2) Dictionary Comprehension:
   - One-liner and pythonic.
   - Preferred in interviews for conciseness.

For large data, both have the same complexity, so choose based on readability.
"""

# ============================================================
# SUMMARY:
# ============================================================
"""
- Used condition as a lambda function to keep code reusable.
- Filtering performed in O(n) time.
- Dictionary comprehension is the most pythonic solution.
"""
