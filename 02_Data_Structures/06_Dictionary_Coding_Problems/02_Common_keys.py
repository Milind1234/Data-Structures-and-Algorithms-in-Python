# ========================================
# Problem: Merge Two Dictionaries & Sum Common Keys
# ========================================

# Example:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# Expected Output → {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# ========================================
# APPROACH 1: Manual Loop (Basic Approach)
# ========================================
def merge_dicts_basic(dict1, dict2):
    # Copy first dictionary
    new_dict = dict1.copy()
    
    # Loop through dict2 and add/update keys
    for key in dict2:
        if key in new_dict:
            new_dict[key] += dict2[key]
        else:
            new_dict[key] = dict2[key]
    
    return new_dict

# Time Complexity: O(n + m)  (n = len(dict1), m = len(dict2))
# Space Complexity: O(n + m)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print("Basic Approach Output:", merge_dicts_basic(dict1, dict2))


# ========================================
# APPROACH 2: Dictionary Comprehension
# ========================================
# One-liner for merging and summing common keys
merged_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}

print("Comprehension Approach Output:", merged_dict)

# ---------- HOW IT WORKS ----------
# {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}

# 1) set(dict1) | set(dict2)
#    - Creates union of all keys from both dictionaries.
#    - Example: {'a', 'b', 'c'} | {'b', 'c', 'd'} = {'a', 'b', 'c', 'd'}

# 2) dict1.get(k, 0)
#    - Safely gets value for key 'k' from dict1, default 0 if key missing.
#    - Similarly dict2.get(k, 0) does the same for dict2.

# 3) dict1.get(k, 0) + dict2.get(k, 0)
#    - Adds values of same keys, or just value from one dictionary if the key is unique.

# 4) {k: value for k in keys}
#    - Dictionary comprehension builds a new dictionary with summed values.

# ---------- EXAMPLE EXECUTION ----------
# Key 'a' → 1 (from dict1) + 0 (missing in dict2) = 1
# Key 'b' → 2 (dict1) + 3 (dict2) = 5
# Key 'c' → 3 (dict1) + 4 (dict2) = 7
# Key 'd' → 0 (missing in dict1) + 5 (dict2) = 5
# Final Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# Time Complexity: O(n + m) → Iterates through all unique keys once
# Space Complexity: O(n + m) → Stores new merged dictionary
