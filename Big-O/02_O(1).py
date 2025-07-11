# -------------------------------------------------------------------
# 📌 Understanding O(1) - Constant Time Complexity
# -------------------------------------------------------------------

# 💡 O(1) means:
# The number of operations does NOT depend on the size of the input.
# It always performs the same number of operations — just one!

# -------------------------------------------------------------------
# 🧪 Example Function
# -------------------------------------------------------------------

def multiply_number(n):
    return n * n  # ✅ One operation: multiplication

# 🔁 Call the function with a value
print(multiply_number(5))  # Output: 25

# 🔁 Call it again with a large number
print(multiply_number(100))  # Output: 10000

# -------------------------------------------------------------------
# 🧠 Explanation:
# -------------------------------------------------------------------
#
# This function always performs just **one multiplication**:
#     ➤ n * n
#
# So even if `n` is:
#     - 1
#     - 100
#     - 1,000,000
#
# The number of operations = 1 (always)
#
# That’s why it is called:
# ✅ O(1) ➝ Constant Time Complexity
#

# -------------------------------------------------------------------
# 🎴 Real-Life Analogy:
# -------------------------------------------------------------------
# Imagine a deck of cards.
# If someone asks you to pick ANY one card at random (without searching),
# you just reach in and grab one — that’s a **single constant action**.
#
# You don’t loop through the deck to find it — just one action:
# ➤ ✅ Constant time.

# -------------------------------------------------------------------
# 📊 Graphical Representation (ASCII Style)
# -------------------------------------------------------------------
#
#      |
#    O |                                ← Flat line = constant
#    P |
#    E |
#    R |
#    A |
#    T |
#    I |
#    O |
#    N |
#    S |__ __ __ __ __ __ __ __ __ __ __ __  O(1)
#      |__ __ __ __ __ __ __ __ __ __ __ __
#             E L E M E N T S  (input size ➝)
#
# 🔍 On the X-axis: number of elements (input size)
# 🔍 On the Y-axis: number of operations
# 📉 As input increases, the operation count stays the same ➝ flat graph

# -------------------------------------------------------------------
# ✅ Final Notes:
# -------------------------------------------------------------------
# - O(1) is the most efficient time complexity possible.
# - It’s also called **Constant Time**.
# - You may hear both: "O(1)" or "Constant Time Complexity".
#
# 🔥 Remember:
#     If the input grows, but the number of steps stays the same ➝ O(1)
