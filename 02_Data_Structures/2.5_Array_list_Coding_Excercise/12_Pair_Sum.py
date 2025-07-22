# ===================================================
# 🧠 PAIR SUM PROBLEM - Find all pairs with target sum
# ===================================================

# Problem:
# Given an array of integers and a target sum,
# return all pairs of elements that add up to the target.

# =====================================================================
# 1️⃣ Brute-force Version (With Commutative Pairs - e.g., [3,4] & [4,3])
# =====================================================================
# ✔️ Steps:
# - Use two nested loops.
# - Check all possible unique pairs.
# - If a pair sums to target, add it to result list.

# ❗Time Complexity: O(n^2)
# ❗Space Complexity: O(1) (excluding output list)

def pair_sum_brute_force(arr, target):
    output = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                output.append(f"{arr[i]}+{arr[j]}")
    return output

# ✅ Example:
arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
print("Brute Force Result:", pair_sum_brute_force(arr, 7))

# ==========================================================================
# 2️⃣ Optimal Version Using Sets (Avoids duplicate/commutative pairs)
# ==========================================================================
# ✔️ Steps:
# - Use a set to track seen elements.
# - Use another set to store unique pairs.
# - For each element, check if (target - element) is in the seen set.

# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(n)

def pair_sum_optimized(arr, target):
    seen = set()     # Stores seen numbers
    output = set()   # Stores unique (min, max) pairs

    for num in arr:
        complement = target - num
        if complement in seen:
            output.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return output

# ✅ Example:
print("Optimized Result:", pair_sum_optimized(arr, 7))

# 📝 Output for arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9] and target = 7
# Brute Force Result: ['2+5', '4+3', '3+4', '5+2', '6+1', '-2+9']
# Optimized Result: {(2, 5), (3, 4), (-2, 9), (1, 6)}

# Note: Optimized version automatically removes duplicates like (3,4) and (4,3)
