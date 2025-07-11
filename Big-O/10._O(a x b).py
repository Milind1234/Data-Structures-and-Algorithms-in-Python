# ==============================
# Time Complexity: Add vs Multiply
# ==============================

"""
In this lesson, we explore how to calculate time complexity when functions
take two different input variables: a and b.

This is a commonly asked interview topic, so it’s crucial to understand
whether to add or multiply the runtimes based on how the loops are structured.
"""
# ================================================================
# SECTION 2: Multiply the Runtimes — O(a * b)
# ================================================================

def print_items_multiply(a, b):
    # Outer loop runs 'a' times
    for i in range(a):
        # Inner loop runs 'b' times for each 'i'
        for j in range(b):
            print(i, j)  # O(a * b)

"""
🧠 Explanation:
- For every iteration of `i` in range(a), the entire inner loop of `b` runs.
- So if `a = 5` and `b = 10`, the inner print runs 5 * 10 = 50 times.

⏱️ Total Time Complexity = O(a * b)
This is because:
  → “Do this for every that” → We **multiply** the complexities.
"""

# ==============================
# Summary:
# ==============================

"""
Use O(a * b) when:
  - One loop is nested inside another.
  - One depends on the other.

📝 Always analyze based on structure — not just variable names.
"""

# Example Calls
print("\nMultiply Example Output:")
print_items_multiply(3, 2)