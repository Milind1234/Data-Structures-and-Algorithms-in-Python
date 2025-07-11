# -------------------------------------------------------------------
# 📌 O(n²) – Quadratic Time Complexity
# -------------------------------------------------------------------

def print_items(n):
    """
    🔁 This function prints all pairs (i, j) for a given input size n.
    
    🧠 It uses two nested loops:
    ➤ Outer loop runs n times
    ➤ Inner loop runs n times for each outer loop

    ⏱️ Total operations = n × n = n² → O(n²)
    """

    for i in range(n):           # Outer loop → O(n)
        for j in range(n):       # Inner loop → O(n)
            print(f"( {i} , {j} )")  # ➤ Prints coordinate pairs (i, j)


# ▶️ Test the function with n = 10
print_items(10)

# -------------------------------------------------------------------
# 🧠 DETAILED EXPLANATION:
# -------------------------------------------------------------------
#
# ➤ This function has two nested loops, one inside the other.
# ➤ Each loop runs `n` times, so the total operations = n * n = n².
#
# Example:
#   If n = 10, the output will contain 100 coordinate pairs like:
#   (0, 0), (0, 1), ..., (9, 9)
#
# Output sample:
# (0, 0) (0, 1) ... (0, 9)
# (1, 0) (1, 1) ... (1, 9)
# ...
# (9, 0) (9, 1) ... (9, 9)
#
# So the number of operations = 100 ➝ O(n²)

# -------------------------------------------------------------------
# 📈 GRAPHICAL VIEW (ASCII Style)
# -------------------------------------------------------------------
 
#                O(n^2)
#      |           /                         / O(n)
#    O |          /                       /
#    P |         /                     /
#    E |        /                   /
#    R |       /                 /
#    A |      /               /
#    T |     /             /
#    I |    /          /
#    O |   /       /
#    N |  /     /
#    S |_/_ / __ __ __ __ __ __ __ __ __ __  O(1)
#      |/__ __ __ __ __ __ __ __ __ __ __ __
#             E L E M E N T S

# 📊 Interpretation:
# - O(1) is constant — flat line at the bottom
# - O(n) is linear — gentle slope
# - O(n²) is quadratic — steep curve 📈

# -------------------------------------------------------------------
# 🚫 O(n²) is inefficient for large input sizes!
# -------------------------------------------------------------------
#
#   ➤ For n = 10   ➝ 100 operations
#   ➤ For n = 100  ➝ 10,000 operations
#   ➤ For n = 1000 ➝ 1,000,000 operations 😨
#
#   That’s why nested loops are costly and should be avoided when possible.
# -------------------------------------------------------------------
