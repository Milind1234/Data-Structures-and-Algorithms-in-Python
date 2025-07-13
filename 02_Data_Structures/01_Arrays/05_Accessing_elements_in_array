# -----------------------------------------
# 📘 Accessing Elements in an Array in Python
# -----------------------------------------

# Importing array module
import array as arr

# Creating an array of integers
arr_1 = arr.array('i', [1, 2, 3, 4, 5])

# ✅ Function to access an element at a given index
def access_element(array, idx):
    if idx < 0 or idx >= len(array):
        print("❌ Invalid index: No element at this index.")
    else:
        print(f"✅ Element at index {idx} is: {array[idx]}")

# Taking input from the user
try:
    index = int(input("Enter the index number of the element you want to access: "))
    access_element(arr_1, index)
except ValueError:
    print("❌ Please enter a valid integer index.")

# -----------------------------------------
# 🧠 Time and Space Complexity
# -----------------------------------------

# Time Complexity: O(1)
# - Accessing any index in an array is done in constant time.

# Space Complexity: O(1)
# - No extra space is used apart from a few variables (constant space).
