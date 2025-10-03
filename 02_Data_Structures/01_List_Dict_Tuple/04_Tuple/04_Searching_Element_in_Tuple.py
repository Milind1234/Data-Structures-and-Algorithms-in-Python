# ==============================================================
# Searching an Element in a Tuple
# ==============================================================

# Sample Tuple
sample_tuple = ('a', 'b', 'c', 'd', 'e')

# ==============================================================
# 1. Using 'in' Operator
# ==============================================================
# Syntax:
# element in tuple_name
# Returns True if element exists, else False
print("'a' in sample_tuple:", 'a' in sample_tuple)   # True
print("'f' in sample_tuple:", 'f' in sample_tuple)   # False

# Time Complexity: O(n) → performs linear search internally
# Space Complexity: O(1)

# ==============================================================
# 2. Using index() Method
# ==============================================================
# Syntax:
# tuple_name.index(element)
# Returns index of element, raises ValueError if not present
try:
    idx = sample_tuple.index('c')
    print("'c' found at index:", idx)
except ValueError:
    print("'c' not found")

# Time Complexity: O(n) → searches elements one by one
# Space Complexity: O(1)

# ==============================================================
# 3. Custom Search Function
# ==============================================================
def search_tuple(p_tuple, element):
    for i in range(len(p_tuple)):
        if p_tuple[i] == element:
            return f"Element '{element}' found at index {i}"
    return f"Element '{element}' not found"

print(search_tuple(sample_tuple, 'b'))   # Element found
print(search_tuple(sample_tuple, 'f'))   # Element not found

# Time Complexity: O(n) → loop visits each element until found or end
# Space Complexity: O(1) → no extra memory required

# ==============================================================
# Summary:
# - 'in' → Quick True/False check
# - index() → Gives position but raises error if not found
# - Custom Function → Gives meaningful message without exception
# All have O(n) time complexity since tuples do not support hashing for direct lookup.
# ==============================================================
