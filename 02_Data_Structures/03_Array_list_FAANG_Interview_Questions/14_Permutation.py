"""
=============================================================
🔁 PERMUTATION CHECKER – TWO METHODS
=============================================================

👉 Problem:
Check whether two lists (or strings) are permutations of each other.

That means:
- Both should contain the exact same elements.
- The order doesn't matter, but the frequency must be identical.

=============================================================
1️⃣ Using Sorting
=============================================================
Steps:
- Step 1: Check if both lists are of the same length.
- Step 2: Sort both lists.
- Step 3: Compare if sorted versions are equal.

✅ Time Complexity: O(n log n)
✅ Space Complexity: O(1) (ignoring output)

"""

def permutation_sorting(l1, l2):
    if len(l1) != len(l2):
        return False
    l1.sort()
    l2.sort()
    return l1 == l2

# Example usage:
l1 = ['a', 'b', 'c', 'd']
l2 = ['b', 'c', 'd', 'a']
print("Using Sorting:", permutation_sorting(l1, l2))  # Output: True


"""
=============================================================
2️⃣ Using Counter (from collections module)
=============================================================
Steps:
- Step 1: Check if lengths are equal.
- Step 2: Use Counter to count frequency of elements.
- Step 3: Compare both Counters.

✅ Time Complexity: O(n)
✅ Space Complexity: O(n)

"""

from collections import Counter

def permutation_counter(l1, l2):
    if len(l1) != len(l2):
        return False
    return Counter(l1) == Counter(l2)

# Example usage:
print("Using Counter:", permutation_counter(l1, l2))  # Output: True
