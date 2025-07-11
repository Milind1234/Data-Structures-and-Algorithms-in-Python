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
# SECTION 1: Add the Runtimes — O(a + b)
# ================================================================

def print_items_add(a, b):
    # First loop runs 'a' times
    for i in range(a):
        print(i)  # O(a)
    
    # Second loop runs 'b' times
    for j in range(b):
        print(j)  # O(b)

"""
🧠 Explanation:
- The first loop runs independently for `a` elements => O(a)
- The second loop runs independently for `b` elements => O(b)
- These loops are sequential, not nested.

⏱️ Total Time Complexity = O(a) + O(b) = O(a + b)
This is because:
  → “Do this, then do that” → We **add** the complexities.
"""
# ==============================
# Summary:
# ==============================

"""
Use O(a + b) when:
  - Two loops run one after another.
  - They are **independent**.

  📝 Always analyze based on structure — not just variable names.
"""
# Example Calls
print("\nAdd Example Output:")
print_items_add(3, 2)
