# --------------------------------------------------------------
# 📘 Time_complexity_notations_explained.py
# --------------------------------------------------------------
# 🔍 In this, we will explore:
#     ✅ What is Big O Notation?
#     ✅ Why is it needed?
#     ✅ Types of Notations (Big O, Omega, Theta)
#     ✅ Real-world analogies
#     ✅ Examples to understand each concept clearly
# --------------------------------------------------------------

# --------------------------------------------------------------
# ✅ WHAT IS BIG O NOTATION?
# --------------------------------------------------------------
# Big O is the language we use to describe the efficiency of algorithms.
# It helps us answer: "How does the runtime or memory usage grow
# as the input size increases?"
#
# Big O = Time/Space Complexity = Number of operations (not seconds!)
#
# 📦 Analogy: Imagine sending a file to a friend. If the file is small,
# electronic transfer (email/FTP) is fast. But if the file is HUGE,
# flying with a physical hard drive might be faster!
#
# In computer science:
#     - Electronic transfer ➝ Time increases *with size* (Linear) → O(n)
#     - Flying a hard drive ➝ Time stays *constant* (Independent of size) → O(1)
#
# ➕ This illustrates how runtime depends on input size (n).

# --------------------------------------------------------------
# ✅ WHY IS BIG O IMPORTANT?
# --------------------------------------------------------------
# 🧠 Helps analyze how fast or slow your code is
# 🚀 Makes it easier to choose the most efficient algorithm
# 📈 Essential for technical interviews
# 💻 Used to compare two pieces of code doing the same task

# --------------------------------------------------------------
# ✅ WHAT DOES BIG O MEASURE?
# --------------------------------------------------------------
# It doesn't measure **seconds** but instead:
#     ➤ Number of operations (Time Complexity)
#     ➤ Amount of memory used (Space Complexity)
#
# 💡 Example:
#   Code A takes 30s on a slow PC, 10s on a fast PC
#   Code B takes 60s on a slow PC, 20s on a fast PC
#   ➤ Big O looks at operations (independent of hardware)

# --------------------------------------------------------------
# ✅ TYPES OF NOTATIONS
# --------------------------------------------------------------
# 🔸 Big O (O): Worst-case performance (most common)
# 🔹 Omega (Ω): Best-case performance
# 🔸 Theta (Θ): Average-case performance
#
# 🧮 Real-life Analogy - Finding a number in a list:
#   arr = [1, 2, 3, 4, 5, 6, 7, 8]
#
#   - Searching for 1 ➝ Found instantly ➝ Best Case ➝ Ω(1)
#   - Searching for 4 ➝ Found midway ➝ Average Case ➝ Θ(n)
#   - Searching for 8 ➝ Found at end ➝ Worst Case ➝ O(n)
#
#   So,
#   🔹 Ω (Omega) → Best Case
#   🔸 Θ (Theta) → Average Case
#   🔸 O (Big O) → Worst Case

# --------------------------------------------------------------
# ✅ BIG O IN PRACTICE: COMMON COMPLEXITIES
# --------------------------------------------------------------
# ➤ O(1)     ➝ Constant Time
# ➤ O(log n) ➝ Logarithmic Time (e.g., Binary Search)
# ➤ O(n)     ➝ Linear Time (e.g., Loop through array)
# ➤ O(n log n) ➝ Quasilinear Time (e.g., Merge Sort)
# ➤ O(n^2)   ➝ Quadratic Time (e.g., Nested Loops)
# ➤ O(2^n)   ➝ Exponential Time
# ➤ O(n!)    ➝ Factorial Time (e.g., Permutations)

# --------------------------------------------------------------
# ✅ SIMPLE EXAMPLES
# --------------------------------------------------------------

# O(1) ➝ Constant Time Example

def get_first_item(arr):
    return arr[0]  # Only one operation regardless of input size

# O(n) ➝ Linear Time Example

def print_all_items(arr):
    for item in arr:
        print(item)  # Prints each item once ➝ Operations grow with size

# O(n^2) ➝ Quadratic Time Example

def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # Every element pairs with every other ➝ n * n

# O(log n) ➝ Logarithmic Time Example (Binary Search Style)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# --------------------------------------------------------------
# ✅ FINAL THOUGHTS
# --------------------------------------------------------------
# 🔁 Always consider:
#     - How fast is the algorithm as input grows?
#     - How much memory does it use?
#
# 🎯 Choose algorithms with better time & space complexity whenever possible
# 📚 Big O = your best friend in writing efficient code
# 💼 You’ll 100% be asked about it in coding interviews
# --------------------------------------------------------------
