# -------------------------------------------------------------------
# 📌 O(2n) ➝ O(n) — Dropping Constants in Big O Notation
# -------------------------------------------------------------------

def print_items(n):
    """
    This function prints numbers twice:
    1️⃣ First loop prints 0 to n-1
    2️⃣ Second loop also prints 0 to n-1

    Total operations = n + n = 2n ➝ O(2n)
    But in Big O, we DROP the constant ➝ O(n)
    """

    # 🔁 First loop - O(n)
    for i in range(n):
        print(i)

    # 🔁 Second loop - O(n)
    for j in range(n):
        print(j)

# ▶️ Call the function with n = 10
print_items(10)

# -------------------------------------------------------------------
# 🧠 EXPLANATION:
# -------------------------------------------------------------------
#
# We have TWO separate loops:
#     - The first loop runs n times (0 to n-1)
#     - The second loop runs n times (0 to n-1)
#
# So total operations:
#     n (from first loop) + n (from second loop) = 2n
#
# Time Complexity:
#     ➤ O(2n)
#
# BUT... in Big O, we only care about how the function grows
# as input gets large — constants don’t matter!

# -------------------------------------------------------------------
# 🔥 RULE: Drop Constants
# -------------------------------------------------------------------
#     O(2n) ➝ O(n)
#     O(5n) ➝ O(n)
#     O(100n + 50) ➝ O(n)
#
# Constants are dropped because they don’t affect the growth rate.

# -------------------------------------------------------------------
# 📊 VISUAL (ASCII STYLE)
# -------------------------------------------------------------------
#
#      |                                    / O(n)
#    O |                                 /
#    P |                              /
#    E |                           /
#    R |                        /
#    A |                     /
#    T |                  /
#    I |              /
#    O |          /
#    N |       /
#    S |__ / __ __ __ __ __ __ __ __ __ __  O(1)
#      |/__ __ __ __ __ __ __ __ __ __ __ __
#             E L E M E N T S
#
# 🔺 O(2n) and O(n) have similar shape — they grow linearly.
# Big O cares about the shape of the growth, not the scale.

# -------------------------------------------------------------------
# ✅ FINAL TAKEAWAY:
# -------------------------------------------------------------------
# - Even though this function runs TWO loops, both are O(n)
# - Combined: O(n + n) = O(2n)
# - Drop the constant ➝ ✅ O(n)
#
# ✨ Rule #1 of Big O simplification:
#     ➤ Drop constants!
#
#     So always simplify:
#         O(2n) ➝ O(n)
#         O(10) ➝ O(1)
# -------------------------------------------------------------------
