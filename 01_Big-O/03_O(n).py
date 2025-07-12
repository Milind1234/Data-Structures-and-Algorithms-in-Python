# -------------------------------------------------------------------
# 📌 O(n) – Linear Time Complexity
# -------------------------------------------------------------------

def print_items(n):
    """
    📦 This function prints numbers from 0 to n-1.
    
    🔁 It runs a single loop from 0 to n.
    ➤ The number of operations grows directly with the size of input `n`.
    
    ⏱️ Time Complexity: O(n)
    """

    for i in range(n):
        print(i)

# ▶️ Test the function with n = 10
print_items(10)

# -------------------------------------------------------------------
# 🧠 EXPLANATION:
# -------------------------------------------------------------------
#
# We define a function `print_items(n)` that runs a loop from 0 to n-1.
#
# 👉 If n = 10 → prints 10 numbers (0 to 9)
# 👉 If n = 5  → prints 5 numbers (0 to 4)
# 👉 If n = 100 → prints 100 numbers (0 to 99)
#
# So as the input increases, the number of operations increases *linearly*.
#
# ✅ That’s what we call **O(n)** ➝ Linear Time Complexity.
#
# In simple words:
#     If input is n, function runs n times.

# -------------------------------------------------------------------
# 📈 GRAPHICAL VIEW (ASCII Style)
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
# 🔍 X-axis = Number of elements (input size)
# 🔍 Y-axis = Number of operations performed
#
# The number of operations grows at the same rate as the input → 📈 Linear

# -------------------------------------------------------------------
# ✅ FINAL TAKEAWAY:
# -------------------------------------------------------------------
# - O(n) is called Linear Time Complexity.
# - It means as input increases, operations increase at the same rate.
# - Perfect for simple loops that run once per input element.
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