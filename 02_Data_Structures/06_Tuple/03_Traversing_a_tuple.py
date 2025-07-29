# ==============================================================
# Traversing Tuples in Python
# ==============================================================

# Sample Tuple
sample_tuple = ('a', 'b', 'c', 'd', 'e')
print("Sample Tuple:", sample_tuple)

# ==============================================================
# 1. For Loop (Direct Iteration)
# ==============================================================
# Syntax:
# for element in tuple_name:
#     # process element
print("\nTraversal using direct for loop:")
for element in sample_tuple:
    print(element)

# Time Complexity: O(n) → visits every element once
# Space Complexity: O(1) → no extra memory used

# ==============================================================
# 2. For Loop with Index (range + len)
# ==============================================================
# Syntax:
# for i in range(len(tuple_name)):
#     tuple_name[i]
print("\nTraversal using index and range():")
for i in range(len(sample_tuple)):
    print(f"Index {i}: {sample_tuple[i]}")

# Time Complexity: O(n)
# Space Complexity: O(1)

# ==============================================================
# 3. While Loop
# ==============================================================
print("\nTraversal using while loop:")
i = 0
while i < len(sample_tuple):
    print(f"Index {i}: {sample_tuple[i]}")
    i += 1

# Time Complexity: O(n)
# Space Complexity: O(1)

# ==============================================================
# 4. Using enumerate() (index + value together)
# ==============================================================
print("\nTraversal using enumerate():")
for index, value in enumerate(sample_tuple):
    print(f"Index {index}: {value}")

# Time Complexity: O(n)
# Space Complexity: O(1)

# ==============================================================
# 5. Using map() Function
# ==============================================================
print("\nTraversal using map():")
list(map(print, sample_tuple))  # map applies print() to each element

# Time Complexity: O(n)
# Space Complexity: O(n) temporarily (map result list if converted)

# ==============================================================
# Summary:
# - Most common: simple for loop
# - All approaches have Time Complexity: O(n)
# - Space Complexity: O(1) (except map if converted to list)
# ==============================================================

