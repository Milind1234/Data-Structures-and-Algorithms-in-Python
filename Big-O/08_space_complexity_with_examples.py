# ------------------------------------------------------
# 🧠 SPACE COMPLEXITY EXPLAINED (with examples)
# ------------------------------------------------------

# Space complexity measures the amount of memory (RAM) an algorithm uses
# as the size of input increases.
# It's just as important as time complexity, especially when memory is limited.

# ==========================================================
# 🧪 EXAMPLE 1: Recursive Function ➝ Space Complexity: O(n)
# ==========================================================

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

# ▶️ Call the function with input 3
print(recursive_sum(3))

# ------------------------------------------------------
# 🧠 Explanation - Step by Step (with Stack Visualization)
# ------------------------------------------------------
# Each recursive call waits for the next one to return,
# so all of them stay in memory until the base case is reached.
# This builds up a call stack of depth n.

# Let's visualize the stack growth:
#
#     ┌──────────────┐
#     │ recursive_sum(3) │
#     ├──────────────┤
#     │ recursive_sum(2) │
#     ├──────────────┤
#     │ recursive_sum(1) │
#     ├──────────────┤
#     │ recursive_sum(0) │ → returns 0
#     └──────────────┘
#
# Then, the stack unwinds as follows:
# recursive_sum(1) ➝ 1 + 0 = 1
# recursive_sum(2) ➝ 2 + 1 = 3
# recursive_sum(3) ➝ 3 + 3 = 6
#
# ✅ Space Complexity = O(n) (n stack frames held in memory)

# ==============================================================
# 🧪 EXAMPLE 2: Function with Loop & Helper Call ➝ O(1) Space
# ==============================================================

def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i + 1)
    return total

def pair_sum(a, b):
    return a + b

# ▶️ Call the function with input 4
print(pair_sum_sequence(4))

# ------------------------------------------------------
# 🧠 Explanation - Step by Step
# ------------------------------------------------------
# pair_sum_sequence(4) runs a loop from i = 0 to 3 (4 iterations)
# On each iteration, it calls the helper function `pair_sum` which executes and returns immediately.
# So at no point are multiple function calls waiting in memory.

# 🌀 Iteration-wise Breakdown:
# i = 0 → total = 0 + pair_sum(0,1) → total = 1
# i = 1 → total = 1 + pair_sum(1,2) → total = 4
# i = 2 → total = 4 + pair_sum(2,3) → total = 9
# i = 3 → total = 9 + pair_sum(3,4) → total = 16

# ✅ Space Complexity = O(1)
# Because no matter how big n gets, we only store:
# ➤ 'total' variable
# ➤ 'i' loop index
# ➤ 'a' and 'b' inside the helper function — one at a time

# So only a constant amount of memory is used!

# ------------------------------------------------------
# 📌 CONCLUSION:
# ------------------------------------------------------
# 1️⃣ Recursive calls ➝ O(n) space (due to call stack)
# 2️⃣ Iterative calls with immediate return ➝ O(1) space
#
# Remember:
# ➤ Time complexity measures operations
# ➤ Space complexity measures memory usage
#
# ✅ GOOD BYE EVERYONE !
