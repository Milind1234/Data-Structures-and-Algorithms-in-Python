# ============================================================
# Problem: Check if Two Lists Have Same Frequency of Elements
# ============================================================

# ------------------------------------------------------------
# 1. Problem Statement
# ------------------------------------------------------------
# Define a function that takes two lists and checks whether they
# contain the same frequency of elements (order does not matter).
#
# Example:
# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# Output: False
#
# Reason: Frequency of elements is different:
# list1 -> {1:2, 2:2, 3:1}
# list2 -> {3:2, 1:1, 2:1}
# ------------------------------------------------------------

# ------------------------------------------------------------
# 2. Approach 1: Using collections.Counter (Pythonic & Clean)
# ------------------------------------------------------------
from collections import Counter

def check_same_frequency_counter(list1, list2):
    # Step 1: Length check
    if len(list1) != len(list2):
        return False
    # Step 2: Compare frequency counts
    return Counter(list1) == Counter(list2)

# Complexity:
# Time: O(n) -> Counting + Comparison
# Space: O(k) -> k = unique elements

# Example Usage
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency_counter(list1, list2))  # Output: False

list3 = [1, 2, 3, 2, 1]
list4 = [2, 1, 1, 3, 2]
print(check_same_frequency_counter(list3, list4))  # Output: True


# ------------------------------------------------------------
# 3. Approach 2: Manual Dictionary Counting (Without Counter)
# ------------------------------------------------------------
def count_frequency(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    return freq

def check_same_frequency_manual(list1, list2):
    # Step 1: Length check
    if len(list1) != len(list2):
        return False
    
    # Step 2: Create frequency dictionaries manually
    freq1 = count_frequency(list1)
    freq2 = count_frequency(list2)
    
    # Step 3: Compare dictionaries
    return freq1 == freq2

# Complexity:
# Time: O(n) -> Two passes to count + comparison
# Space: O(k) -> k = unique elements

# Example Usage
print(check_same_frequency_manual(list1, list2))  # Output: False
print(check_same_frequency_manual(list3, list4))  # Output: True


# ------------------------------------------------------------
# 4. Approach 3: Sorting + Comparison (Less Efficient)
# ------------------------------------------------------------
def check_same_frequency_sorting(list1, list2):
    # Step 1: Length check
    if len(list1) != len(list2):
        return False
    # Step 2: Sort and compare directly
    return sorted(list1) == sorted(list2)

# Complexity:
# Time: O(n log n) -> Sorting dominates
# Space: O(1) (if sorted in-place)
print(check_same_frequency_sorting(list1, list2))  # Output: False
print(check_same_frequency_sorting(list3, list4))  # Output: True


# ------------------------------------------------------------
# Summary:
# ------------------------------------------------------------
# Approach 1 (Counter): Clean and Pythonic (Recommended)
# Approach 2 (Manual Dict): Shows understanding of hashing
# Approach 3 (Sorting): Good when sorting is already needed elsewhere
# ------------------------------------------------------------
