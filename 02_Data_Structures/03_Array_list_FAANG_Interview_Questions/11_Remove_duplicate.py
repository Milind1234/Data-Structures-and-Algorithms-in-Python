 # Question:
# Remove duplicates from a list while preserving the original order.

# Example input:
lst = [1, 1, 2, 2, 3, 4, 5]

# -----------------------------------------------------
# ✅ Method 1: Optimized approach (preserve order)

def remove_duplicates(lst):
    unique_lst = []
    seen = set()  # Used for fast O(1) lookup
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# --- Step-by-step Working ---
# lst = [1, 1, 2, 2, 3, 4, 5]
# unique_lst = [] → Will store final result
# seen = set() → Tracks already seen items
#
# Loop:
# item = 1 → not in seen → add to unique_lst → [1] → seen = {1}
# item = 1 → in seen → skip
# item = 2 → not in seen → [1, 2] → seen = {1, 2}
# item = 2 → in seen → skip
# item = 3 → not in seen → [1, 2, 3] → seen = {1, 2, 3}
# item = 4 → not in seen → [1, 2, 3, 4] → seen = {1, 2, 3, 4}
# item = 5 → not in seen → [1, 2, 3, 4, 5] → seen = {1, 2, 3, 4, 5}

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n) for set and list


# -----------------------------------------------------
# ⚠️ Method 2: Simple approach (removes duplicates but sorts)

def remove_duplicates_sorted(arr):
    return sorted(set(arr))

print(remove_duplicates_sorted([1, 1, 2, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# --- Step-by-step Working ---
# Convert list to set → removes duplicates (unordered)
# Then sort the set → O(n log n)
# Returns a sorted list without duplicates

# ⚠️ Limitation: Original order is NOT preserved

# ⏱ Time Complexity: O(n log n)
# ⏳ Space Complexity: O(n) for set and sorted list


# -----------------------------------------------------
# 🔍 Conclusion:
# - Use Method 1 when you want to preserve original order (✅ Optimal)
# - Use Method 2 only when sorted output is acceptable and order doesn't matter
