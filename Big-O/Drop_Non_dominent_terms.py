# -------------------------------------------------------------------
# 📌 Function to Demonstrate Time Complexity: O(n² + n) ➝ O(n²)
# -------------------------------------------------------------------

def print_items(n):
    """
    🧪 This function demonstrates how Big O time complexity works
    using both a nested loop (O(n²)) and a single loop (O(n)).

    🔹 Nested Loop  → O(n²)
    🔹 Single Loop  → O(n)

    🧠 Total Time Complexity = O(n² + n)
    ✅ Simplified as O(n²)
    """

    # ----------------------------------------
    # 🔁 Part 1 - Nested Loop: O(n²)
    # ----------------------------------------
    for i in range(n):
        for j in range(n):
            print(f"( {i} , {j} )")  # ➤ Prints all (i, j) pairs

    # ----------------------------------------
    # 🔁 Part 2 - Single Loop: O(n)
    # ----------------------------------------
    for k in range(n):
        print(k)  # ➤ Prints numbers from 0 to n-1


# -------------------------------------------------------
# ▶️ Let's test the function with n = 10
# -------------------------------------------------------
print_items(10)

# -------------------------------------------------------------------
# 🧠 DETAILED EXPLANATION:
# -------------------------------------------------------------------

# 🔁 1️⃣ NESTED LOOP (O(n²)):
#
# for i in range(n):
#     for j in range(n):
#         print(f"( {i} , {j} )")
#
# 📌 Outer loop runs n times
# 📌 Inner loop also runs n times → Total = n * n = n²
# ✅ Time Complexity = O(n²)
#
# Example:
# If n = 10 ➝ it prints 100 coordinate pairs: (0,0) to (9,9)

# 🔁 2️⃣ SINGLE LOOP (O(n)):
#
# for k in range(n):
#     print(k)
#
# 📌 Runs n times → O(n)
# Example: If n = 10 ➝ prints numbers 0 to 9

# -------------------------------------------------------------------
# 📊 TOTAL TIME COMPLEXITY:
# -------------------------------------------------------------------
#
#     O(n²) + O(n)
#
# ✅ But in Big O, we care about how the function grows as input increases.
#    Since n² grows MUCH faster than n, we drop the non-dominant term (O(n)).

# -------------------------------------------------------------------
# 🎯 FINAL TIME COMPLEXITY:
#     ✅ O(n²)
# -------------------------------------------------------------------
#
# Example:
# ➤ If n = 100 → n² = 10,000, but n = 100
# ➤ So the 100 extra steps barely matter compared to 10,000
#
# That’s why we drop O(n) and just write O(n²)

# -------------------------------------------------------------------
# 🔥 BIG O SIMPLIFICATION RULES:
# -------------------------------------------------------------------
# 📌 Drop Constants:      O(2n) ➝ O(n)
# 📌 Drop Small Terms:    O(n² + n) ➝ O(n²)
# -------------------------------------------------------------------
