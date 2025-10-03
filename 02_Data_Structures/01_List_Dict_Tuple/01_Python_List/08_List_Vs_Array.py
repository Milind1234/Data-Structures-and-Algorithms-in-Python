"""
Array vs List in Python
=======================

This note explains the similarities and differences between Python lists and arrays.
Also includes practical examples and helpful tips.
"""

# ----------------------
# 🔁 Similarities
# ----------------------

# 1. Both are mutable (i.e., elements can be updated)
# 2. Both can be indexed and iterated
# 3. Both support slicing

# Examples:
my_list = [10, 20, 30, 40]
my_list[1] = 25  # Updating element
print("Updated List:", my_list)

import numpy as np
my_array = np.array([1, 2, 3, 4])
my_array[2] = 10  # Updating element
print("Updated Array:", my_array)

# Slicing
print("List Slice:", my_list[1:3])
print("Array Slice:", my_array[1:3])

# Iteration
for item in my_list:
    print("List Item:", item)

for item in my_array:
    print("Array Item:", item)


# ----------------------
# ⚖️ Differences
# ----------------------

# 1. Arrays support arithmetic operations directly; lists do not.
# 2. Lists can hold mixed data types; arrays require the same data type.

# Arithmetic example:
my_list = [1, 2, 3, 4, 5, 6]
my_array = np.array([1, 2, 3, 4, 5, 6])

# This will work
print("Array divided by 2:", my_array / 2)

# This will cause an error
try:
    print("List divided by 2:", my_list / 2)
except TypeError as e:
    print("Error with list division:", e)

# Mixed types
my_list = [1, 2, 3, "a"]
my_array = np.array([1, 2, 3, "a"])

print("List with mixed types:", my_list)
print("Array with mixed types (converted to strings):", my_array)

# ----------------------
# 💡 Extra Points
# ----------------------

# ✅ Use case recommendations:
# - Use lists when:
#   • You need a flexible container with mixed types.
#   • You are performing general-purpose programming.
# - Use arrays when:
#   • You are doing numerical computations (e.g., data science, machine learning).
#   • Performance and memory optimization is needed.

# ✅ Performance comparison:
# Arrays are faster and more memory-efficient for large numerical datasets.

# ✅ Type enforcement:
# Lists don't enforce types; arrays do.
print(type(my_list[0]))  # <class 'int'>
print(my_array.dtype)    # <U11 (Unicode string of length 11)> if "a" is present

# ✅ Library used:
# Arrays in this context are from NumPy (not to be confused with the standard `array` module).


# ----------------------
# 🧠 Summary (Checklist)
# ----------------------

# Feature                  | List       | NumPy Array
# ------------------------|------------|-------------
# Mutable                 | ✅ Yes     | ✅ Yes
# Supports Slicing        | ✅ Yes     | ✅ Yes
# Can Index & Iterate     | ✅ Yes     | ✅ Yes
# Arithmetic Ops          | ❌ No      | ✅ Yes
# Mixed Data Types        | ✅ Yes     | ❌ No
# Type Enforced           | ❌ No      | ✅ Yes
# Performance (large data)| ❌ Slower  | ✅ Faster
