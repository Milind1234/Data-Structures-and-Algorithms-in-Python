    # --------------------------------------------------
# 📘 Deleting Elements from an Array in Python
# --------------------------------------------------

import array as arr

# Step 1: Create an array of integers
arr_1 = arr.array('i', [10, 20, 30, 40, 50])
print("Original Array:", arr_1.tolist())

# ✅ Method 1: Remove element by value (first occurrence)
# Time Complexity: O(n) — because it searches for the element first
# Space Complexity: O(1) — done in-place
def delete_by_value(array, value):
    if value in array:
        array.remove(value)
        print(f"✅ Element {value} removed. Array after deletion:", array.tolist())
    else:
        print(f"❌ Element {value} not found in array.")

# ✅ Method 2: Delete element by index using pop(index)
# Time Complexity: O(n) — elements after index must be shifted
# Space Complexity: O(1)
def delete_by_index(array, index):
    if 0 <= index < len(array):
        removed = array.pop(index)
        print(f"✅ Element {removed} at index {index} removed. Array after deletion:", array.tolist())
    else:
        print("❌ Invalid index. No element deleted.")

# ✅ Method 3: Delete last element using pop()
# Time Complexity: O(1) — no shifting needed
# Space Complexity: O(1)
def delete_last_element(array):
    if len(array) > 0:
        removed = array.pop()
        print(f"✅ Last element {removed} removed. Array after deletion:", array.tolist())
    else:
        print("❌ Array is empty. No element to delete.")

# ✅ Method 4: Delete using del keyword
# Time Complexity: O(n) — shifts elements after index
# Space Complexity: O(1)
def delete_using_del(array, index):
    if 0 <= index < len(array):
        print(f"✅ Element {array[index]} at index {index} removed using del.")
        del array[index]
        print("Array after deletion:", array.tolist())
    else:
        print("❌ Invalid index for deletion using del.")

# ✅ Testing all methods
delete_by_value(arr_1, 30)       # Remove by value
delete_by_index(arr_1, 1)        # Remove at index 1
delete_last_element(arr_1)       # Remove last element
delete_using_del(arr_1, 0)       # Delete using del at index 0
