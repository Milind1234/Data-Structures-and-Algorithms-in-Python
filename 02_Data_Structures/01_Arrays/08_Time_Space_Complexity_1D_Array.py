# -------------------------------------------------------------
# 📘 Time and Space Complexity of Array Operations in Python
# -------------------------------------------------------------

# ✅ 1. Creating an Empty Array
# Time Complexity: O(1)
# Space Complexity: O(1)
# No elements to process or store yet.
import array as arr
empty_array = arr.array('i', [])
print("Empty array created:", empty_array.tolist())

# ✅ 2. Creating an Array with Elements
# Time Complexity: O(n)
# Space Complexity: O(n)
# We are allocating contiguous memory and inserting each element.
arr_with_elements = arr.array('i', [1, 2, 3, 4, 5])
print("Array with elements:", arr_with_elements.tolist())

# ✅ 3. Inserting a Value in an Array
# Time Complexity: O(n) (worst case: insertion at start/middle → shifts elements)
# Space Complexity: O(1)
arr_with_elements.insert(0, 0)  # Insert at beginning (worst case)
print("After inserting 0 at beginning:", arr_with_elements.tolist())

# ✅ 4. Traversing a Given Array
# Time Complexity: O(n)
# Space Complexity: O(1)
print("Traversing array:")
for i in arr_with_elements:
    print(i, end=" ")
print()

# ✅ 5. Accessing a Given Cell (by index)
# Time Complexity: O(1)
# Space Complexity: O(1)
index = 3
print(f"Accessing element at index {index}:", arr_with_elements[index])

# ✅ 6. Searching a Given Value (Linear Search)
# Time Complexity: O(n)
# Space Complexity: O(1)
search_element = 4
found = False
for i in range(len(arr_with_elements)):
    if arr_with_elements[i] == search_element:
        print(f"Element {search_element} found at index {i}")
        found = True
        break
if not found:
    print(f"Element {search_element} not found in array.")

# ✅ 7. Deleting a Given Value
# Time Complexity: O(n) (due to shifting elements)
# Space Complexity: O(1)
delete_value = 2
if delete_value in arr_with_elements:
    arr_with_elements.remove(delete_value)
    print(f"Element {delete_value} removed. Array after deletion:", arr_with_elements.tolist())
else:
    print(f"Element {delete_value} not found in array.")

# -------------------------------------------------------------
# 📌 Summary:
#
# Operation                        Time       Space
# --------------------------------------------------
# Creating an empty array          O(1)       O(1)
# Creating array with elements     O(n)       O(n)
# Inserting value                  O(n)       O(1)
# Traversing array                 O(n)       O(1)
# Accessing element (by index)     O(1)       O(1)
# Searching value (linear search)  O(n)       O(1)
# Deleting value                   O(n)       O(1)
# -------------------------------------------------------------
